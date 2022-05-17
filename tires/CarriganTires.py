import numpy as np
from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array
    def needs_service():
        return  not (all(i < 0.9 for i in tire_array))
        