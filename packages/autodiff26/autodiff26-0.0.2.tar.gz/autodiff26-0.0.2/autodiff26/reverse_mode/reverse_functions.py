r"""Implements Function class object function methods"""

#!/usr/bin/env python3
# File       : reverse_functions.py
# Description: Define functions and override operators
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np
_supported_types = (int, float, np.int32, np.int64)
_base = np.exp(1)

class Node:
    """Function class for overrriding numeric operations in dual number operations"""

    def __init__(self, val):
        """Initialize node object

            Attributes
            ----------
            self.val = numeric value
            self.der = store derivative calculated during forward pass traversal
            self.children = store tuple of (tangent trace, primal trace)

        """
        self.val = val
        self.der = None
        self.children = []

    
    def __str__(self):
        """Formatted output of node obj"""

        return f"value: {self.val}, derivative: {self.der}"


    def grad(self):
        """Recursively calculate derivatives

        Example
        -------

        >>> x = Node(5.0)
        >>> y = Node(9.0)
        >>> g = lambda x, y: x * y
        >>> f = g(x,y)
        >>> f.der = 1.0
        >>> print(x.grad())
        9.0

        Returns
        -------
        der:
            Returns gradient/derivative of function with respect to vairable
        """
        if self.der is None:
            der = sum(derivative * child.grad() for derivative, child in self.children)
            self.der = der
        return self.der


    def __add__(self, other):
        """ Implements addition for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda w: w + w
        >>> x = Node(5.0)
        >>> result = f(x)
        >>> print(result.val)
        10.0
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
        if isinstance(other, Node):
            result = Node(self.val + other.val)
            self.children.append((1.0, result))
            other.children.append((1.0, result))
            return result
        elif isinstance(other, _supported_types):
            result = Node(self.val + other)
            self.children.append((1.0, result))
            return result
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for addition")


    def __sub__(self, other):
         """Function that implements subtraction

        Parameters
        ----------
        x: Node, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: w - 2.0
        >>> a = Node(5.0)
        >>> ans = g(a)
        >>> print(ans.val)
        3.0
        >>> print(ans.der)
        None

        Returns
        -------
        Node:
            Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """
         if isinstance(other, Node):

            result = Node(self.val - other.val)
            self.children.append((1.0, result))
            other.children.append((-1.0, result))
            return result
         elif isinstance(other, _supported_types):
            result = Node(self.val - other)
            self.children.append((1.0, result))
            return result
         else:
            raise TypeError(f"Type `{type(other)}` is not supported for addition")
    
    def __mul__(self, other):
        """ Implements multiplication for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda w: 2*w*w
        >>> x = Node(5.0)
        >>> result = f(x)
        >>> print(result.val)
        50.0
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
        if isinstance(other, Node):
            result = Node(self.val * other.val)
            self.children.append((other.val, result))
            other.children.append((self.val, result))
            return result
        elif isinstance(other, _supported_types):
            result = Node(self.val * other)
            self.children.append((other, result))
            return result
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for multiplication")

    def __rmul__(self, other):
        """Implements reflected multiplication by call __mul__"""
        return self.__mul__(other)

    def __radd__(self, other):
        """Implements reflected Addition by call __add__"""
        return self.__add__(other)

    def __rsub__(self, other):
        """Function that implements subtraction

        Parameters
        ----------
        x: Node, int, float
                input to evaluate value and derivative

        Examples
        --------
        >>> g = lambda w: 2 - w
        >>> a = Node(5.0)
        >>> ans = g(a)
        >>> print(ans.val)
        -3.0
        >>> print(ans.der)
        None

        Returns
        -------
        Node:
            Returns updated function object with value and derivative

        Raises
        ------
        TypeError
            If input not a FunctionClass, int, float Object

        """

        if isinstance(other, Node):
            result = Node(other.val - self.val)
            self.children.append((-1.0, result))
            other.children.append((1.0, result))
            return result
        elif isinstance(other, _supported_types):
            result = Node(other - self.val)
            self.children.append((-1.0, result))
            return result
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for addition")
            

    def __truediv__(self, other):
        """ Implements true division for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda v, w: v / w
        >>> x = Node(5.0)
        >>> y = Node(2.0)
        >>> result = f(x , 7)
        >>> print(result.val)
        2.5
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
        if isinstance(other, Node):
            result = Node(self.val / other.val)
            self.children.append((1 / other.val, result))
            other.children.append(((-self.val) / (other.val**2), result))
            return result
        elif isinstance(other, _supported_types):
            result = Node(self.val / other)
            self.children.append((1 / other, result))
            return result
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for division")

    def __rtruediv__(self, other):
        """Implements reflected true division"""
        if self.val == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        if isinstance(other, _supported_types):
            result = Node(other / self.val)
            self.children.append(((-other) / (self.val**2), result))
            return result
        else:
            raise TypeError(f"Type `{type(other)}` is not supported for division")



    def __abs__(self):
        """Function that implements absolute operation
        Parameters
        ----------
        x: Node object, int, float
                input to evaluate value and forward pass derivative
        
        Examples
        --------
        >>> f = lambda w: abs(w)
        >>> x = Node(-1)
        >>> result = f(x)
        >>> print(result.val)
        1.0
        >>> print(result.der)
        None
        
        Returns
        -------
        Node:
            Returns updated node object with value at the point in forward pass
        
        Raises
        ------
        TypeError
            If input is not a Node, int or float
        
        """
        if isinstance(self, Node):
            result = Node(abs(float(self.val)))
            self.children.append((1.0, result))
            return result
        elif not isinstance(self, _supported_types):
            raise TypeError(f"Type '{type(Node)}' is not supported for absolute value")

    def __pow__(self, other):
        """Function that implements the power operation
        
        Parameters
        ----------
        x: Node object, int, float
                Input to evaluate value and forward pass derivative
                
        Examples
        --------
        >>> f = lambda w: w**2
        >>> x = Node(2)
        >>> result = f(x)
        >>> print(result.val)
        4.0
        >>> print(result.der)
        None
        
        Returns
        -------
        Node:
            Returns updated node object with function value at the point
        
        Raises
        ------
        TypeError
            If input not a Node, int, float Object 
        """
        if isinstance(other, _supported_types):
            if self.val == 0 and other < 1:
                raise ZeroDivisionError(
                    f"0.0 cannot be raised to a negative power"
                )
        elif isinstance(other, Node):
            if self.val <= 0:
                raise ValueError(
                    f"self.val cannot be raised to the power of {other}; log is undefined for x = {self.val}"
                )
        try:
            Val = self.val ** other.val
            result = Node(Val)
            self.children.append((Val*other.val/self.val, result))
            other.children.append((Val*np.log(self.val), result))
            return result
        except AttributeError:
            result = Node(float(self.val**other))
            self.children.append((other*self.val**(other-1),result))
            return result

    def __rpow__(self, other):
        """Function to implement the reverse power operation
        
        Parameters
        ----------
        x: Node object, int, float
                Input to evaluate and forward pass derivative

        Examples
        --------
        >>> f = lambda w: 2**w
        >>> x = Node(3)
        >>> result = f(x)
        >>> print(result.val)
        8.0
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a Node, int, float Object
        """
        if other <= 0:
            raise ValueError(
                f"{other} cannot be raised to the power of {self.val}; log is undefined for x = {other}"
            )
        Val = other**self.val
        result = Node(float(Val))
        self.children.append((Val*np.log(other), result))
        return result

    def __neg__(self):
        """Function that negates an input for forward pass in reverse mode
        
        Parameters
        ----------
        x: Node object, int, float
                Input to evaluate value and forward pass derivative
        
        Examples
        --------
        >>> f = lambda w: -w
        >>> x = Node(1)
        >>> result = f(x)
        >>> print(result.val)
        -1.0
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a Node, int, float Object 
        """

        if isinstance(self,Node):
            result = Node(self.val*-1)
            self.children.append((-1.0, result))
            return result
        elif not isinstance(self, _supported_types):
            raise TypeError(f"Type '{type(Node)}' is not supported for negation")

        
def sin(x):
    """Implements sin rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

    Examples
    ---------
    >>> f = lambda w: sin(w)
    >>> x = Node(0)
    >>> result = f(x)
    >>> print(result.val)
    0.0
    >>> print(result.der)
    None

    Returns
    -------
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a Node, int, float Object 
    """
    if isinstance(x, Node):
        result = Node(np.sin(x.val))
        x.children.append((np.cos(x.val), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.sin(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for sin operation")


def cos(x):
    """Implements cos rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

    Examples
    ---------
    >>> f = lambda w: cos(w)
    >>> x = Node(0)
    >>> result = f(x)
    >>> print(result.val)
    1.0
    >>> print(result.der)
    None

    Returns
    -------
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a Node, int, float Object 
    """
    if isinstance(x, Node):
        result = Node(np.cos(x.val))
        x.children.append((-np.sin(x.val), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.cos(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for cos operation")


def tan(x):
   """Function that implements tan rules for primal and tangent trace

    Parameters
    ----------
    x: Node, int, float
            input to evaluate value and derivative

    Examples
    --------
    >>> g = lambda w: tan(w)
    >>> a = Node(0)
    >>> ans = g(a)
    >>> print(ans.val)
    0.0
    >>> print(ans.der)
    None
 
    Returns
    -------
    FunctionClass
                Returns updated function object with value and derivative

    Raises
    ------
    TypeError
        If input not a Node, int, float Object

    """
   if isinstance(x, Node):
        result = Node(np.tan(x.val))
        x.children.append((1 / (np.cos(x.val)**2), result))
        return result
   elif isinstance(x, _supported_types):
        result = Node(np.tan(x))
        return result
   else:
        raise TypeError(f"Type `{type(x)}` is not supported for sinh operation")


def arcsin(x):
   """Implements arcsin rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

    Examples
    ---------
    >>> f = lambda w: arcsin(w)
    >>> x = Node(0.1)
    >>> result = f(x)
    >>> print(result.val)
    0.1001674211615598
    >>> print(result.der)
    None

    Returns
    -------
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a FunctionClass, int, float Object 
    """
   if isinstance(x, Node):
        if abs(x.val) >= 1:
            raise ValueError(f"Derivative of arcsin(x) undefined at x = {x.val}")
        result = Node(np.arcsin(x.val))
        x.children.append((1 / np.sqrt(1 - x.val**2), result))
        return result
   elif isinstance(x, _supported_types):
        if abs(x) >=1:
            raise ValueError(f"Derivative of arcsin(x) undefined at x = {x}")
        result = Node(np.arcsin(x))
        return result
   else:
        raise TypeError(f"Type `{type(x)}` is not supported for arcsin operation")
    
def arccos(x):
    """Implements arccos rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

    Examples
    ---------
    >>> f = lambda w: arccos(w)
    >>> x = Node(0.1)
    >>> result = f(x)
    >>> print(result.val)
    1.4706289056333368
    >>> print(result.der)
    None

    Returns
    -------
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a FunctionClass, int, float Object 
    """
    if isinstance(x, Node):
        if abs(x.val) >= 1:
            raise ValueError(f"Derivative of arccos(x) undefined at x = {x.val}")
        result = Node(np.arccos(x.val))
        x.children.append((-1 / np.sqrt(1 - x.val**2), result))
        return result
    elif isinstance(x, _supported_types):
        if abs(x) >=1:
            raise ValueError(f"Derivative of arcsin(x) undefined at x = {x}")
        result = Node(np.arccos(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for arcsin operation")

def arctan(x):
   
    """Implements arccos rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

    Examples
    ---------
    >>> f = lambda w: arctan(w)
    >>> x = Node(0.1)
    >>> result = f(x)
    >>> print(result.val)
    0.09966865249116204
    >>> print(result.der)
    None

    Returns
    -------
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a FunctionClass, int, float Object 
    """
    if isinstance(x, Node):
        result = Node(np.arctan(x.val))
        x.children.append((1 / (1 + x.val**2), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.arctan(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for arcsin operation")
    


def exp(x):
    """Implements exp rules for forward pass reverse mode

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
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
    if isinstance(x, Node):
        result = Node(np.exp(x.val))
        x.children.append(((np.exp(x.val)), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.exp(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for exp operation")

def log(x, base=_base):
    """Implements log rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

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
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a FunctionClass, int, float Object 
    """
    if base == 0:
        raise ValueError("Cannot take log of base 0")
    if isinstance(x, Node):
        if x.val <= 0 or base == 1:
            raise ValueError("Cannot take log of non-positive values")
        result = Node(np.log(x.val) / np.log(base))
        x.children.append((1 / (x.val * np.log(base)), result))
        return result
    elif isinstance(x, _supported_types):
        if x <= 0 or base == 1:
            raise ValueError("Cannot take log of non-positive values")
        result = Node(np.log(x) / np.log(base))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for log operation")

def sqrt(x):
    """Implements sqrt rules for forward pass reverse mode

    Parameters
    ----------
    x: int, float, Node Object
        Input to evaluate value and forward pass derivative

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
    Node:
        Returns updated node object with function value at the point

    Raises
    -------
    TypeError
        If input not a FunctionClass, int, float Object 
    """
    if isinstance(x, Node):
        if x.val <= 0:
            raise ValueError(f"The derivative of the square root of x is undefined for x.val <= 0")
        result = Node(np.sqrt(x.val))
        x.children.append((0.5 / np.sqrt(x.val), result))
        return result
    elif isinstance(x, _supported_types):
        if x < 0:
            raise ValueError(f"The square root of x is undefined for x < 0")
        result = Node(np.sqrt(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for sqrt operation")


def logistic(x):
    """Implements logistic rules for forward pass reverse mode

    Parameters
    -----------
    x: int, float, Node object
        Input to evaluate value and forward pass derivative

    Examples
    --------
    >>> f = lambda w: logistic(w)
    >>> x = Node(0)
    >>> result = f(x)
    >>> print(result.val)
    0.5
    >>> print(result.der)
    None

    Returns
    --------
    Node
        Returns updated Node object with function value

    Raises
    ------
    TypeError
        If input not a Node, int, float Object

    """
    # logistic function
    f = lambda y: 1 / (1 + np.exp(-y))
    
    if isinstance(x, _supported_types):
        result = Node(f(x))
        return result

    elif isinstance(x, Node):
        result = Node(f(x.val))
        deriv = (1-f(x.val))*f(x.val)
        x.children.append((deriv, result))
        return result

    else:
        raise TypeError(
                f"Type `{type(x)}` is not supported for logistic operations"
            )
    

def sinh(x):
    """Implements sinh rules for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda w: sinh(w)
        >>> x = Node(1.0)
        >>> result = f(x)
        >>> print(result.val)
        1.1752011936438
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
    if isinstance(x, Node):
        result = Node(np.sinh(x.val))
        x.children.append((np.cosh(x.val), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.sinh(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for sinh operation")


def cosh(x):
    """Implements cosh rules for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda w: cosh(w)
        >>> x = Node(1.0)
        >>> result = f(x)
        >>> print(result.val)
        1.5430806348152
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
    if isinstance(x, Node):
        result = Node(np.cosh(x.val))
        x.children.append((np.sinh(x.val), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.cosh(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for cosh operation")


def tanh(x):
    """Implements tanh rules for forward pass reverse mode

        Parameters
        ----------
        x: int, float, Node Object
            Input to evaluate value and forward pass derivative

        Examples
        ---------
        >>> f = lambda w: tanh(w)
        >>> x = Node(1.0)
        >>> result = f(x)
        >>> print(result.val)
        0.76159415595576
        >>> print(result.der)
        None

        Returns
        -------
        Node:
            Returns updated node object with function value at the point

        Raises
        -------
        TypeError
            If input not a FunctionClass, int, float Object
        """
    if isinstance(x, Node):
        result = Node(np.tanh(x.val))
        x.children.append(((1 - np.tanh(x.val)**2), result))
        return result
    elif isinstance(x, _supported_types):
        result = Node(np.tanh(x))
        return result
    else:
        raise TypeError(f"Type `{type(x)}` is not supported for tanh operation")
