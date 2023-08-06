import operator as op
import numpy as np


class Expr:
    """
    This is a class for expression.

    Attributes:
        d (dict): Dictionary of opreations.
        left: Left part of the expression.
        right: Right part of the expression.
        operator (fucntion): Operation of the expression.
    """
    d = {op.add: "+", op.sub: "-", op.mul: "*",
         op.pow: "^", np.sin: "sin", np.cos: "cos"}

    @classmethod
    def sin(cls, x):
        return cls(x, None, np.sin)

    @classmethod
    def cos(cls, x):
        return cls(x, None, np.cos)

    def __init__(self, left, right, operator):
        """
        The constructor for the Expr class.

        Parameters:
            d (dict): Dictionary of opreations.
            left: Left part of the expression.
            right: Right part of the expression.
            operator (fucntion): Operation of the expression.
        """
        self.left = left
        self.right = right
        self.operator = operator

    def __add__(self, other):
        return Expr(self, other, op.add)

    def __sub__(self, other):
        return Expr(self, other, op.sub)

    def __mul__(self, other):
        return Expr(self, other, op.mul)

    def __pow__(self, other):
        return Expr(self, other, op.pow)

    def __radd__(self, other):
        return Expr(other, self, op.add)

    def __rmul__(self, other):
        return Expr(other, self, op.mul)

    def __rsub__(self, other):
        return Expr(other, self, op.sub)

    def __repr__(self):
        left = self.left
        res = ""
        if self.operator in (np.sin, np.cos):
            if isinstance(left, Symbol):
                res = f"{self.d[self.operator]}({left.letter})"
            else:
                res = f"{self.d[self.operator]}({left})"
            return res
        res += "("
        if isinstance(left, Symbol):
            res += left.letter
        else:
            res += str(left)
        res += f" {self.d[self.operator]} "
        right = self.right
        if isinstance(right, Symbol):
            res += right.letter
        else:
            res += str(right)
        res += ")"
        return res


class Symbol:

    def __init__(self, letter):
        self.letter = letter

    def __add__(self, other):
        return Expr(self, other, op.add)

    def __sub__(self, other):
        return Expr(self, other, op.sub)

    def __mul__(self, other):
        return Expr(self, other, op.mul)

    def __pow__(self, other):
        return Expr(self, other, op.pow)

    def __radd__(self, other):
        return Expr(other, self, op.add)

    def __rmul__(self, other):
        return Expr(other, self, op.mul)

    def __rsub__(self, other):
        return Expr(other, self, op.sub)
