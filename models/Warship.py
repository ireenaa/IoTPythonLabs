from models.Ship import Ship


class Warship(Ship):

    def __init__(self, name="", capacity=0, speed=0,
                 type_of_weapon="", interacts_with="", ship_class=""):
        super().__init__(name, capacity, speed)
        self.type_of_weapon = type_of_weapon
        self.interacts_with = interacts_with
        self.ship_class = ship_class

    def __str__(self):
        return f"Warship(name={self.name},capacity={self.capacity}, speed={self.speed}," \
               f"type_of_weapon={self.type_of_weapon}, interacts_with={self.interacts_with}" \
               f"ship_class={self.ship_class})"

    def get_total_people_count(self) -> int:
        return 0

    def calculate_load_time(self) -> int:
        return 0
