
from model.ActorStatus import ActorStatus
from model.Capacity import Capacity

class LoaderState:
    def __init__(self, status:ActorStatus, cap1:Capacity, cap2:Capacity):
        self.status = status
        self.cap1 = cap1
        self.cap2 = cap2



