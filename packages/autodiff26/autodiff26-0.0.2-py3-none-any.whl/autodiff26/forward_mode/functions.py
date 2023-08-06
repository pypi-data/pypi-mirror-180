r"""Implements Function class object function methods"""

#!/usr/bin/env python3
# File       : functions.py
# Description: Define functions and override operators
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np
_supported_types = (int, float, np.int32, np.int64)
_base = np.exp(1)

class FunctionClass:
    """Function class for overrriding numeric operations in dual number operations"""

    def __init__(self, val, der=1.0):
        """Initialize FunctionClass objects"""

        self.val = val
        self.der = der


    def __add__(self, other):
        """Function that implements addition

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: w + w
        >>> a = FunctionClass(5.0)
        >>> ans = g(a)
        >>> print(ans.val)
        10.0
        >>> print(ans.der)
        2.0

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """

        if isinstance(other, FunctionClass):
            return FunctionClass(self.val + other.val, self.der + other.der)
        elif isinstance(other, _supported_types):
            return FunctionClass(self.val + other, self.der)
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for addition")


    def __sub__(self, other):
        """Function that implements subtraction

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: w - 2.0
        >>> a = FunctionClass(5.0)
        >>> ans = g(a)
        >>> print(ans.val)
        3.0
        >>> print(ans.der)
        1.0

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """

        if isinstance(other, FunctionClass):
            return FunctionClass(self.val - other.val, self.der - other.der)
        elif isinstance(other, _supported_types):
            return FunctionClass(self.val - other, self.der)
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for subtraction")


    def __mul__(self, other):
        """Function that implements multiplication rules for primal and tangent trace

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: 2*w *w*w*w
        >>> a = FunctionClass(2.0)
        >>> ans = g(a)
        >>> print(ans.val)
        32.0
        >>> print(ans.der)
        64.0

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """
        if isinstance(other, FunctionClass):
            dual_part = self.val * other.der
            dual_part += other.val * self.der
            real_part = self.val * other.val
            return FunctionClass(real_part, dual_part)

        # not int/scalar
        elif not isinstance(other, _supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for multiplication"
            )
        else:
            return FunctionClass(self.val*other, other*self.der)


    def __str__(self):
        """Formatted output of obj val"""

        return f"Value: {self.val}, Derivative: {self.der}"


    def __rmul__(self, other):
        """Implements reflected multiplication by call __mul__"""

        return self.__mul__(other)


    def __radd__(self, other):
        """Implements reflected addition by call __add__"""
        return self.__add__(other)


    def __rsub__(self, other):
        """Implements reflected subtraction"""
        if isinstance(other, _supported_types):
            return FunctionClass(other - self.val, -self.der)
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for subtraction")


    def __truediv__(self, other):
        """Function that implements true division

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda v, w : v / w
        >>> a = FunctionClass(5.0)
        >>> b = FunctionClass(2.0)
        >>> ans = g(a, b)
        >>> print(ans.val)
        2.5
        >>> print(ans.der)
        -0.75

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object
        ZeroDivisionError
            If denominator is 0
        """

        if isinstance(other, FunctionClass):
            numerator = self * FunctionClass(other.val, -other.der)
            denominator = other.val**2
            if denominator == 0:
                raise ZeroDivisionError("You cannot divide by 0")
            return FunctionClass(numerator.val/denominator, numerator.der/denominator)
        elif isinstance(other, _supported_types):
            if other == 0:
                raise ZeroDivisionError("You cannot divide by 0")
            return FunctionClass(self.val/other, self.der/other)
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for division")


    def __rtruediv__(self, other):
        """Implements reflected true division"""
        if self.val == 0:
            raise ZeroDivisionError("You cannot divide by 0")
        if isinstance(other, _supported_types):
            other_class = FunctionClass(other, 0)
            return other_class / self
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for division")


    def __abs__(self):
        """Function that implements absolute operation
        Parameters
        ----------
        x: FunctionClass, int, float
            input to evaluate value and derivative
        Examples
        --------
        >>> g = lambda w: abs(w)
        >>> a = FunctionClass(2.0)
        >>> ans = g(a)
        >>> print(ans.val)
        2.0
        >>> print(ans.der)
        1.0

        Returns
        -------
        FunctionClass
                Returns updated function object with value and derivative
        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object
        Value Error
            Derivative of absolute at 0

        """
        if isinstance(self, FunctionClass):
            if self.val == 0:
                raise ValueError("Derivative of absolute undefined at 0")
            self.der = self.der * (self.val/abs(self.val))
            if self.val < 0:
                self.val = abs(self.val)
            return FunctionClass(self.val, self.der)
        elif not isinstance(self, _supported_types):
            raise TypeError(
                f"Type `{type(FunctionClass)}` is not supported for absolute"
            )


    def __pow__(self, other):
        """Function that implements power

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: w**2
        >>> w = FunctionClass(1.0)
        >>> ans = g(w)
        >>> print(ans.val)
        1.0
        >>> print(ans.der)
        2.0

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object
        ValueError
            if trying to take log of 0
        """
        if isinstance(other, _supported_types):
            if self.val == 0 and other <= 0:
                raise ValueError("Cannot be raised to negative power")
            val = self.val**other
            der = other*(self.val**(other-1))*self.der
            return FunctionClass(val, der)

        else:
            raise TypeError(f"Type `{type(other)}` is not supported for power operations")


    def __rpow__(self, other):
        """Function that implements reflected power

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: 2**w
        >>> w = FunctionClass(2.0)
        >>> ans = g(w)
        >>> print(ans.val)
        4.0
        >>> print(ans.der)
        2.772588722239781

        Returns
        -------
        FunctionClass
                    Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object
        Value Error
            if base is less than or equal to 0
        """
        if isinstance(other, _supported_types):
            if other <= 0:
                raise ValueError(f"Cannot take log of {other}")
            
            der = (other**self.val) * np.log(other) * self.der
            return FunctionClass(other**self.val, der)
            
        else:
            raise TypeError(
                f"Type `{type(other)}` is not supported for operation"
            ) 


    def __neg__(self):
        """Function that implements the negation of the input

        Parameters
        ----------
        x: FunctionClass, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: -w * -12
        >>> a = FunctionClass(1.0)
        >>> ans = g(a)
        >>> print(ans.val)
        12.0
        >>> print(ans.der)
        12.0

        Returns
        -------
        FunctionClass
                Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """
        if isinstance(self, FunctionClass):
            self.val = self.val * -1
            self.der = self.der * -1
            return FunctionClass(self.val, self.der)
        elif not isinstance(self, _supported_types):
            raise TypeError(
                f"Type `{type(FunctionClass)}` is not supported for negation"
            ) 


