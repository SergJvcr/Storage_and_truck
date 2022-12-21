
class ActorStatus:
    def __init__(self, code:str, title:str, busy:bool, next:list[str]):
        self.code = code
        self.title = title
        self.next = next    
        self.busy = busy

    def __str__(self) -> str:
        return f"ActorStatus {self.code} {self.title}"

    def __eq__(self, __o: object) -> bool:
        print("ActorStatus.__eq(x) implicitly called")
        return self.code == __o.code










