import numpy as np
from tires import Tires

class Octoprime(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array
    def needs_service():
        if tire_array.sum() >= 3 :
            return True
        else :
            return False
        