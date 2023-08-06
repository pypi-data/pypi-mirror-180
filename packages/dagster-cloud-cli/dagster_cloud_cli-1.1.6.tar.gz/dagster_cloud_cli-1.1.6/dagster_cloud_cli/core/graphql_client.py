import logging
import time
from contextlib import ExitStack, contextmanager
from typing import Any, Dict, Optional

import requests
import urllib3
from packaging.version import Version, parse
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3 import Retry

from ._utils import merge_dicts
from .errors import DagsterCloudHTTPError, DagsterCloudMaintenanceException, GraphQLStorageError
from .headers.auth import DagsterCloudInstanceScope
from .headers.impl import get_dagster_cloud_api_headers

DEFAULT_RETRIES = 6
RETRY_BACKOFF_FACTOR = 0.5
DEFAULT_TIMEOUT = 60

logger = logging.getLogger("dagster_cloud")


class GqlShimClient:
    """Adapter for gql.Client that wraps errors in human-readable format."""

    def __init__(
        self,
        url: str,
        session: requests.Session,
        headers: Optional[Dict[str, Any]] = None,
        verify: bool = True,
        timeout: int = DEFAULT_TIMEOUT,
        cookies: Optional[Dict[str, Any]] = None,
        proxies: Optional[Dict[str, Any]] = None,
    ):
        self._exit_stack = ExitStack()

        self.url = url
        self.headers = headers
        self.verify = verify
        self.timeout = timeout
        self.cookies = cookies
        self._session = session
        self._proxies = proxies

    @property
    def session(self) -> requests.Session:
        return self._session

    def execute(self, query: str, variable_values: Optional[Dict[str, Any]] = None):

        start_time = time.time()

        while True:
            try:
                return self._execute_retry(query, variable_values)
            except DagsterCloudMaintenanceException as e:
                if time.time() - start_time > e.timeout:
                    raise

                logger.warning(
                    "Dagster Cloud is currently unavailable due to scheduled maintenance. Retrying in {retry_interval} seconds...".format(
                        retry_interval=e.retry_interval
                    )
                )
                time.sleep(e.retry_interval)

    def _execute_retry(self, query: str, variable_values: Optional[Dict[str, Any]] = None):
        try:
            response = self._session.post(
                self.url,
                headers=merge_dicts(self.headers, {"Content-type": "application/json"}),
                cookies=self.cookies,
                timeout=self.timeout,
                verify=self.verify,
                json=merge_dicts(
                    {
                        "query": query,
                    },
                    {"variables": variable_values} if variable_values else {},
                ),
                proxies=self._proxies,
            )
            try:
                result = response.json()
                if not isinstance(result, dict):
                    result = {}
            except ValueError:
                result = {}

            if "errors" not in result and "data" not in result and "maintenance" not in result:
                response.raise_for_status()
                raise requests.HTTPError("Unexpected GraphQL response", response=response)

        except HTTPError as http_error:
            raise DagsterCloudHTTPError(http_error) from http_error
        except Exception as exc:
            raise GraphQLStorageError(exc.__str__()) from exc

        if "maintenance" in result:
            maintenance_info = result["maintenance"]
            raise DagsterCloudMaintenanceException(
                message=maintenance_info.get("message"),
                timeout=maintenance_info.get("timeout"),
                retry_interval=maintenance_info.get("retry_interval"),
            )

        if "errors" in result:
            raise GraphQLStorageError(f"Error in GraphQL response: {str(result['errors'])}")
        else:
            return result


def get_agent_headers(config_value: Dict[str, Any], scope: DagsterCloudInstanceScope):
    return get_dagster_cloud_api_headers(
        config_value["agent_token"],
        scope=scope,
        deployment_name=config_value.get("deployment"),
        additional_headers=config_value.get("headers"),
    )


@contextmanager
def create_cloud_requests_session(retries: int = DEFAULT_RETRIES):
    with requests.Session() as session:
        urllib_version = parse(urllib3.__version__)  # type: ignore[attr-defined]
        # method for whitelisting all methods (GET/POST/etc.) is moving from method_whitelist
        # to allowed_methods
        allowed_method_param = (
            {"allowed_methods": None}
            if urllib_version >= Version("1.26.0")
            else {"method_whitelist": None}
        )

        adapter = HTTPAdapter(
            max_retries=Retry(  # pylint: disable=unexpected-keyword-arg
                total=retries,
                backoff_factor=RETRY_BACKOFF_FACTOR,
                status_forcelist=[500, 502, 503, 504],
                **allowed_method_param,  # type: ignore
            )
        )
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        yield session


def create_proxy_client(
    session: requests.Session,
    url: str,
    config_value: Dict[str, Any],
    scope: DagsterCloudInstanceScope = DagsterCloudInstanceScope.DEPLOYMENT,
):
    return GqlShimClient(
        url=url,
        headers=merge_dicts(
            {"Content-type": "application/json"}, get_agent_headers(config_value, scope=scope)
        ),
        verify=config_value.get("verify", True),
        timeout=config_value.get("timeout", DEFAULT_TIMEOUT),
        cookies=config_value.get("cookies", {}),
        proxies=config_value.get("proxies"),
        session=session,
    )


@contextmanager
def create_cloud_dagit_client(url: str, api_token: str, retries=3):
    with create_cloud_requests_session(retries=retries) as session:
        yield GqlShimClient(
            session=session,
            url=f"{url}/graphql",
            headers=get_dagster_cloud_api_headers(
                api_token, scope=DagsterCloudInstanceScope.DEPLOYMENT
            ),
        )
