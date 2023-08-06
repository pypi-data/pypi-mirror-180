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
        self.gradient = 0.0

    @type_check
    def __add__(self, other):
        return ReverseVar(self.real + other.real, [(self, 1.0), (other, 1.0)])

    @type_check
    def __sub__(self, other):
        return self.__add__(-other)

    @type_check
    def __mul__(self, other):
        return ReverseVar(
            self.real * other.real, [(self, other.real), (other, self.real)]
        )

    @type_check
    def __truediv__(self, other):
        return self * other**-1

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return ReverseVar(
                self.real**other, [(self, other * self.real ** (other - 1))]
            )
        elif isinstance(other, ReverseVar):
            return ReverseVar(
                self.real**other.real,
                [(self, other.real * (self.real ** (other.real - 1))),
                 (other, np.log(self.real) * self.real ** other.real)],
            )
        else:
            raise TypeError(f"Type `{type(other)}` is not supported")

    def __neg__(self):
        return ReverseVar(-self.real, [(self, -1.0)])

    @type_check
    def __radd__(self, other):
        return self.__add__(other)

    @type_check
    def __rsub__(self, other):
        return (-self).__add__(other)

    @type_check
    def __rmul__(self, other):
        return self.__mul__(other)

    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            return ReverseVar(
                other**self.real, [(self, other**self.real * np.log(other))]
            )
        else:
            raise TypeError(f"Type `{type(other)}` is not supported")

    def backward(self):
        """
        Reverse pass of the backward modeauto differentiation.
        """
        self.gradient = 1.0
        self._backward()

    def _backward(self):
        if self.parent is None:
            return
        for parent, coef in self.parent:
            parent.gradient += self.gradient * coef
            parent._backward()

    def __str__(self):
        return f"real: {self.real}, gradient: {self.gradient}"
