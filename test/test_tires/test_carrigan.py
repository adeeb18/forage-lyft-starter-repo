import numpy as np
import unittest

from tires.CarriganTires import CarriganTires


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tire_array = np.array([.95, .8, .7, .6])
        tires = CarriganTires(tire_array)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        tire_array = np.array([.85, .8, .7, .6])
        tires = CarriganTires(tire_array)
        self.assertFalse(engine.needs_service())