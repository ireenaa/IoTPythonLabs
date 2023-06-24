from abc import ABC, abstractmethod


class Ship(ABC):
    """
        Abstract base class representing a ship.

        Attributes:
            name (str): The name of the ship.
            speed (int): The speed of the ship.
            capacity (int): The maximum capacity of the ship.

        Methods:
            get_total_people_count(): Abstract method to get the total number of people on the ship.
            calculate_load_time(): Abstract method to calculate the load time for the ship.
        """

    # __instance = None

    def __init__(self, name="", speed=0, capacity=0):
        """
                The constructor for Ship class.

                Parameters:
                   name (str): The name of the ship.
                   speed (int): The speed of the ship.
                   capacity (int): The maximum capacity of the ship.
                """
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
        """
            Abstract method to get the total number of people on the ship.
        """
        pass

    @abstractmethod
    def calculate_load_time(self):
        """
            Abstract method to calculate the load time for the ship.
        """
        pass
