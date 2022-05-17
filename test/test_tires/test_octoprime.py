import numpy as np
import unittest

from tires.OctoprimeTires import OctoprimeTires  


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tire_array = np.array([.95, .8, .7, .6])
        tires = CarriganTires(tire_array)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        tire_array = np.array([.5, .5, .5, .5])
        tires = CarriganTires(tire_array)
        self.assertFalse(engine.needs_service())