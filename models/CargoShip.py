from Ship import Ship


class CargoShip(Ship):
    TIME_OF_LOADING_CARGO = 60
    AMOUNT_OF_CARGO = 20

    def __init__(self, name="", capacity=0, speed=0,
                 tonnage=0, type_of_cargo=""):
        super().__init__(name, capacity, speed)
        self.tonnage = tonnage
        self.type_of_cargo = type_of_cargo

    def __str__(self):
        return f"CargoShip(name={self.name}, capacity={self.capacity}, speed={self.speed}," \
               f"tonnage={self.tonnage}, type_of_cargo={self.type_of_cargo})"

    def get_total_people_count(self) -> int:
        return 0

    def calculate_load_time(self) -> int:
        return self.tonnage // self.AMOUNT_OF_CARGO * self.TIME_OF_LOADING_CARGO
