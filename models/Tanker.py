from models.ship import Ship


class Tanker(Ship):
    """
    Class representing a tanker ship, derived from the Ship class

     Attributes:
        name (str): The name of the tanker.
        capacity (int): The capacity of the tanker.
        speed (int): The speed of the tanker.
        length_of_ship (int): The length of the tanker in meters.
        volume (int): The volume of the tanker's cargo.
    """

    def __init__(self, name="", capacity=0, speed=0,
                 length_of_ship=0, volume=0):
        """
        The constructor for Tanker class.

        Parameters:
            name (str): The name of the tanker.
            capacity (int): The capacity of the tanker.
            speed (int): The speed of the tanker in knots.
            length_of_ship (int): The length of the tanker in meters.
            volume (int): The volume of the tanker's cargo.
        """

        super().__init__(name, capacity, speed)
        self.length_of_ship = length_of_ship
        self.volume = volume

    def __str__(self):
        """
               Returns a string representation of the Tanker object.

               Returns:
                   str: A formatted string containing the values of the Tanker object's attributes.
               """
        return f"Tanker(name={self.name},capacity={self.capacity}, speed={self.speed}," \
               f" length_of_ship={self.length_of_ship}, volume={self.volume})"

    def get_total_people_count(self) -> int:
        """
               Returns the total number of people on the tanker.

               Returns:
                   int: The total number of people on the tanker.
               """
        return 0

    def calculate_load_time(self) -> int:
        """
                Calculates the load time for the tanker.

                Returns:
                    int: The calculated load time for the tanker.
                """
        return 0
