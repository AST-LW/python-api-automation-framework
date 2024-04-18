from dataclasses import dataclass
import requests
from urllib.parse import urljoin

from config.config_reader import CONFIG


class RequestBuilder:
    def __init__(self):
        self._base_url = CONFIG.get("BASE_URL")
        self._endpoint = None
        self._headers = {}
        self._query_params = {}
        self._path_params = {}
        self._data = None

    def with_endpoint(self, endpoint):
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

    def with_data(self, data):
        self._data = data
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


class PostRequestBuilder(RequestBuilder):
    def send(self):
        url = self._build_url()
        response = requests.post(
            url, json=self._data, headers=self._headers)
        return self._parse_response(response)

    def _parse_response(self, response):
        if response.ok:
            return {"status": response.status_code, "data": response.json(), "error": None}
        else:
            return {"status": response.status_code,
                    "data": response.json(), "error": response.text}

# class GetRequestBuilder(RequestBuilder):
#     def send(self, response_model: Type[BaseModel]) -> ResponseConfig:
#         url = self._build_url()
#         if self._data == None:
#             response = requests.get(url=url, headers=self._headers)
#         else:
#             response = requests.get(
#                 url=url, json=self._data, headers=self._headers)
#         return self._parse_response(response, response_model)

#     def _parse_response(self, response, response_model: Type[BaseModel]) -> ResponseConfig:
#         if response.ok:
#             return ResponseConfig(status=response.status, data=response_model.model_validate(response.json()))
#         else:
#             return ResponseConfig(status=response.status_code, error=response.text)

# class PutRequestBuilder(RequestBuilder):
#     def send(self):
#         url = self._build_url()
#         response = requests.put(url, json=self._data, headers=self._headers)
#         return response


# class DeleteRequestBuilder(RequestBuilder):
#     def send(self):
#         url = self._build_url()
#         if self._data == None:
#             response = requests.delete(url, headers=self._headers)
#         else:
#             response = requests.delete(
#                 url=url, json=self._data, headers=self._headers)
#         return response


# class PatchRequestBuilder(RequestBuilder):
#     def send(self):
#         url = self._build_url()
#         response = requests.patch(url, json=self._data, headers=self._headers)
#         return response


class RequestDirectory:
    # @staticmethod
    # def create_get_request():
    #     return GetRequestBuilder()

    @staticmethod
    def create_post_request():
        return PostRequestBuilder()

    # @staticmethod
    # def create_put_request():
    #     return PutRequestBuilder()

    # @staticmethod
    # def create_delete_request():
    #     return DeleteRequestBuilder()

    # @staticmethod
    # def create_patch_request():
    #     return PatchRequestBuilder()
