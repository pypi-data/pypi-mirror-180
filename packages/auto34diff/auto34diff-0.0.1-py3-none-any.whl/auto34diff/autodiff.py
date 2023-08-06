import numpy as np
from .forward import ForwardVar


class AutoDiff:
    """
    This is a class for auto differentiation.

    Attributes:
        f (fucntion): The function that we try to autodifferentiate on.
        var (dict): A map of variables associated with their respective values.
        J (int): Jacobian matrix of the auto differentiation.
        value (int): Value of the auto differentiation.
    """

    def __init__(self, f, var):
        """
        The constructor for the AutoDiff class.

        Parameters:
            f (list(ForwardVar)): A list of ForwardVar that represents functions.
            var (list(ForwardVar)): A list of dual number variables
        """
        if not isinstance(f, list):
            raise TypeError(
                f"Type `{type(f)}` is not supported, expected list")
        if not all(isinstance(i, ForwardVar) for i in f):
            raise TypeError("f should be a list of ForwardVar")

        if not isinstance(var, list):
            raise TypeError(
                f"Type `{type(var)}` is not supported, expected list")
        if not all(isinstance(i, ForwardVar) for i in var):
            raise TypeError("var should be a list of ForwardVar")

        self.f = f
        self.var = var
        self.J = None
        self.value = 0  # Numerical result

    def calc_jacobian(self, P):
        """
        Calculate jacobian for the AutoDiff class.

        Parameters:
            P (list(int)): Directional derivatives.
        """
        if not isinstance(P, list):
            raise TypeError(
                f"Type `{type(P)}` is not supported, expected list")
        if not all(isinstance(i, int) for i in P):
            raise TypeError("P should be a list of int")

        assert len(P) == len(
            self.var), "The length of P should match the number of variables"

        # Get input functions number
        n = len(self.f)

        # Scalar jacobian (derivative) calculation
        if n == 1:
            self.J = self.f[0].dual
            self.value = self.J
            return

        # Construct the Jacobian matrix of the autodifferentiation
        self.J = np.vstack([self.f[i].dual for i in range(n)])

        # populate value
        self.value = self.J @ P
