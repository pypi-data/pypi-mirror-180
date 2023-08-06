#!/usr/bin/env python3
# File       : ad_calculator.py
# Description: Forward mode calculation
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import warnings
warnings.filterwarnings("error")

import autodiff26.forward_mode.functions as ad

_supported_types = (int, float, list, np.ndarray, np.int32, np.int64)
def autodiff(function, eval = None, **kwargs):
    """Implements the calculator

    Parameters
    ----------
    function: Function
            Function to evaluate value and derivative.
            Takes any number of inputs.
    eval: str
        variable to differentiate with respect to
        If not provided defaults to first variable provided

    **kwargs: Arbitrary key word arguments
            Inputs to the function to evaluate

    Note
    -----
    Variable value to evaluate at can be single value, list or numpy array
    Lists will be converted to numpy arrays for efficiency
    Incase of multiple input types, type will be converted to numpy array

    Examples
    --------
    >>> x_1 = np.array([0.5,1,2])
    >>> x_2 = np.array([0.5,3,4])
    >>> f = lambda x_1,x_2: ad.sin(x_1*x_2) * ad.sin(0.5)
    >>> fn = autodiff(f, x_1=x_1, x_2=x_2)
    >>> print(fn.val)
    [0.11861178 0.06765654 0.47432361]
    >>> print(fn.der)
    [ 0.46452136 -1.89851074 -0.41853859]

    Returns
    -------
    any
        ad object with primal trace and tangent trace results
        can be accessed via obj.val and obj.der respectively

    Raises
    ------
    Exception
        If cannot successfully parse input elements
    """

    # make inputs uniform
    first_value = next(iter(kwargs.values()))  # returns first value

    # no variable specified, differentiate with respect to first variable provided
    if not eval:
        try:
            eval = next(iter(kwargs.keys()))
        except:
            raise Exception("Could not sucessfully set differentiation variable")
    # Check if lst is a list of lists
    if isinstance(first_value, list) and all(isinstance(x, list) for x in first_value):
        raise Exception("Input must be 1 dimensional")
    
    initial_length = len(np.array(first_value, ndmin=1)) # length of first object
    if not _uniformize(kwargs, initial_length):
        raise Exception("Could not successfully parse values to evaluate at")

    # evaluate function
    res_val = np.empty(initial_length)  # primal trace
    res_der = np.empty(initial_length)  # tangent trace
    
    res_val, res_der = _evaluate(kwargs, res_val, res_der, initial_length, function, eval)

    # process output to required form
    # if was scalar convert back to scalar else return np array
    try:
        res_val, res_der = res_val.item(), res_der.item()
        to_return = ad.FunctionClass(res_val, res_der)
    except:
        to_return = ad.FunctionClass(res_val, res_der)     
    return to_return
    
  
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
        # reset any gradient
        if not isinstance(kwargs[key], _supported_types):
            raise TypeError(f" {type(values)} is not a supported form on input")
        else:
            # dimension of inputs to evaluate at do not match
            try:
                # Check if lst is a list of lists
                if isinstance(values, list) and all(isinstance(x, list) for x in values):
                    raise Exception("Input must be 1 dimensional")
                array_values = np.array(values, ndmin=1, dtype=np.float64)
            except:
                raise Exception("Could not turn to np array")
            if len(array_values) != initial_length:
                raise Exception("Dimension of Values to evaluate at for multivariables must match")
            kwargs[key] = array_values

    return True


def _evaluate(kwargs, res_val, res_der, initial_length, function, eval):
    """Evaluates function at values provided

    Parameters
    -----------
    **kwargs: key word arguments representing variables and their values

    Returns
    -------
    np.array
        arrays of primal and tangent trace

    """   
    for i in range(initial_length):
        
        current = {}

        for key, value in kwargs.items():
            if eval and eval == key:
                current[key] =  ad.FunctionClass(value[i])
            else:
                current[key] = value[i]
    
        result = function(*[current[key] for key in kwargs])

        # constant result
        if isinstance(result, ad.FunctionClass):
            res_val[i], res_der[i] = result.val, result.der
        else:
            res_val[i], res_der[i] = result, 0.0

    return res_val, res_der
