import sys, unittest
sys.path.insert(0, "src")
from roadsafety import Position, Shipment, assess_risk, level_for

ROUTE = [(30.05, 31.20), (30.10, 31.25)]


class RiskTests(unittest.TestCase):
    def test_normal_trip_is_low(self):
        r = assess_risk(Shipment("a", ROUTE), Position(30.05, 31.20, 60))
        self.assertEqual(r.score, 0)
        self.assertEqual(level_for(r.score), "low")

    def test_speeding_adds_reason(self):
        r = assess_risk(Shipment("a", ROUTE), Position(30.05, 31.20, 90))
        self.assertGreater(r.score, 0)
        self.assertEqual(len(r.reasons), 1)

    def test_many_factors_are_critical(self):
        s = Shipment("a", ROUTE, hours_driven_today=10, inspection_valid=False, bad_weather=True)
        r = assess_risk(s, Position(30.40, 31.60, 100, stopped_minutes=30))
        self.assertEqual(level_for(r.score), "critical")
        self.assertLessEqual(r.score, 100)


if __name__ == "__main__":
    unittest.main()
