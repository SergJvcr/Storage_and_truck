from Capacity import Capacity
from Unit import Unit

class Truck (Capacity):

    def __init__(self, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity, amount, unit)

    def __str__(self) -> str:
        return f'Truck cap={super().get_capacity()} amount={super().get_amount()}'

    def put(self, request_amount:float):
        super().put(request_amount)

    def unload(self):
        super().amount = 0

    def run(self):
        pass