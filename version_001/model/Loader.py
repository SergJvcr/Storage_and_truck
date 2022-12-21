from model.Actor import Actor
from model.ActorStatus import ActorStatus
from model.Capacity import Capacity
from model.Unit import Unit
from model.LoaderState import LoaderState

LOADER_READY: ActorStatus = ActorStatus("READY", "Готов", False, [])
LOADER_LOADING: ActorStatus = ActorStatus("LOADING", "Погрузка", True, [])
LOADER_UNLOADING: ActorStatus = ActorStatus("UNLOADING", "Разрузка", True, [])

class Loader(Capacity, Actor):
    def __init__(self, capacity: float, amount: float, unit: Unit, status: ActorStatus) -> None:
        Capacity.__init__(self, capacity, amount, unit)
        Actor.__init__(self, status)

    # Когда приезжает грузовик под погрузку, вызываем этот метод с указанием экземпляра грузовика,
    # при этом грузовик пристыковывается к погрузчику
    # Чтобы отстыковать грузовик, например при завершении погрузки или разгрузки, вызваем этот же метод с параметром None
    def setLinkCapacity(self, obj: Capacity):
        self.linkedCapacity = obj

    def unlinkCapacity(self):
        self.setLinkCapacity(None)

    def load(self, obj: Capacity, request_amount: float):
        obj.take(request_amount)

    def unload(self, obj: Capacity, request_amount: float) -> float:
        return obj.take(request_amount)

    def __str__(self) -> str:
        return f'Loader cap={super().get_capacity()} amount={super().get_amount()}'

    def set_state(self, st: ActorStatus, cap1: Capacity, cap2: Capacity):
        self.state = LoaderState(status=st, cap1=cap1, cap2=cap2)
        self.setStatus(st)

    def tick(self):

        if super().getStatus() in (LOADER_LOADING, LOADER_UNLOADING):
            m = min(self.get_avail_capacity(),
                    self.state.cap2.get_avail_capacity())
            m = min(m, self.state.cap1.get_avail_capacity())
            self.put(self.state.cap1.take(m))
            self.state.cap2.put(self.takeAll())

            if m > 0:
                return True
            else:
                self.setStatus(LOADER_READY)
                return False

        # elif super().getStatus()==LOADER_UNLOADING:
        #     self.unload(self.getLinkedCapacity())
