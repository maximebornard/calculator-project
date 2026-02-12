"""calculator.simple_calculator

This module defines the :class:`SimpleCalculator` class.

It provides basic arithmetic operations with strict input validation:
all parameters must be integers. The methods return integers except
:method:`divide`, which always returns a float.

Author: Maxime Bornard
"""

class SimpleCalculator:
    """A simple calculator implementing basic arithmetic operations.

    Rules:
        - Inputs must be integers.
        - fsum, substract and multiply return integers.
        - divide returns a float and raises ZeroDivisionError if b == 0.
    """
    
    def valide(self, value: object, name: str) -> None:
        """Validate that the given value is an integer.

        Args:
            value: The value to validate.
            name: The parameter name (used in the error message).

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} doit être un int")
    
    def fsum(self, a: int, b: int) -> int:
        """Add two integers.

        Args:
            a: First integer.
            b: Second integer.

        Returns:
            The sum of a and b.

        Raises:
            TypeError: If a or b is not an integer.
        """
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a + b)
    
    def substract(self, a: int, b: int) -> int:
        """Subtract b from a.

        Args:
            a: First integer.
            b: Second integer.

        Returns:
            The result of a - b.

        Raises:
            TypeError: If a or b is not an integer.
        """
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a - b)
    
    def multiply(self, a: int, b: int) -> int:
        """Multiply two integers.

        Args:
            a: First integer.
            b: Second integer.

        Returns:
            The product a * b.

        Raises:
            TypeError: If a or b is not an integer.
        """
        self.valide(a, "a")
        self.valide(b, "b")
        return int(a * b)
    
    def divide(self, a: int, b: int) -> float:
        """Divide a by b.

        Args:
            a: Numerator (integer).
            b: Denominator (integer).

        Returns:
            The result of a / b as a float.

        Raises:
            TypeError: If a or b is not an integer.
            ZeroDivisionError: If b is 0.
        """
        self.valide(a, "a")
        self.valide(b, "b")
        return float(a / b)