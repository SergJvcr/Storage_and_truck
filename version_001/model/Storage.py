from model.Capacity import Capacity
from model.Unit import Unit

class Storage (Capacity):
    def __init__(self, address:str, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity=capacity, amount=amount, unit=unit)
        self.address = address

    def __str__(self) -> str:
        return f"The address this storage is {self.address}, capacity: {self.CAPACITY}. Occupancy the storage: {(self.amount)}"
