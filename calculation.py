class Calculation:
    def __init__(self, operation: str, x: float, y: float, result: float):
        self.operation = operation
        self.x = x
        self.y = y
        self.result = result

    def __repr__(self):
        return f"{self.x} {self.operation} {self.y} = {self.result}"