def sin(x):
    """Function that implements sin rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: sin(w)
    >>> a = FunctionClass(0.0)
    >>> ans = g(a)
    >>> print(ans.val)
    0.0
    >>> print(ans.der)
    1.0

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object

    """

    if isinstance(x, FunctionClass):
        return FunctionClass(np.sin(x.val),np.cos(x.val)*x.der)

    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for sin operation"
            )
    else:
        return FunctionClass(np.sin(x), 0.0)


def arcsin(x):
    """Function that implements the arcsin rules forprimal and tanget trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Note
    -------
    The derivative of arcsin(x) is only defined between (-1,1)

    Examples
    --------
    >>> g = lambda w: arcsin(w)
    >>> a = FunctionClass(0.1)
    >>> ans = g(a)
    >>> print(ans.val)
    0.1001674211615598
    >>> print(ans.der)
    1.005037815259212

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object
    Value Error
        If input is less than -1 or greater than 1
    
    """
    if isinstance(x, FunctionClass):
        if abs(x.val) >= 1:
            raise ValueError(f"Derivative of arcsin(x) undefined at x = {x.val}")
        return FunctionClass(np.arcsin(x.val), x.der/pow((1-x.val**2), 0.5))

    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for arcsin operation"
            )
    else:
        if abs(x) >= 1:
            raise ValueError(f"Derivative of arcsin(x) undefined at x = {x}")
        return FunctionClass(np.arcsin(x), 0.0)


