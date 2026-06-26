from trust_score.models import (
    LOW_RISK,
    MEDIUM_RISK,
    HIGH_RISK
)

def calculate_weighted_score(scores: list, weights: list) -> float:

    weighted_score = 0

    for score, weight in zip(scores, weights):
        weighted_score += score * weight

    return round(weighted_score, 2)

    
def determine_risk_level(weighted_score: float) -> str:

    if weighted_score >= 90:
        return LOW_RISK

    elif weighted_score >= 70:
        return MEDIUM_RISK

    else:
        return HIGH_RISK