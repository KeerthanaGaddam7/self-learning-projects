import json
import math

from jsonschema import validate

from trust_score.schema import TRUST_SCORE_SCHEMA


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
 
    total = sum(weights)

    if not math.isclose(total, 1.0, rel_tol=1e-9):
        return normalize_weights(weights)

    return weights

def validate_input(file_path: str):

    data = load_input(file_path)

    validate_schema(data)

    original_total = sum(data["weights"])

    normalized = not math.isclose(original_total, 1.0, rel_tol=1e-9)

    data["weights"] = validate_weights(data["weights"])

    data["weights_normalized"] = normalized

    return data