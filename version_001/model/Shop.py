from Capacity import Capacity
from Unit import Unit

class Shop(Capacity):
    def __init__(self, address:str, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity=capacity, amount=amount, unit=unit)
        self.address = address

    def __str__(self) -> str:
        return f"The address this shop is {self.address}, capacity: {self.CAPACITY}. Occupancy the shop: {(self.CAPACITY-self.amount)}"