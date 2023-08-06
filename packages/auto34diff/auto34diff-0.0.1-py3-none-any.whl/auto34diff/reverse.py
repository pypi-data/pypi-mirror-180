import numpy as np


def type_check(func):
    def wrapper(self, other):
        if isinstance(other, (int, float)):
            other = ReverseVar(other)
        elif not isinstance(other, ReverseVar):
            raise TypeError(f"Type `{type(other)}` is not supported")
        return func(self, other)
    return wrapper


class ReverseVar:
    """
    This is a class for backward mode auto differentiation.

    Attributes:
        real (int, float): Value of the ReverseVar.
        parent (list(tuple(ReverseVar, float))): A list of parent variables associated with their respective values.
        gradient (float): Gradient of the ReverseVar.
    """

    def __init__(self, real, parent=None):
        """
        The constructor for the ReverseVar class.

        Parameters:
            real (int, float): Value of the ReverseVar.
            parent (list(tuple(ReverseVar, float))): A list of parent variables associated with their respective values. Default: None
        """
        if not isinstance(real, (int, float)):
            raise TypeError(f"Type `{type(real)}` is not supported")

        self.real = real
        self.parent = parent
        self.gradient = 0.

    @type_check
    def __add__(self, other):
        return ReverseVar(self.real + other.real, [(self, 1.0), (other, 1.0)])

    @type_check
    def __sub__(self, other):
        return self.__add__(-other)

    @type_check
    def __mul__(self, other):
        return ReverseVar(self.real * other.real, [(self, other.real), (other, self.real)])

    @type_check
    def __truediv__(self, other):
        return self * other ** -1

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "power must be float or int"
        return ReverseVar(self.real ** other, [(self, other * self.real ** (other - 1))])

    def __neg__(self):
        return ReverseVar(-self.real, [(self, -1.0)])

    @type_check
    def __radd__(self, other):
        return self.__add__(other)

    @type_check
    def __rsub__(self, other):
        return -self.__add__(other)

    @type_check
    def __rmul__(self, other):
        return self.__mul__(other)

    def backward(self):
        """
        Reverse pass of the backward modeauto differentiation.
        """
        self.gradient = 1.
        self._backward()

    def _backward(self):
        if self.parent is None:
            return
        for parent, coef in self.parent:
            parent.gradient += self.gradient * coef
            parent._backward()

    def sin(self):
        """
        Sine operator of the ReverseVar.

        Returns:
            ReverseVar: The sine of the ReverseVar.
        """
        return ReverseVar(np.sin(self.real), [(self, np.cos(self.real))])

    def cos(self):
        """
        Cosine operator of the ReverseVar.

        Returns:
            ReverseVar: The cosine of the ReverseVar.
        """
        return ReverseVar(np.cos(self.real), [(self, -np.sin(self.real))])

    def exp(self):
        """
        Exponential operator of the ReverseVar.

        Returns:
            ReverseVar: The exponential of the ReverseVar.
        """
        return ReverseVar(np.exp(self.real), [(self, np.exp(self.real))])

    def log(self):
        """
        Log operator of the ReverseVar.

        Returns:
            ReverseVar: The log of the ReverseVar.
        """
        return ReverseVar(np.log(self.real), [(self, 1.0 / self.real)])

    def relu(self):
        """
        ReLU operator of the ReverseVar.

        Returns:
            ReverseVar: The ReLU of the ReverseVar.
        """
        return ReverseVar(self.real if self.real > 0 else 0., [(self, 1. if self.real > 0 else 0.)])

    def __str__(self):
        return f"real: {self.real}, gradient: {self.gradient}"