def arccos(x):
    """Function that implements the arccos rules for primal and tangent trace
    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative
    Note
    -------
    The derivative of arccos(x) is only defined between (-1,1)
    Examples
    --------
    >>> g = lambda w: arccos(w)
    >>> a = FunctionClass(0.1)
    >>> ans = g(a)
    >>> print(ans.val)
    1.4706289056333368
    >>> print(ans.der)
    - 1.005037815259212

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative
                
    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object
    Value Error
        If input is less than -1 or greater than 1
    
    """
    if isinstance(x, FunctionClass):
        if abs(x.val) >= 1:
            raise ValueError(f"Derivative of arccos(x) undefined at x = {x.val}")
        return FunctionClass(np.arccos(x.val), -x.der/pow((1-x.val**2), 0.5))

    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for arccos operation"
            )
    else:
        if abs(x) >= 1:
            raise ValueError(f"Derivative of arccos(x) undefined at x = {x}")
        return FunctionClass(np.arccos(x), 0.0)


def arctan(x):
    """Function that implements the arctan rules for primal and tangent trace
    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative
    Note
    -------
    The derivative of arctan(x) is only defined between (-1,1)
    Examples
    --------
    >>> g = lambda w: arctan(w)
    >>> a = FunctionClass(0.1)
    >>> ans = g(a)
    >>> print(ans.val)
    0.09966865249116204
    >>> print(ans.der)
    0.9900990099

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object
    Value Error
        If input is less than -1 or greater than 1
    
    """
    if isinstance(x, FunctionClass):
        return FunctionClass(np.arctan(x.val), x.der / (1 + x.val**2))

    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for arccos operation"
            )
    else:
        return FunctionClass(np.arctan(x), 0.0)


def cos(x):
    """Function that implements cos rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: cos(w)
    >>> a = FunctionClass(1.0)
    >>> ans = g(a)
    >>> print(ans.val)
    0.5403023058681398
    >>> print(ans.der)
    -0.8414709848078965

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object

    """

    if isinstance (x, FunctionClass):
        return FunctionClass(np.cos(x.val), -np.sin(x.val)*x.der)
    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for cos operation"
            )
    else:
        return FunctionClass(np.cos(x), 0.0)


def tan(x):
    """Function that implements tan rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: tan(w)
    >>> a = FunctionClass(0)
    >>> ans = g(a)
    >>> print(ans.val)
    0.0
    >>> print(ans.der)
    1.0

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object

    """

    if isinstance(x, FunctionClass):
        return FunctionClass(np.tan(x.val), (1/(pow(np.cos(x.val), 2))) * x.der)
    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for tan operation"
            )
    else:
        return FunctionClass(np.tan(x), 0.0)


def exp(x):
    """Function that implements exp rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: exp(w)
    >>> a = FunctionClass(0)
    >>> ans = g(a)
    >>> print(ans.val)
    1.0
    >>> print(ans.der)
    1.0

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object

    """
    if isinstance(x, FunctionClass):
        return FunctionClass(np.exp(x.val), (np.exp(x.val))*x.der)
    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for exp operation"
            )
    else:
        return FunctionClass(np.exp(x), 0.0)


