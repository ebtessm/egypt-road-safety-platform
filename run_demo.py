import json, sys
sys.path.insert(0, "src")
from roadsafety import Position, Shipment, assess_risk, build_alert

with open("examples/sample_shipments.json", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    pos = Position(**item.pop("position"))
    item["planned_route"] = [tuple(p) for p in item["planned_route"]]
    s = Shipment(**item)
    alert = build_alert(s.id, assess_risk(s, pos))
    print(json.dumps(alert, ensure_ascii=False))
