from models.Ship import Ship


class Tanker(Ship):

    def __init__(self, name="", capacity=0, speed=0,
                 length_of_ship=0, volume=0):
        super().__init__(name, capacity, speed)
        self.length_of_ship = length_of_ship
        self.volume = volume

    def __str__(self):
        return f"Tanker(name={self.name},capacity={self.capacity}, speed={self.speed}," \
               f" length_of_ship={self.length_of_ship}, volume={self.volume})"

    def get_total_people_count(self) -> int:
        return 0

    def calculate_load_time(self) -> int:
        return 0
