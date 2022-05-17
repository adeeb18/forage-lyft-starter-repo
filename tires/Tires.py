from abc import abstractmethod, ABC

class Tires(ABC):
     def __init__(self, tire_array):
        self.tire_array = tire_array

    @abstractmethod
    def needs_service():
        pass
