import numpy as np


def type_check(func):
    def wrapper(self, other):
        if isinstance(other, (int, float)):
            other = ForwardVar(other, 0.0)
        elif not isinstance(other, ForwardVar):
            raise TypeError(f"Type `{type(other)}` is not supported")
        return func(self, other)

    return wrapper


class ForwardVar:
    """
    This is a class for forward mode auto differentiation.

    Attributes:
        real (int, float): Real part of the ForwardVar.
        dual (int, float, optional): Dual part of the ForwardVar.
    """

    def __init__(self, real, dual=1.0):
        """
        The constructor for the ForwardVar class.

        Parameters:
            real (int, float): Real part of the ForwardVar.
            dual (int, float, optional): Dual part of the ForwardVar. Default: 1.0
        """
        if not isinstance(real, (int, float)):
            raise TypeError(f"Type `{type(real)}` is not supported")
        if not isinstance(dual, (int, float, np.ndarray)):
            raise TypeError(f"Type `{type(dual)}` is not supported")
        self.real = real
        self.dual = dual

    @type_check
    def __add__(self, other):
        return ForwardVar(self.real + other.real, self.dual + other.dual)

    @type_check
    def __sub__(self, other):
        return self.__add__(-other)

    @type_check
    def __mul__(self, other):
        return ForwardVar(
            self.real * other.real, self.real * other.dual + other.real * self.dual
        )

    @type_check
    def __truediv__(self, other):
        return self * other**-1

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return ForwardVar(
                self.real**other, other * self.real ** (other - 1) * self.dual
            )
        elif isinstance(other, ForwardVar):
            a, b = self.real, self.dual
            c, d = other.real, other.dual
            return ForwardVar(a**c, a**c * (d * np.log(a) + b * c / a))
        else:
            raise TypeError(f"Type `{type(other)}` is not supported")

    def __neg__(self):
        return ForwardVar(-self.real, -self.dual)

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
            return ForwardVar(
                other**self.real, other**self.real * np.log(other) * self.dual
            )
        else:
            raise TypeError(f"Type `{type(other)}` is not supported")

    def __str__(self):
        return f"real: {self.real}, dual: {self.dual}"
