from model.ActorStatus import ActorStatus

class Actor:
    def __init__(self, status: ActorStatus):
        self.status = status

    def tick(self) -> bool:
        return False

    def getStatus(self)->ActorStatus:
        return self.status

    def onStatusChanged(self, oldSt:ActorStatus, newStatus:ActorStatus):
        pass

    def setStatus(self, newStatus:ActorStatus):
        st1 = self.status.code
        st2 = newStatus.code
        if st1!=st2:
            oldSt = self.status
            self.status = newStatus
            self.onStatusChanged(oldSt, newStatus)


    def __str__(self) -> str:
        return f"Actor {self.getStatus()}"