def log(x, base=_base):
    """Function that implements log rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: log(w)
    >>> a = FunctionClass(1)
    >>> ans = g(a)
    >>> print(ans.val)
    0.0
    >>> print(ans.der)
    1.0

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object
    ValueError
        If trying to take the log of non positive number

    """
    if isinstance(x, FunctionClass):
        if x.val <= 0 or base == 1:
            raise ValueError("Cannot take log of non-positive values")
        return FunctionClass(np.log(x.val) / np.log(base), 
                             x.der / (x.val * np.log(base)))

    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for logarithm operation"
            )

    else:
        if x <= 0 or base == 1:
            raise ValueError("Cannot take the logarithm of non-positive values")
        return FunctionClass(np.log(x) / np.log(base), 0.0)


def sqrt(x):
    """Function that implements squareroot for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    ------
    >>> g = lambda w: sqrt(w)
    >>> a = FunctionClass(4)
    >>> ans = g(a)
    >>> print(ans.val)
    2.0
    >>> print(ans.der)
    0.25

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object
    Value Error
        If input is less than 0
    
    """
    if isinstance(x, FunctionClass):
        
        if x.val <= 0:
            raise ValueError(f"Squareroot of x is undefined for x.val < 0")
        return x ** 0.5
    elif not isinstance(x, _supported_types):
        raise TypeError(
                f"Type `{type(x)}` is not supported for squareroot operation"
            )

    else:
        if x < 0:
            raise ValueError(f"Squareroot of x is undefined for x < 0")
        return FunctionClass(np.sqrt(x), 0.0)


def logistic(x):
    """Function that implements logistic rules for primal and tangent trace

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: logistic(w)
    >>> a = FunctionClass(1)
    >>> ans = g(a)
    >>> print(ans.val)
    0.7310585786300049
    >>> print(ans.der)
    0.19661193324148188

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a FunctionClass, int, float Object

    """
    
    if isinstance(x, _supported_types):
        f = lambda y: 1 / (1 + np.exp(-y))
        return FunctionClass(f(x), 0.0)

    elif isinstance(x, FunctionClass):
        f = lambda y: 1 / (1 + exp(-y))
        res = f(x)
        return res

    else:
        raise TypeError(
                f"Type `{type(x)}` is not supported for logistic operations"
            )


def sinh(x):
    """Function that implements sinh (hyperbolic sin)

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: sinh(w)
    >>> a = FunctionClass(1, 2)
    >>> ans = g(a)
    >>> print(ans.val)
    1.1752011936438
    >>> print(ans.der)
    3.08616126963

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input is not a FunctionClass, int, float Object

    """
    if isinstance(x, FunctionClass):
        val = np.sinh(x.val)
        der = np.cosh(x.val) * x.der
        return FunctionClass(val, der)
    elif isinstance(x, _supported_types):
        val =np.sinh(x)
        return FunctionClass(val, 0.0)
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for sinh operation")


def cosh(x):
    """Function that implements cosh (hyperbolic cos)

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: cosh(w)
    >>> a = FunctionClass(2, 1)
    >>> ans = g(a)
    >>> print(ans.val)
    3.7621956910836
    >>> print(ans.der)
    3.626860407847

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input is not a FunctionClass, int, float Object

    """
    if isinstance(x, FunctionClass):
        return FunctionClass(np.cosh(x.val), (np.sinh(x.val) * x.der))
    elif isinstance(x, _supported_types):
        return FunctionClass(np.cosh(x), 0.0)
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for cosh operation")


def tanh(x):
    """Function that implements tanh (hyperbolic tan )

    Parameters
    ----------
    x: FunctionClass, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: tanh(w)
    >>> a = FunctionClass(2, 1)
    >>> ans = g(a)
    >>> print(ans.val)
    0.96402758007582
    >>> print(ans.der)
    0.07065082485

    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input is not a FunctionClass, int, float Object

    """
    if isinstance(x, FunctionClass):
        return FunctionClass(np.tanh(x.val), ((1 - np.tanh(x.val)**2) * x.der))
    elif isinstance(x, _supported_types):
        return FunctionClass(np.tanh(x), 0.0)
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for tanh operation")


