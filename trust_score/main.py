from trust_score.validator import validate_input

from trust_score.calculator import (
    calculate_weighted_score,
    determine_risk_level
)

from trust_score.hashing import generate_sha256


def main():

    try:

        data = validate_input("sample_input.json")

        weighted_score = calculate_weighted_score(
            data["scores"],
            data["weights"]
        )

        risk_level = determine_risk_level(
            weighted_score
        )

        evidence = {
            "scores": data["scores"],
            "weights": data["weights"],
            "weights_normalized": data["weights_normalized"],
            "weighted_score": weighted_score,
            "risk_level": risk_level
        }
        evidence_hash = generate_sha256(
            evidence
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