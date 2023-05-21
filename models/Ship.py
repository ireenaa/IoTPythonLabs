from abc import ABC, abstractmethod


class Ship(ABC):

    # __instance = None

    def __init__(self, name="", speed=0, capacity=0):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    # @classmethod
    # def get_instance(cls):
    #   if not cls.__instance:
    #        cls.__instance = Ship()
    #   return cls.__instance

    @abstractmethod
    def get_total_people_count(self):
        pass

    @abstractmethod
    def calculate_load_time(self):
        pass
