import numpy as np
from auto34diff.forward import ForwardVar
from auto34diff.reverse import ReverseVar


def exp(x):
    """
    Exponential operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Exponent.
    """

    if isinstance(x, (int, float)):
        return np.exp(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.exp(x.real), np.exp(x.real) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.exp(x.real), [(x, np.exp(x.real))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def log(x, base=np.e):
    """
    Logarithm operator.

    With one argument, return the natural logarithm of x (to base e).

    With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Inpute variable.

        base (int/float): Base value.
    """

    if isinstance(x, (int, float)):
        if np.isclose(base, np.e):  # natural base
            return np.log(x)
        else:
            return np.log(x) / log(base)
    elif isinstance(x, ForwardVar):
        if isinstance(base, (int, float)):  # log_{number}(ForwardVar)
            return ForwardVar(np.log(x.real) / np.log(base), x.dual / (x.real*np.log(base)))
        elif isinstance(base, ForwardVar):  # log_{ForwardVar}(ForwardVar)
            return log(x) / log(base)
        # else: log_{not support}(ForwardVar)
    elif isinstance(x, ReverseVar):
        if isinstance(base, (int, float)):  # log_{number}(ReverseVar)
            return ReverseVar(np.log(x.real) / np.log(base), [(x, 1.0 / (x.real*np.log(base)))])
        elif isinstance(base, ReverseVar):  # log_{ReverseVar}(ReverseVar)
            return ReverseVar(
                np.log(x.real) / np.log(base.real),
                [
                    (x, 1.0 / (x.real*np.log(base.real))),
                    (base, -np.log(x.real)*np.log(base.real)**(-2)/base.real)
                ]
            )
        # else: log_{not support}(ReverseVar)
    raise TypeError(
        f"Type `{type(x)}` and base type `{type(base)}` not supported")


def sin(x):
    """
    Trigonometric sine operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Angle, in radians (2π rad equals 360 degrees).
    """

    if isinstance(x, (int, float)):
        return np.sin(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.sin(x.real), np.cos(x.real) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.sin(x.real), [(x, np.cos(x.real))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def cos(x):
    """
    Trigonometric cosine operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Angle, in radians.
    """
    if isinstance(x, (int, float)):
        return np.cos(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.cos(x.real), -np.sin(x.real) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.cos(x.real), [(x, -np.sin(x.real))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def tan(x):
    """
    Trigonometric tangent operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Angle, in radians.
    """
    if isinstance(x, (int, float)):
        return np.tan(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.tan(x.real), 1/(np.cos(x.real)**2) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.tan(x.real), [(x, 1/(np.cos(x.real)**2))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def arcsin(x):
    """
    Trigonometric inverse sine operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): y-coordinate on the unit circle.
    """
    if isinstance(x, (int, float)):
        if abs(x) > 1:
            raise ValueError("y-coordinate outside the unit circle")
        return np.arcsin(x)
    elif not isinstance(x, (ForwardVar, ReverseVar)):
        raise TypeError(f"Type `{type(x)}` is not supported")

    if abs(x.real) > 1:
        raise ValueError("y-coordinate outside the unit circle")

    if isinstance(x, ForwardVar):
        return ForwardVar(np.arcsin(x.real), 1/np.sqrt(1-x.real**2) * x.dual)
    else:
        return ReverseVar(np.arcsin(x.real), [(x, 1/np.sqrt(1-x.real**2))])


def arccos(x):
    """
    Trigonometric inverse cosine operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): x-coordinate on the unit circle.
    """

    if isinstance(x, (int, float)):
        if abs(x) > 1:
            raise ValueError("x-coordinate outside the unit circle")
        return np.arccos(x)
    elif not isinstance(x, (ForwardVar, ReverseVar)):
        raise TypeError(f"Type `{type(x)}` is not supported")

    if abs(x.real) > 1:
        raise ValueError("x-coordinate outside the unit circle")

    if isinstance(x, ForwardVar):
        return ForwardVar(np.arccos(x.real), -1/np.sqrt(1-x.real**2) * x.dual)
    else:
        return ReverseVar(np.arccos(x.real), [(x, -1/np.sqrt(1-x.real**2))])


def arctan(x):
    """
    Trigonometric inverse tangent operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Inpute variable.
    """

    if isinstance(x, (int, float)):
        return np.arctan(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.arctan(x.real), 1/(1+x.real**2) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.arctan(x.real), [(x, 1/(1+x.real**2))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def sinh(x):
    """
    Hyperbolic sine operator.

    Equivalent to 1/2 * (np.exp(x) - np.exp(-x)).

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Input variable.
    """

    if isinstance(x, (int, float)):
        return np.sinh(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.sinh(x.real), np.cosh(x.real) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.sinh(x.real), [(x, np.cosh(x.real))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def cosh(x):
    """
    Hyperbolic cosine operator.

    Equivalent to 1/2 * (np.exp(x) + np.exp(-x)).

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Input variable.
    """

    if isinstance(x, (int, float)):
        return np.cosh(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.cosh(x.real), np.sinh(x.real) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.cosh(x.real), [(x, np.sinh(x.real))])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def tanh(x):
    """
    Hyperbolic tangent operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Input variable.
    """

    if isinstance(x, (int, float)):
        return np.tanh(x)
    elif isinstance(x, ForwardVar):
        return ForwardVar(np.tanh(x.real), (1-np.tanh(x.real)**2) * x.dual)
    elif isinstance(x, ReverseVar):
        return ReverseVar(np.tanh(x.real), [(x, 1-np.tanh(x.real)**2)])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")


def sqrt(x):
    """
    Non-negative square-root operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Inpute variable.

        base (int/float): Base value.
    """
    if isinstance(x, (int, float)):
        if x < 0:
            raise ValueError("Invalid value encountered in sqrt")
        return np.sqrt(x)
    elif not isinstance(x, (ForwardVar, ReverseVar)):
        raise TypeError(f"Type `{type(x)}` is not supported")

    if x.real < 0:
        raise ValueError("Invalid value encountered in sqrt")

    if isinstance(x, ForwardVar):
        return ForwardVar(np.sqrt(x.real), .5/np.sqrt(x.real) * x.dual)
    else:
        return ReverseVar(np.sqrt(x.real), [(x, .5/np.sqrt(x.real))])


def logistic(x):
    """
    Standard logistic  operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Input variable.
    """

    if isinstance(x, (int, float)):
        return .5 + .5 * np.tanh(x/2)
    elif not isinstance(x, (ForwardVar, ReverseVar)):
        raise TypeError(f"Type `{type(x)}` is not supported")

    exp_x = np.exp(x.real)
    if isinstance(x, ForwardVar):
        return ForwardVar(.5 + .5*np.tanh(x.real/2), exp_x/(1+exp_x)**2 * x.dual)
    else:
        return ReverseVar(.5 + .5*np.tanh(x.real/2), [(x, exp_x/(1+exp_x)**2)])


def relu(x):
    """
    Rectified Linear Unit operator.

    Parameters:
        x (int/float/ForwardVar/ReverseVar): Input variable.
    """

    if isinstance(x, (int, float)):
        return (x > 0) * x
    elif isinstance(x, ForwardVar):
        return ForwardVar(x.real if x.real > 0 else 0., x.dual if x.real > 0 else 0.)
    elif isinstance(x, ReverseVar):
        return ReverseVar(x.real if x.real > 0 else 0., [(x, 1. if x.real > 0 else 0.)])
    else:
        raise TypeError(f"Type `{type(x)}` is not supported")
