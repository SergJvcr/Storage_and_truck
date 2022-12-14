class Unit:
    def __init__(self, code:str, title:str) -> None:
        self.code = code
        self.title = title

    def __str__(self) -> str:
        return f"Unit {self.code} {self.title}"


