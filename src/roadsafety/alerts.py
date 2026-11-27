from .risk import RiskResult


def level_for(score: int) -> str:
    if score >= 70:
        return "critical"
    if score >= 45:
        return "high"
    if score >= 20:
        return "medium"
    return "low"


def build_alert(shipment_id: str, result: RiskResult) -> dict:
    return {
        "shipment_id": shipment_id,
        "level": level_for(result.score),
        "score": result.score,
        "reasons": result.reasons,
    }
