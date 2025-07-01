class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self) -> float:
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b == 0:
                raise ValueError("Division by zero is not allowed")
            return self.a / self.b
        else:
            raise ValueError("Invalid operation. Use: addition, subtraction, multiplication, division")

if __name__ == "__main__":
    try:
        calc = Calculator(10.5, 5.5, "addition")
        print(f"Result: {calc.calculate()}")  # Output: Result: 16.0
        calc = Calculator(10.5, 5.5, "division")
        print(f"Result: {calc.calculate()}")  # Output: Result: 1.9090909090909092
    except ValueError as e:
        print(f"Error: {e}")
