#!/usr/bin/env python3
# File       : reverse_calculator.py
# Description: Reverse mode calculation
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import autodiff26.reverse_mode.reverse_functions as rev_ad
_supported_types = (int, float, list, np.ndarray)

def reversediff(function, eval = None, **kwargs):
    """Implements the reverse mode calculator

    Parameters
    ----------
    function: Function
            Function to evaluate value and derivative.
            Takes any number of inputs.
    eval: str
        Variable to get function derivative of, if multivariable. If set to none, will default to
        differentiate with respect to first variable
    **kwargs: Arbitrary key word arguments
            Inputs to the function to evaluate

    Example with single point input
    --------
    >>> x = 2
    >>> y = 5
    >>> z = 7.5
    >>> f = lambda x_1, x_2, x_3 : (x_1 * x_2 * x_3) + x_1
    >>> x_eval = reversediff(f, eval = 'x_1', x_1 = x, x_2 = y, x_3 = z)
    >>> print(x_eval)
    38.5
    >>> y_eval = reversediff(f, eval = 'x_2', x_1 = x, x_2 = y, x_3 = z)
    >>> print(y_eval)
    15.0
    >>> result = reversediff(f, x_1 = x, x_2 = y, x_3 = z)
    >>> print(result)
    77.0

    Example with multivariate input
    -------------------------------
    >>> x = [2, 1]
    >>> y = [5, 7]
    >>> z = [7, 9]
    >>> f = lambda x_1, x_2, x_3 : (x_1 * x_2 * x_3) + x_1
    >>> x_eval = reversediff(f, eval = 'x_1', x_1 = x, x_2 = y, x_3 = z)
    >>> print(x_eval)
    [36.0, 64.0]
    >>> y_eval = reversediff(f, eval = 'x_2', x_1 = x, x_2 = y, x_3 = z)
    >>> print(y_eval)
    [14.0, 9.0]
    >>> result  =reversediff(f, x_1 = x, x_2 = y, x_3 = z)
    >>> print(result)
    [36.0, 64.0]

    Returns
    -------
        Derivative at provided point(s)
    """
    # make inputs uniform
    first_value = next(iter(kwargs.values()))  # returns first value

    # Check if lst is a list of lists
    if isinstance(first_value, list) and all(isinstance(x, list) for x in first_value):
        raise Exception("Input must be 1 dimensional")
    
    initial_length = len(np.array(first_value, ndmin=1)) # length of first object

    # make inputs to be of uniform type
    if not _uniformize(kwargs, initial_length):
        raise Exception("Could not successfully parse values to evaluate at")

    # default to first variable if none provided
    if eval == None:
        try:
            eval = next(iter(kwargs.keys()))
        except:
            raise Exception("Could not successfully get differentiation variable")
        
    if not isinstance(eval, str):
        raise Exception("Please only enter one evaluation variable in string format")
    if eval not in kwargs:
        raise Exception("Please enter valid evaluation variable")

    # get derivative with respect to specified variable
    output =[]
    for i in range(initial_length):
        current = {}
        for key, value in kwargs.items():
            current[key] =  rev_ad.Node(value[i])

        function_ad = function(*[current[key] for key in kwargs])
        
        # not constant result
        if isinstance(function_ad, rev_ad.Node):
            function_ad.der = 1.0

        evaluated = current[eval]
        output.append(evaluated.grad())
    if len(output) == 1:
        return output[0]
    else:
        return output


def _uniformize(kwargs, initial_length):
    """Preprocesses input for input to calculator

    Parameters
    -----------
    **kwargs: key word arguments representing variables and their values

    Returns
    -------
    bool
        if successfully preprocesses input

    Raises
    ------
    TypeError
        If input not defined in terms of scalar int, float , list of scalars or np.array
    Exception
        If dimension of values to evaluate at do not match
    """

    # convert to np arrays
    for key in kwargs:
        values = kwargs[key]
        if not isinstance(kwargs[key], _supported_types):
            raise TypeError(f" {type(values)} is not a supported form on input")
        else:
            # dimension of inputs to evaluate at do not match
            try:
                array_values = np.array(values, ndmin=1, dtype=np.float64)
            except:
                raise Exception("Input must be at most 1 dimensional")
            if len(array_values) != initial_length:
                raise Exception("Dimension of Values to evaluate at for multivariables must match")
            kwargs[key] = array_values

    return True

   