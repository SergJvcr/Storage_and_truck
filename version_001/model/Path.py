from Address import Address


class Path:
    def __init__(self, addr1:Address, addr2:Address, distance:float):
        self.address1 = addr1
        self.address2 = addr2
        self.distance = distance
