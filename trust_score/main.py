from trust_score.validator import validate_input

from trust_score.calculator import (
    calculate_weighted_score,
    determine_risk_level
)

from trust_score.hashing import generate_sha256
from trust_score.tracing import tracer


def main():
 
    try:

        with tracer.start_as_current_span("Trust Score Request") as parent_span:

            parent_span.set_attribute(
                "application",
                "Trust Score Calculator"
            )

            parent_span.set_attribute(
                "version",
                "1.0"
            )

            
            with tracer.start_as_current_span("Input Validation") as span:

                data = validate_input("sample_input.json")

                span.set_attribute(
                    "weights_normalized",
                    data["weights_normalized"]
                )

                span.set_attribute(
                    "score_count",
                    len(data["scores"])
                )

                span.set_attribute(
                    "weight_count",
                    len(data["weights"])
                )

            
            with tracer.start_as_current_span("Score Calculation") as span:

                weighted_score = calculate_weighted_score(
                    data["scores"],
                    data["weights"]
                )

                risk_level = determine_risk_level(
                    weighted_score
                )

                span.set_attribute(
                    "weighted_score",
                    weighted_score
                )

                span.set_attribute(
                    "risk_level",
                    risk_level
                )

            # Update parent span
            parent_span.set_attribute(
                "final_score",
                weighted_score
            )

            parent_span.set_attribute(
                "risk_level",
                risk_level
            )

            with tracer.start_as_current_span("Evidence Generation") as span:

                evidence = {
                    "scores": data["scores"],
                    "weights": data["weights"],
                    "weights_normalized": data["weights_normalized"],
                    "weighted_score": weighted_score,
                    "risk_level": risk_level
                }

                span.set_attribute(
                    "evidence_fields",
                    len(evidence)
                )

            with tracer.start_as_current_span("SHA256 Hash") as span:

                evidence_hash = generate_sha256(
                    evidence
                )

                span.set_attribute(
                    "hash_length",
                    len(evidence_hash)
                )

        print("\nTrust Score Calculator")

        print(f"Weighted Score : {weighted_score}")

        print(f"Risk Level     : {risk_level}")

        print("\nEvidence")

        print(evidence)

        print("\nSHA-256")

        print(evidence_hash)

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()