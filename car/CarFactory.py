from abc import ABC, abstractmethod
from car import Car
from engine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine import SternmanEngine
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        e = CapuletEngine(last_service_mileage, current_mileage)
        b = SpindlerBattery(last_service_date, current_date)
        c  = Car(e, b)
        return c

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        e = WilloughbyEngine(last_service_mileage, current_mileage)
        b = SpindlerBattery(last_service_date, current_date)
        c  = Car(e, b)
        return c

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        e = SternmanEngine(warning_light_on)
        b = SpindlerBattery(last_service_date, current_date)
        c  = Car(e, b)
        return c

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        e = WilloughbyEngine(last_service_mileage, current_mileage)
        b = NubbinBattery(last_service_date, current_date)
        c  = Car(e, b)
        return c

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        e = CapuletEngine(last_service_mileage, current_mileage)
        b = NubbinBattery(last_service_date, current_date)
        c  = Car(e, b)
        return c


    
    