# calculator.py
from calculation import Calculation

class Calculator:
    history = []

    @staticmethod
    def add(x: float, y: float) -> Calculation:
        result = x + y
        calc = Calculation("+", x, y, result)
        Calculator.history.append(calc)
        return calc

    @staticmethod
    def subtract(x: float, y: float) -> Calculation:
        result = x - y
        calc = Calculation("-", x, y, result)
        Calculator.history.append(calc)
        return calc

    @staticmethod
    def multiply(x: float, y: float) -> Calculation:
        result = x * y
        calc = Calculation("*", x, y, result)
        Calculator.history.append(calc)
        return calc

    @staticmethod
    def divide(x: float, y: float) -> Calculation:
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        result = x / y
        calc = Calculation("/", x, y, result)
        Calculator.history.append(calc)
        return calc
    