
class ActorStatus:
    def __init__(self, code:str, title:str, next:list[str]):
        self.code = code
        self.title = title
        self.next = next    

    def __str__(self) -> str:
        return f"ActorStatus {self.code} {self.title}"











