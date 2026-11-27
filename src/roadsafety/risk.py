"""Prototype risk scoring for hazardous-materials shipments.

All thresholds and weights are ILLUSTRATIVE EXAMPLES, not official limits.
They must be reviewed by road-safety experts and the competent authorities.
"""
from dataclasses import dataclass, field
from math import radians, sin, cos, asin, sqrt
from typing import List, Tuple


@dataclass
class Position:
    lat: float
    lon: float
    speed_kmh: float
    stopped_minutes: float = 0.0


@dataclass
class Shipment:
    id: str
    planned_route: List[Tuple[float, float]]
    speed_limit_kmh: float = 70.0
    hours_driven_today: float = 0.0
    inspection_valid: bool = True
    bad_weather: bool = False


@dataclass
class RiskResult:
    score: int
    reasons: List[str] = field(default_factory=list)


def distance_km(a, b) -> float:
    lat1, lon1, lat2, lon2 = map(radians, (a[0], a[1], b[0], b[1]))
    h = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return 2 * 6371.0 * asin(sqrt(h))


def route_deviation_km(pos: Position, route) -> float:
    return min(distance_km((pos.lat, pos.lon), p) for p in route)


def assess_risk(shipment: Shipment, pos: Position) -> RiskResult:
    score, reasons = 0, []
    over = pos.speed_kmh - shipment.speed_limit_kmh
    if over > 0:
        score += min(40, int(over * 2))
        reasons.append(f"سرعة أعلى من الحد المسموح بـ {over:.0f} كم/س")
    dev = route_deviation_km(pos, shipment.planned_route)
    if dev > 1.0:
        score += 25
        reasons.append(f"خروج عن المسار المخطط بمسافة {dev:.1f} كم")
    if pos.stopped_minutes > 20:
        score += 15
        reasons.append(f"توقف غير معتاد {pos.stopped_minutes:.0f} دقيقة")
    if shipment.hours_driven_today > 8:
        score += 20
        reasons.append(f"ساعات قيادة طويلة ({shipment.hours_driven_today:.1f} ساعة)")
    if not shipment.inspection_valid:
        score += 30
        reasons.append("فحص المركبة منتهٍ")
    if shipment.bad_weather:
        score += 10
        reasons.append("طقس سيئ")
    return RiskResult(min(score, 100), reasons)
