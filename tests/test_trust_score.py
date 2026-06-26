import pytest

from trust_score.calculator import (
    calculate_weighted_score,
    determine_risk_level
)

from trust_score.validator import (
    validate_weights
)

from trust_score.hashing import (
    generate_sha256
)

from trust_score.models import (
    LOW_RISK,
    MEDIUM_RISK,
    HIGH_RISK
)


def test_calculate_weighted_score():
   
    scores = [90, 80, 75, 88, 95, 85]
    weights = [0.2, 0.2, 0.15, 0.15, 0.2, 0.1]

    result = calculate_weighted_score(scores, weights)

    assert result == 85.95


def test_low_risk():
 

    assert determine_risk_level(95) == LOW_RISK


def test_medium_risk():
 

    assert determine_risk_level(85) == MEDIUM_RISK


def test_high_risk():
  
    assert determine_risk_level(60) == HIGH_RISK


def test_weight_normalization():
  
    weights = [
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2
    ]

    normalized = validate_weights(weights)

    assert round(sum(normalized), 10) == 1.0


def test_zero_weight_sum():
 
    weights = [0, 0, 0, 0, 0, 0]

    with pytest.raises(ValueError):
        validate_weights(weights)


def test_sha256_consistency():

    data = {
        "scores": [90, 80, 75, 88, 95, 85],
        "weights": [0.2, 0.2, 0.15, 0.15, 0.2, 0.1],
        "weighted_score": 85.95,
        "risk_level": MEDIUM_RISK
    }

    hash1 = generate_sha256(data)
    hash2 = generate_sha256(data)

    assert hash1 == hash2