from ship import Ship


class CruiseShip(Ship):
    """
       Class representing a cruise ship, derived from the Ship class.

       Attributes:
           name (str): The name of the cruise ship.
           passengers_count (int): The number of passengers on the cruise ship.
           crew_count (int): The number of crew members on the cruise ship.
           support_staff_count (int): The number of support staff members on the cruise ship.
           capacity (int): The capacity of the cruise ship.
           speed (int): The speed of the cruise ship.
           TIME_OF_LOADING_ONE_PERSON (int): The time taken to load one person on the cruise ship.
    """
    TIME_OF_LOADING_ONE_PERSON = 5

    def __init__(self, name="",passengers_count=0, crew_count=0,
                 support_staff_count=0, capacity=0, speed=0):
        """
        The constructor for Cruise ship class.

        Parameters:
           name (str): The name of the cruise ship.
           passengers_count (int): The number of passengers on the cruise ship.
           crew_count (int): The number of crew members on the cruise ship.
           support_staff_count (int): The number of support staff members on the cruise ship.
           capacity (int): The capacity of the cruise ship.
           speed (int): The speed of the cruise ship.

        """
        super().__init__(name, capacity, speed)
        self.passengers_count = passengers_count
        self.crew_count = crew_count
        self.support_staff_count = support_staff_count

    def __str__(self):
        """
        Returns a string representation of the CruiseShip object.

        Returns:
            str: A formatted string containing the values of the CruiseShip object's attributes.
        """

        return f"CruiseShip(name={self.name},capacity={self.capacity}, speed={self.speed}" \
               f" passengers_count={self.passengers_count}, crew_count={self.crew_count}" \
               f"support_staff_count={self.support_staff_count})"

    def get_total_people_count(self) -> int:
        """
               Returns the total number of people on the cruise ship.

               Returns:
                   int: The total number of people on the cruise ship.
               """
        return self.passengers_count + self.crew_count + self.support_staff_count

    def calculate_load_time(self) -> int:
        """
                Calculates the load time for the cruise ship.

                Returns:
                    int: The calculated load time for the cruise ship.
                """
        return self.TIME_OF_LOADING_ONE_PERSON * self.get_total_people_count()
