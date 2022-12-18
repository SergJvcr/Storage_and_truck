from model.Actor import Actor
from model.ActorStatus import ActorStatus
from model.Capacity import Capacity
from model.Unit import Unit

LOADER_LOADING = ""
LOADER_UNLOADING = ""

class Loader(Capacity, Actor):
    def __init__(self, capacity:float, amount:float, unit:Unit, status:ActorStatus) -> None:
        Capacity.__init__(self, capacity, amount, unit)
        Actor.__init__(self, status)

    # Когда приезжает грузовик под погрузку, вызываем этот метод с указанием экземпляра грузовика,
    # при этом грузовик пристыковывается к погрузчику
    # Чтобы отстыковать грузовик, например при завершении погрузки или разгрузки, вызваем этот же метод с параметром None
    def setLinkCapacity(self, obj:Capacity):
        self.linkedCapacity = obj

    def unlinkCapacity(self):
        self.setLinkCapacity(None)

    def load(self, obj:Capacity, request_amount:float):
        obj.take(request_amount)

    def unload(self, obj:Capacity, request_amount:float)->float:
        return obj.take(request_amount)

    def __str__(self) -> str:
        return  f'Loader cap={super().get_capacity()} amount={super().get_amount()}'

    def tick(self):
        if super().getStatus()==LOADER_LOADING:
            self.load(self.getLinkedCapacity())

        elif super().getStatus()==LOADER_UNLOADING:
            self.unload(self.getLinkedCapacity())
