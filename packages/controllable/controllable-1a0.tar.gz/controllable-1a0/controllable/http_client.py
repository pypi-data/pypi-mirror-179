import requests


class HTTPClient:
    def __init__(self, controllable_endpoint: str, app_key: str, environment: str) -> None:
        self.controllable_endpoint = controllable_endpoint
        self.app_key = app_key
        self.environment = environment

    def execute(self, operation: str, request_list: list, timeout_in_seconds: float):
        execution_requests = {
            "operation": operation,
            "environment": self.environment,
            "requests": request_list,
        }

        res = requests.post(url=self.controllable_endpoint + "/api/v1/properties/execute",
                            json=execution_requests,
                            headers=self.get_headers(),
                            timeout=timeout_in_seconds)

        if not res.ok:
            response_json = res.json()

            if "message" in response_json:
                raise Exception(response_json["message"])
            else:
                raise Exception(
                    "Unkown exception while calling controllable server")

        response_json = res.json()

        if "responses" not in response_json:
            raise Exception("Responses not present in result from server")

        return response_json

    def get_headers(self):
        return {
            "Authorization": "AppKey " + self.app_key
        }
