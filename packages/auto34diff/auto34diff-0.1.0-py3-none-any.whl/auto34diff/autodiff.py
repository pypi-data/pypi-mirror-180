from auto34diff.functions import *
import numpy as np


class AutoDiff:
    """
    This is a class for auto differentiation.

    Attributes:
        var (list(ForwardVar|ReverseVar)): A list of variables used in the autodifferentiation process. It
            can be either a list of ForwardVar or a list of ReverseVar depending on the mode that the user
            chooses.
        J (int): Jacobian matrix of the auto differentiation.
        mode (str): The mode of autodifferentiation that the user specifies.
    """

    def __init__(self, vals, mode="forward"):
        """
        The constructor for the AutoDiff class.

        Parameters:
            vals (array-like(int|float)): A list of variable values initialized.
            mode (str): The mode of autodifferentiation that the user specifies. The options are "forward"
                and "reverse" and the default option is "forward".
        """

        self.J = None

        mode = mode.lower()
        assert mode in (
            "forward",
            "reverse",
        ), "Mode should be either forward or reverse."
        self.mode = mode

        if isinstance(vals, list):
            assert all(
                isinstance(val, (int, float)) for val in vals
            ), "vals should be a list of numbers."
        elif isinstance(vals, (int, float)):
            vals = [vals]
        else:
            raise TypeError("vals should be a list of numbers or a number.")

        if self.mode == "reverse":
            self.var = [ReverseVar(val) for val in vals]
        else:
            self.var, num_params = [], len(vals)
            for i, val in enumerate(vals):
                dual_part = np.zeros(num_params)
                dual_part[i] = 1
                self.var.append(ForwardVar(val, dual_part))

    def get_params(self):
        if len(self.var) == 1:
            return self.var[0]
        return self.var

    def update_func(self, f):
        if isinstance(f, list):
            self.f = f
        elif isinstance(f, (ReverseVar, ForwardVar)):
            self.f = [f]
        else:
            raise TypeError(
                "f should be a list of ReverseVar or ForwardVar or a ReverseVar or a ForwardVar.")

    def calc(self):
        if self.mode == "forward":
            if len(self.f) == 1:
                self.J = self.f[0].dual
            else:
                self.J = np.vstack(
                    [self.f[i].dual for i in range(len(self.f))])
        elif self.mode == "reverse":
            res = []
            for f in self.f:
                for x in self.var:
                    x.gradient = 0.
                f.backward()
                res.append([x.gradient for x in self.var])
            self.J = np.array(res)

    def get(self, x=None):
        P = [1 if id(v) == id(x) else 0 for v in self.var] if x else None
        if self.mode == "forward":
            if P is None:
                return self.J
            return self.J @ P
        elif self.mode == "reverse":
            if P is None:
                return self.J
            return self.J @ P
