from model.Capacity import Capacity
from model.Unit import Unit
from model.Address import Address

class Shop(Capacity):
    def __init__(self, address:Address, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity=capacity, amount=amount, unit=unit)
        self.address = address

    def __str__(self) -> str:
        return f"The address this shop is {self.address}, capacity: {self.capacity}. Occupancy the shop: {(self.capacity-self.amount)}"