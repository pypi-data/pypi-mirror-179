from .models import *


def decode_execution_results_from_json(response_json) -> ExecutionResults:
    execution_results = ExecutionResults()

    execution_responses = response_json["responses"]

    for execution_response in execution_responses:
        success = False
        value_id = None
        value_rule = None
        value_segment = None
        value_data = None

        if "success" in execution_response:
            success = execution_response["success"]

        if "value" in execution_response:
            value_response = execution_response["value"]

            if "id" in value_response:
                value_id = value_response["id"]

            if "rule" in value_response:
                rule_response = value_response["rule"]
                if "expression" in rule_response:
                    value_rule = rule_response["expression"]

            if "data" in value_response:
                value_data = value_response["data"]

            if "segment" in value_response:
                segment_response = value_response["segment"]
                if "path" in segment_response:
                    segment_path = segment_response["path"]
                    value_segment = {}
                    for segment_path_component in segment_path:
                        if "name" in segment_path_component and "value" in segment_path_component:
                            value_segment[segment_path_component["name"]
                                          ] = segment_path_component["value"]

        value = PropertyValue(value_data, value_rule,
                              value_segment, value_id)

        execution_results.add(ExecutionResult(success, value))

    return execution_results
