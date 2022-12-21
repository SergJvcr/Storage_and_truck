from model.Unit import Unit

class Capacity:
    def __init__(self, capacity: float, amount: float, unit: Unit):
        self.capacity = capacity  # общая вместимость
        self.amount = amount  # количество товара
        self.unit = unit

    def __str__(self):
        return f'capacity={self.capacity} amount={self.amount}'

    def is_empty(self) -> bool:
        return self.amount <= 0

    def get_capacity(self) -> float:
        return self.capacity

    def get_amount(self) -> float:
        return self.amount

    def get_avail_capacity(self) -> float:
        return self.capacity - self.amount

    # Try to unload requested amount of cargo from capacity
    def take(self, request_amount: float) -> float:
        if self.amount <= 0:
            return 0.0

        if self.amount < request_amount:
            request_amount = self.amount
            self.amount = 0.0
            return request_amount

        self.amount -= request_amount
        return request_amount

    def takeAll(self)->float:
        return self.take(self.amount)

    # Try to put requested amount of cargo into capacity
    def put(self, request_amount: float) -> float:
        avail_capacity = self.get_avail_capacity()
        if avail_capacity <= 0:
            return 0.0

        if avail_capacity < request_amount:
            request_amount = avail_capacity
            self.amount = self.capacity
            return avail_capacity

        self.amount += request_amount
        return request_amount
