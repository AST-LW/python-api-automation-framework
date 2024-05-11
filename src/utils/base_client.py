import requests
from typing import TypeVar, Callable
from dataclasses import asdict
from urllib.parse import urljoin
from pydantic.dataclasses import dataclass

from src.utils.config_parser import CONFIG

T = TypeVar("T")


class RequestBuilder:
    def __init__(self):
        self._base_url = CONFIG.BASE_URL
        self._endpoint = None
        self._headers = {}
        self._query_params = {}
        self._path_params = {}
        self._data = None

    def with_endpoint(self, endpoint: str):
        self._endpoint = endpoint
        return self

    def with_headers(self, headers):
        self._headers = headers
        return self

    def with_query_params(self, query_params):
        self._query_params = query_params
        return self

    def with_path_params(self, path_params):
        self._path_params = path_params
        return self

    def with_data(self, data: T):
        self._data = asdict(data)
        return self

    def _build_url(self):
        url: str = urljoin(self._base_url, self._endpoint)
        if self._path_params:
            for key, value in self._path_params.items():
                url = url.replace("{" + key + "}", str(value))

        if self._query_params:
            url += "?" + \
                "&".join([f"{key}={value}" for key,
                         value in self._query_params.items()])

        return url

    def _send_request(self, method):
        url = self._build_url()
        response = method(
            url, json=self._data, headers=self._headers, params=self._query_params)
        return self._parse_response(response)

    def _parse_response(self, response):
        if response.ok:
            return {"status": response.status_code, "data": response.json(), "error": None}
        else:
            return {"status": response.status_code,
                    "data": response.json(), "error": response.text}

# The following code is used to generate the dynamic request builder classes for HTTP methods


def create_request_builder(method):
    class RequestBuilderSubclass(RequestBuilder):
        def send(self):
            return self._send_request(method)

    return RequestBuilderSubclass


@dataclass
class RequestBuilderSubclassModel(RequestBuilder):
    send: Callable[..., T]


@dataclass
class RequestDirectoryModel:
    post: RequestBuilderSubclassModel


RequestDirectory: RequestDirectoryModel = type("RequestDirectory", (),
                                               {method.lower(): create_request_builder(getattr(requests, method.lower()))() for method in ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']})

# The below was earlier code before the dynamic generation of request builder classes for HTTP methods

# class PostRequestBuilder(RequestBuilder):
#     def send(self):
#         return self._send_request(requests.post)


# class GetRequestBuilder(RequestBuilder):
#     def send(self):
#         return self._send_request(requests.get)


# class PutRequestBuilder(RequestBuilder):
#     def send(self):
#         return self._send_request(requests.put)


# class PatchRequestBuilder(RequestBuilder):
#     def send(self):
#         return self._send_request(requests.patch)


# class DeleteRequestBuilder(RequestBuilder):
#     def send(self):
#         return self._send_request(requests.delete)


# class RequestDirectory:
#     post = PostRequestBuilder()
#     get = GetRequestBuilder()
#     put = PutRequestBuilder()
#     patch = PatchRequestBuilder()
#     delete = DeleteRequestBuilder()
