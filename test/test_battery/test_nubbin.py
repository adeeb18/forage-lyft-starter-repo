import unittest
from datetime import date

from battery.NubbinBattery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-05-18")
        last_service_date = date.fromisoformat("2017-05-18")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-05-18")
        last_service_date = date.fromisoformat("2021-05-18")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())