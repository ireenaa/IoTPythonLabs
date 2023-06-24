from models.ship import Ship


class Warship(Ship):
    """
        Class representing a warship, derived from the Ship class.

        Attributes:
            name (str): The name of the warship.
            capacity (int): The capacity of the warship.
            speed (int): The speed of the warship.
            type_of_weapon (str): The type of weapon carried by the warship.
            interacts_with (str): The type of entities the warship interacts with.
            ship_class (str): The classification of the warship.
        """

    def __init__(self, name="", capacity=0, speed=0,
                 type_of_weapon="", interacts_with="", ship_class=""):
        """
               The constructor for Warship class.

               Parameters:
                   name (str): The name of the warship.
                   capacity (int): The capacity of the warship.
                   speed (int): The speed of the warship.
                   type_of_weapon (str): The type of weapon carried by the warship.
                   interacts_with (str): The type of entities the warship interacts with.
                   ship_class (str): The classification of the warship.
               """

        super().__init__(name, capacity, speed)
        self.type_of_weapon = type_of_weapon
        self.interacts_with = interacts_with
        self.ship_class = ship_class

    def __str__(self):
        """
               Returns a string representation of the Warship object.

               Returns:
                   str: A formatted string containing the values of the Warship object's attributes.
               """
        return f"Warship(name={self.name},capacity={self.capacity}, speed={self.speed}," \
               f"type_of_weapon={self.type_of_weapon}, interacts_with={self.interacts_with}" \
               f"ship_class={self.ship_class})"

    def get_total_people_count(self) -> int:
        """
                Returns the total number of people on the warship.

                Returns:
                    int: The total number of people on the warship.
                """
        return 0

    def calculate_load_time(self) -> int:
        """
                Calculates the load time for the warship.

                Returns:
                    int: The calculated load time for the warship.
                """
        return 0
