from typing import List
from models import Ship


class ShipManager:
    ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def get_ships_with_max_speed_than(self, chosen_speed):
        return list(filter(lambda ship: (ship.speed > chosen_speed), self.ships))

    def get_ships_accommodating_more_than(self, chosen_capacity):
        return list(filter(lambda ship: (ship.capacity > chosen_capacity), self.ships))
