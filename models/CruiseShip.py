from Ship import Ship


class CruiseShip(Ship):
    TIME_OF_LOADING_ONE_PERSON = 5

    def __init__(self, name="",
                 passengers_count=0, crew_count=0, support_staff_count=0, capacity=0, speed=0):
        super().__init__(name, capacity, speed)
        self.passengers_count = passengers_count
        self.crew_count = crew_count
        self.support_staff_count = support_staff_count

    def __str__(self):
        return f"CruiseShip(name={self.name},capacity={self.capacity}, speed={self.speed}" \
               f" passengers_count={self.passengers_count}, crew_count={self.crew_count}" \
               f"support_staff_count={self.support_staff_count})"

    def get_total_people_count(self) -> int:
        return self.passengers_count + self.crew_count + self.support_staff_count

    def calculate_load_time(self) -> int:
        return self.TIME_OF_LOADING_ONE_PERSON * self.get_total_people_count()
