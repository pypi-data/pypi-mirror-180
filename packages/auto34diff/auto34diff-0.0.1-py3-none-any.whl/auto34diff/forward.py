import numpy as np


def type_check(func):
    def wrapper(self, other):
        if isinstance(other, (int, float)):
            other = ForwardVar(other, 0.)
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
        return ForwardVar(self.real * other.real, self.real * other.dual + other.real * self.dual)

    @type_check
    def __truediv__(self, other):
        return self * other ** -1

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "power must be float or int"
        return ForwardVar(self.real ** other, other * self.real ** (other - 1) * self.dual)

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

    def sin(self):
        """
        Sine operator of the ForwardVar.

        Returns:
            ForwardVar: The sine of the ForwardVar.
        """
        return ForwardVar(np.sin(self.real), np.cos(self.real) * self.dual)

    def cos(self):
        """
        Cosine operator of the ForwardVar.

        Returns:
            ForwardVar: The cosine of the ForwardVar.
        """
        return ForwardVar(np.cos(self.real), -np.sin(self.real) * self.dual)

    def exp(self):
        """
        Exponential operator of the ForwardVar.

        Returns:
            ForwardVar: The exponential of the ForwardVar.
        """
        return ForwardVar(np.exp(self.real), np.exp(self.real) * self.dual)

    def log(self):
        """
        Log operator of the ForwardVar.

        Returns:
            ForwardVar: The log of the ForwardVar.
        """
        return ForwardVar(np.log(self.real), self.dual / self.real)

    def relu(self):
        """
        ReLU operator of the ForwardVar.

        Returns:
            ForwardVar: The ReLU of the ForwardVar.
        """
        return ForwardVar(self.real if self.real > 0 else 0., self.dual if self.real > 0 else 0.)

    def __str__(self):
        return f"real: {self.real}, dual: {self.dual}"
