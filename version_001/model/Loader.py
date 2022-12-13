from Actor import Actor
from Capacity import Capacity
from Unit import Unit

LOADER_LOADING = ""
LOADER_UNLOADING = ""

class Loader2(Capacity, Actor):
    def __init__(self):
        pass

    # Когда приезжает грузовик под погрузку, вызываем этот метод с указанием экземпляра грузовика,
    # при этом грузовик пристыковывается к погрузчику
    # Чтобы отстыковать грузовик, например при завершении погрузки или разгрузки, вызваем этот же метод с параметром None
    def setLinkCapacity(self, obj:Capacity):
        self.linkedCapacity = obj

    def unlinkCapacity(self):
        self.setLinkCapacity(None)

    def load(self, obj:Capacity):
        pass

    def unload(self, obj:Capacity):
        pass


    def tick(self):
        if super().getStatus()==LOADER_LOADING:
            self.load(self.getLinkedCapacity())

        elif super().getStatus()==LOADER_UNLOADING:
            self.unload(self.getLinkedCapacity())


ld: Loader2 = Loader2()

class Loader (Capacity):

    def __init__(self, capacity:float, amount:float, unit:Unit) -> None:
        super().__init__(capacity, amount, unit)

    def __str__(self) -> str:
        pass

    def load(self, obj:Capacity, request_amount:float):
        obj.take(request_amount)

    def unload(self, obj:Capacity, request_amount:float)->float:
        return obj.take(request_amount)