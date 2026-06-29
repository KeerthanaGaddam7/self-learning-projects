import json
import math

from jsonschema import validate

from trust_score.schema import TRUST_SCORE_SCHEMA
from trust_score.tracing import tracer


def load_input(file_path: str) -> dict:

    with open(file_path, "r") as file:
        return json.load(file)


def validate_schema(data: dict):

    validate(
        instance=data,
        schema=TRUST_SCORE_SCHEMA
    )

def normalize_weights(weights: list) -> list:
  
    total = sum(weights)

    if math.isclose(total, 0.0):
        raise ValueError("Weight sum cannot be zero.")

    normalized = [weight / total for weight in weights]

    print(f"⚠️ Weights summed to {total}. They have been normalized.")

    return normalized

def validate_weights(weights: list) -> list:

    with tracer.start_as_current_span("Weight Normalization") as span:

        total = sum(weights)

        span.set_attribute("original_weight_sum", total)

        if not math.isclose(total, 1.0, rel_tol=1e-9):

            normalized = normalize_weights(weights)

            span.set_attribute("weights_normalized", True)

            return normalized

        span.set_attribute("weights_normalized", False)

        return weights

def validate_input(file_path: str):

    data = load_input(file_path)

    validate_schema(data)

    original_total = sum(data["weights"])

    normalized = not math.isclose(original_total, 1.0, rel_tol=1e-9)

    data["weights"] = validate_weights(data["weights"])

    data["weights_normalized"] = normalized

    return data