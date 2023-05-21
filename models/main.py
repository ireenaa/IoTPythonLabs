from managers.ShipManager import ShipManager
from models.CargoShip import CargoShip
from models.CruiseShip import CruiseShip
from models.Tanker import Tanker
from models.Warship import Warship

if __name__ == "__main__":
    ship_manager = ShipManager()
    ship_manager.add_ship(CargoShip("Joseph", 530, 100, 800, "cars"))
    ship_manager.add_ship(CargoShip("Shelters", 570, 487, 549, "tractors"))
    ship_manager.add_ship(Tanker("Knock Nevis", 325, 800, 670, 450))
    ship_manager.add_ship(Tanker("Nina", 470, 674, 580, 560))
    ship_manager.add_ship(CruiseShip("Titanyk", 250, 456, 500, 300, 300))
    ship_manager.add_ship(Warship("Velox", 350, 500, 574, "rocket", "marines"))
    ship_manager.add_ship(Warship("Irenia", 250, 450, 650, "artillery", "aviation"))

    for ship in ship_manager.ships:
        print(ship)

    get_ships_with_max_speed_than = ship_manager.get_ships_with_max_speed_than(300)
    print("\nShip with more speed than 300:")
    for ship in get_ships_with_max_speed_than:
        print(ship)

    get_ships_accommodating_more_than = ship_manager.get_ships_accommodating_more_than(300)
    print("\nShip that accommodates more than 300:")
    for ship in get_ships_accommodating_more_than:
        print(ship)



