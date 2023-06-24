
class ShipManager:
    """
    Class representing a ship manager.

    Attributes:
        ships (list): A list to store the ships managed by the manager.
    """
    ships = []

    def add_ship(self, ship):
        """
        Adds a ship to the manager's list of ships.
        :param ship: The ship to be added to the list.

        """
        self.ships.append(ship)

    def get_ships_with_max_speed_than(self, chosen_speed):
        """
        Returns ships with a speed greater than the chosen speed.
        :param chosen_speed:the chosen speed
        :return: a list of ships with a speed greater than the chosen speed
        """
        return list(filter(lambda ship: (ship.speed > chosen_speed), self.ships))

    def get_ships_accommodating_more_than(self, chosen_capacity):
        """
        Returns ships with a capacity greater than the chosen capacity.

        Args:
        :param chosen_capacity:the chosen capacity
        :return: alist of ships with a capacity greater than the chosen capacity.
        """
        return list(filter(lambda ship: (ship.capacity > chosen_capacity), self.ships))
