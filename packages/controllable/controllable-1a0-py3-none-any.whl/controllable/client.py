from .models import *
from .http_client import HTTPClient
from .decoder import decode_execution_results_from_json


class Client:
    def __init__(self, controllable_endpoint: str, app_key: str, environment: str, default_timeouts: dict[str, float]) -> None:
        self.controllable_endpoint = controllable_endpoint
        self.app_key = app_key
        self.environment = environment
        self.default_timeouts = default_timeouts

        try:
            self.default_create_property_value_timeout = float(
                default_timeouts["create_property_value"])
        except:
            self.default_create_property_value_timeout = None

        try:
            self.default_read_property_value_timeout = float(
                default_timeouts["read_property_value"])
        except:
            self.default_read_property_value_timeout = None

        try:
            self.default_update_property_value_timeout = float(
                default_timeouts["update_propert_value"])
        except:
            self.default_update_property_value_timeout = None

        try:
            self.default_delete_property_value_timeout = float(
                default_timeouts["delete_property_value"])
        except:
            self.default_delete_property_value_timeout = None

        self.http_client = HTTPClient(
            self.controllable_endpoint, self.app_key, self.environment)

    def create_property_value(self, property_reference_value_pairs: PropertyReferenceValuePairs, timeout: float = None) -> ExecutionResults:
        timeout = timeout or self.default_create_property_value_timeout or 5

        requests = []

        for property_reference_value_pair in property_reference_value_pairs.get():
            property_reference = property_reference_value_pair.get_property_reference()
            property_value = property_reference_value_pair.get_property_value()
            property_value_segment = property_value.get_segment()

            segment_path_components = []

            if property_value_segment:
                for segment_path_component_name, segment_path_component_value in property_value_segment:
                    segment_path_components.append({
                        "name": segment_path_component_name,
                        "value": segment_path_component_value
                    })

            requests.append({
                "property": {
                    "namespace": property_reference.get_namespace(),
                    "key": property_reference.get_key(),
                    "version": property_reference.get_version()
                },
                "value": {
                    "data": property_value.get_value(),
                    "rule": {
                        "expression": property_value.get_rule()
                    },
                    "segment": {
                        "path": segment_path_components
                    }
                },
            })

        response = self.http_client.execute(
            "CREATE_PROPERTY_VALUE", requests, timeout)

        return decode_execution_results_from_json(response)

    def read_property_value(self, read_property_requests: ReadPropertyRequests, timeout: float = None) -> ExecutionResults:
        timeout = timeout or self.default_read_property_value_timeout or 1

        requests = []

        for read_property_request in read_property_requests.get():
            params = read_property_request.get_params()
            property_reference = read_property_request.get_property_reference()

            requests.append({
                "property": {
                    "namespace": property_reference.get_namespace(),
                    "key": property_reference.get_key(),
                    "version": property_reference.get_version()
                },
                "params": params
            })

        response = self.http_client.execute(
            "READ_PROPERTY_VALUE", requests, timeout)

        return decode_execution_results_from_json(response)

    def update_property_value(self, property_reference_value_pairs: PropertyReferenceValuePairs, timeout: float = None) -> ExecutionResults:
        timeout = timeout or self.default_update_property_value_timeout or 5

        requests = []

        for property_reference_value_pair in property_reference_value_pairs.get():
            property_reference = property_reference_value_pair.get_property_reference()
            property_value = property_reference_value_pair.get_property_value()

            requests.append({
                "property": {
                    "namespace": property_reference.get_namespace(),
                    "key": property_reference.get_key(),
                    "version": property_reference.get_version()
                },
                "value": {
                    "id": property_value.get_id(),
                    "data": property_value.get_value(),
                    "rule": {
                        "expression": property_value.get_rule()
                    }
                }
            })

        response = self.http_client.execute(
            "UPDATE_PROPERTY_VALUE", requests, timeout)

        return decode_execution_results_from_json(response)

    def delete_property_value(self, property_reference_value_pairs: PropertyReferenceValuePairs, timeout: float = None) -> ExecutionResults:
        timeout = timeout or self.default_delete_property_value_timeout or 5

        requests = []

        for property_reference_value_pair in property_reference_value_pairs.get():
            property_reference = property_reference_value_pair.get_property_reference()
            property_value = property_reference_value_pair.get_property_value()

            requests.append({
                "property": {
                    "namespace": property_reference.get_namespace(),
                    "key": property_reference.get_key(),
                    "version": property_reference.get_version()
                },
                "value": {
                    "id": property_value.get_id()
                }
            })

        response = self.http_client.execute(
            "DELETE_PROPERTY_VALUE", requests, timeout)

        return decode_execution_results_from_json(response)
