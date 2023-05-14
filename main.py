class Ship:
    ID=10.4
    def __init__(self, name="St.John",
                   current_port="LA",
                   max_speed=200,
                   max_capacity=300,
                   current_load=245 ):

        self.name = name
        self.current_port = current_port
        self.max_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load


    def dock(self, port ):
        self.current_port = port
        print("Current port is", port)
        return port

    def set_speed(self, speed):
        self.max_speed = speed
        print("Max speed is ", speed)
        return speed

    def load(self, weight):
        if self.current_load + weight < self.max_capacity:
            self.current_load += weight
        print("We are load ", weight)

    def unload(self, weight):
        if self.current_load - weight > 0:
            self.current_load -= weight
        print("We are unload ", weight)

    instance = None
    @staticmethod
    def get_instance():
        if not Ship.instance:
            Ship.instance = Ship()
        return Ship.instance

ships = [Ship(), Ship("Irenia", "LA", 300, 9000, 3444), Ship.get_instance(), Ship.get_instance()]

for ship in ships:
    print(ship.__dict__)