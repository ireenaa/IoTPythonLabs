class SetManager:
    def init(self, set_manager):
        self.set_manager = set_manager

    def iter(self):
        for ship in self.set_manager.ships:
            yield from ship

    def len(self):
        lngth = 0
        for ship in self.set_manager.ships:
            lngth += len(ship.favorite_port_set)
        return lngth

    def getitem(self, index):
        return list(self.iter())[index]

    def next(self):

        raise StopIteration