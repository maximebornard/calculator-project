"""

"""

class SimpleCalculator:
    
    def valide(self, value: object, name: str) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{name} doit être un int")
    
    def fsum(self, a: int, b: int) -> int:
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a + b)
    
    def substract(self, a: int, b: int) -> int:
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a - b)
    
    def multiply(self, a: int, b: int) -> int:
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a * b)
    
    def divide(self, a: int, b: int) -> int:
        self.valide(a, "a")
        self.valide(b, "b")
        return float(a / b)