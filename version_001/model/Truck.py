from model.Capacity import Capacity
from model.Unit import Unit
from model.Actor import Actor

class Truck (Capacity, Actor):

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