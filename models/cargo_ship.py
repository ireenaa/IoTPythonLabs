from ship import Ship


class CargoShip(Ship):
    """
        Class representing a cargo ship, derived from the Ship class.

        Attributes:
            name (str): The name of the cargo ship.
            capacity (int): The capacity of the cargo ship.
            speed (int): The speed of the cargo ship.
            tonnage (int): The tonnage of the cargo ship.
            type_of_cargo (str): The type of cargo carried by the cargo ship.
            TIME_OF_LOADING_CARGO (int): The time taken to load a specific amount of cargo.
            AMOUNT_OF_CARGO (int): The amount of cargo loaded per unit time.
            """
    TIME_OF_LOADING_CARGO = 60
    AMOUNT_OF_CARGO = 20

    def __init__(self, name="", capacity=0, speed=0,
                 tonnage=0, type_of_cargo=""):
        """
        The constructor for Tanker class.

        Parameters:
            name (str): The name of the cargo ship.
            capacity (int): The capacity of the cargo ship.
            speed (int): The speed of the cargo ship.
            tonnage (int): The tonnage of the cargo ship.
            type_of_cargo (str): The type of cargo carried by the cargo ship.
        """

        super().__init__(name, capacity, speed)
        self.tonnage = tonnage
        self.type_of_cargo = type_of_cargo

    def __str__(self):
        """
                Returns a string representation of the CargoShip object.

                Returns:
                    str: A formatted string containing the values of the CargoShip object's attributes.
                """
        return f"CargoShip(name={self.name}, capacity={self.capacity}, speed={self.speed}," \
               f"tonnage={self.tonnage}, type_of_cargo={self.type_of_cargo})"

    def get_total_people_count(self) -> int:
        """
               Returns the total number of people on the cargo ship.

               Returns:
                   int: The total number of people on the cargo ship.
               """
        return 0

    def calculate_load_time(self) -> int:
        """
                Calculates the load time for the cargo ship.

                Returns:
                    int: The calculated load time for the cargo ship.
                """
        return self.tonnage // self.AMOUNT_OF_CARGO * self.TIME_OF_LOADING_CARGO
