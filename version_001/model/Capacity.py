from Unit import Unit
class Capacity:
    def __init__(self, capacity:float, amount:float, unit:Unit):
        self.CAPACITY = capacity #общая вместимость
        self.amount = amount #количество товара
        self.unit = unit

    def is_empty(self) -> bool:
        return self.amount <= 0

    def get_capacity(self)->float:
        return self.CAPACITY
    def get_amount(self)->float:
        return self.amount

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