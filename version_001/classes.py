class Unit:
    def __init__(self, code:str, title:str) -> None:
        self.code = code
        self.title = title

class Capacity:
    def __init__(self, capacity:float, amount:float, unit:Unit):
        self.capacity = capacity #общая вместимость
        self.amount = amount #количество товара
        self.unit = unit

    def is_empty(self) -> bool:
        return self.amount <= 0

    def get_capacity(self)->float:
        return self.capacity

    def take(self, request_amount:float) -> float:
        if self.amount <= 0:
            return 0.0

        if self.amount < request_amount:
            request_amount = self.amount
            self.amount = 0
            return request_amount

        self.amount -= request_amount
        return request_amount

    def put(self, request_amount:float) -> float:

        self.amount += request_amount
        return request_amount

class Storage (Capacity):
    def __init__(self, address:str, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity=capacity, amount=amount, unit=unit)
        self.address = address

    def __str__(self) -> str:
        return f"The address this storage is {self.address}, capacity: {self.capacity}. Occupancy the storage: {(self.capacity-self.amount)}"

#здесь внёс изменения
class Shop(Capacity):
    def __init__(self, address:str, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity=capacity, amount=amount, unit=unit)
        self.address = address
        #self.capacity = capacity
        #self.amount = amount
        #self.unit = unit

    def __str__(self) -> str:
        return f"The address this shop is {self.address}, capacity: {self.capacity}. Occupancy the shop: {(self.capacity-self.amount)}"

class CarParking:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

class Truck (Capacity):

    def __init__(self, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity, amount, unit)
        pass

    def __str__(self) -> str:
        pass

    def put(self, request_amount:float):
        super().put(request_amount)

    def unload(self):
        super().amount = 0

    def run(self):
        pass

class Loader (Capacity):

    def __init__(self, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity, amount, unit)
        pass

    def __str__(self) -> str:
        pass

    def load(self, obj:Capacity, request_amount:float):
        obj.take(request_amount)

    def unload(self, obj:Capacity, request_amount:float):
        obj.capacity = 0

class Timer:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass