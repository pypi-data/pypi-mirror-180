#!/usr/bin/env python3
# File       : AutoDiffpy.py
# Description: Driver file
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np

import ElementaryFunc
from dual import Dual 
from Node import Node

class AutoDiffpy():

    """Implement the forward auto-differentiation"""

    def __init__(self, func, output_dimension = 1):
        """Constructor for AutoDiffpy class.
        Parameters
        ==========
        func: The functional input in lambda expression.
        output_dimension: The output dimension of the function (e.g., 2 for lambda x: [2*x, x-1]).
        Notes
        =====
        AutoDiffpy calculates the first derivative of func via forward mode auto differentiation. It takes 
        in a function that used lambda expression. If func is constructed via def keyword, we assume there is 
        no other local variables other than the functional inputs.
        """
        self.function = func 
        # We use code object for the function here and 
        # co_nlocals holds the total number of local variables of a function
        if not isinstance(func, list):
            try:
                self.input_dimension = func.__code__.co_nlocals
            except Exception as e:
                print(e)
            except:
                print("We might have a BaseException, or the system-exiting exceptions SystemExit, \
                KeyboardInterrupt and GeneratorExit")
        self.output_dimension = output_dimension

    def _get_values_helper(self, x):
        """
        Return the function value of input x.
        Parameters
        ----------
        x : int, float, Dual, list of int, float, Dual, or numpy.ndarray of int, float
        Input value to the primal trace of the computational graph.
        Returns
        -------
        value : int, float, Dual, or array of int or float
        The function value at the end of the primal trace of the computational graph.
        Examples
        --------
        >>> ad = AutoDiffpy(lambda x: 2*x)
        >>> ad.values(2)
        4
        >>> ad = AutoDiffpy(lambda x: 2*x**3 + 1)
        >>> ad.values(2)
        17
        """
        if self.input_dimension == 1: # if we are dealing with one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)):
                    result = []
                    for value in x:
                        if isinstance(value, (int, float)):
                            result.append(self.function(value))
                        elif isinstance(value, Dual):
                            result.append(self.function(value).real)
                        else:
                            raise TypeError('Only integer, float, and Dual scalar are supported!')
                    return np.array(result)
                elif isinstance(x, (int, float)):
                    return self.function(x)
                elif isinstance(x, Dual):
                    return self.function(x).real
                else:
                    raise TypeError('Only integer, float, and Dual scalar/list are supported!')
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.get_values(x))
                return np.array(result)
        else: # if we are dealing with more than one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)): # We require the input to be list/numpy.ndarray
                    if np.all([isinstance(x_i, (int, float)) for x_i in x]):
                        try:
                            return self.function(*x)
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, Dual) for x_i in x]):
                        try:
                            return self.function(*x).real
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, (list, np.ndarray)) for x_i in x]): # if the input is a vector input 
                        result = []
                        for value in x:
                            if len(value) != self.input_dimension:
                                raise ValueError(f"There is a mismatch in input dimension {len(value)} \
                                and {self.input_dimension}!")
                            if np.all([isinstance(value_i, (int, float)) for value_i in value]):
                                result.append(self.function(*value))
                            elif np.all([isinstance(value_i, Dual) for value_i in value]):
                                result.append(self.function(*value).real)
                            else:
                                raise TypeError('Only integer, float, and Dual scalar are supported!')
                        return np.array(result)
                    else:
                        raise TypeError('Only list/array of integer, float, Dual scalar, or list/array are supported!')
                else:
                    raise TypeError("We require the input to be list/numpy.ndarray!")
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.get_values(x))
                return np.array(result)
    
    def get_values(self, x):
        """
        Return the function value of input x.
        Parameters
        ----------
        x : int, float, Dual, list of int, float, Dual, or numpy.ndarray of int, float
        Input value to the primal trace of the computational graph.
        Returns
        -------
        value : int, float, Dual, or array of int or float
        The function value at the end of the primal trace of the computational graph.
        Examples
        --------
        >>> ad = AutoDiffpy(lambda x: 2*x)
        >>> ad.values(2)
        4
        >>> ad = AutoDiffpy(lambda x: 2*x**3 + 1)
        >>> ad.values(2)
        17
        """
        if isinstance(self.function, list):
            result = []
            for f_i in self.function:
                ad = AutoDiffpy(f_i)
                result.append(ad._get_values_helper(x))
            return np.array(result)
        else:
            return self._get_values_helper(x)

    def _forward_helper(self, x):
        """
        Return a tuple of the function's value and the gradient evaluated at x.
        Parameters
        ----------
        x : int, float, Dual
        Input value to the primal trace of the computational graph.
        Returns
        -------
        gradient : int, float, jacobian
        The function value and gradient at the end of the computational graph.
        Examples
        --------
        >>> ad = AutoDiffpy(lambda x: 2*x)
        >>> ad.values(2)
        4
        >>> ad = AutoDiffpy(lambda x: 2*x**3 + 1)
        >>> ad.values(2)
        17
        """
        if self.input_dimension == 1: # if we are dealing with one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)):
                    result = []
                    for value in x:
                        if isinstance(value, (int, float)):
                            result.append(self.function(Dual(value, 1)).dual)
                        elif isinstance(value, Dual):
                            result.append(self.function(value).dual)
                        else:
                            raise TypeError('Only integer, float, and Dual scalar are supported!')
                    return np.array(result)
                elif isinstance(x, (int, float)):
                    return self.function(Dual(x, 1)).dual
                elif isinstance(x, Dual):
                    return self.function(x).dual
                else:
                    raise TypeError('Only integer, float, and Dual scalar/list are supported!')
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.forward(x))
                return np.array(result)
        else: # if we are dealing with more than one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)): # We require the input to be list/numpy.ndarray
                    if np.all([isinstance(x_i, (int, float)) for x_i in x]):
                        x = [Dual(x_i, 1) for x_i in x]
                        try:
                            return self.function(*x)
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, Dual) for x_i in x]):
                        try:
                            return self.function(*x).dual
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, (list, np.ndarray)) for x_i in x]): # if the input is a vector input 
                        result = []
                        for value in x:
                            if len(value) != self.input_dimension:
                                raise ValueError(f"There is a mismatch in input dimension {len(value)} \
                                and {self.input_dimension}!")
                            if np.all([isinstance(value_i, (int, float)) for value_i in value]):
                                value = [Dual(value_i, 1) for value_i in value]
                                result.append(self.function(*value))
                            elif np.all([isinstance(value_i, Dual) for value_i in value]):
                                result.append(self.function(*value).dual)
                            else:
                                raise TypeError('Only integer, float, and Dual scalar are supported!')
                        return np.array(result)
                    else:
                        raise TypeError('Only list/array of integer, float, Dual scalar, or list/array are supported!')
                else:
                    raise TypeError("We require the input to be list/numpy.ndarray!")
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.forward(x))
                return np.array(result)

    def forward(self, x):
        """
        Return a tuple of the function's value and the gradient evaluated at x.
        Parameters
        ----------
        x : int, float, Dual
        Input value to the primal trace of the computational graph.
        Returns
        -------
        gradient : int, float, jacobian
        The function value and gradient at the end of the computational graph.
        Examples
        --------
        >>> ad = AutoDiffpy(lambda x: 2*x)
        >>> ad.values(2)
        4
        >>> ad = AutoDiffpy(lambda x: 2*x**3 + 1)
        >>> ad.values(2)
        17
        """
        if isinstance(self.function, list):
            result = []
            for f_i in self.function:
                ad = AutoDiffpy(f_i)
                result.append(ad._forward_helper(x))
            return np.array(result)
        else:
            return self._forward_helper(x)

class AutoDiffpy_reverse():

    """Implement the reverse auto-differentiation"""

    def __init__(self, func, output_dimension = 1):
        """Constructor for AutoDiffpy_reverse class.
        Parameters
        ==========
        func: The functional input in lambda expression.
        output_dimension: The output dimension of the function (e.g., 2 for lambda x: [2*x, x-1]).
        Notes
        =====
        AutoDiffpy_reverse calculates the first derivative of func via reverse mode auto differentiation. It takes 
        in a function that used lambda expression. If func is constructed via def keyword, we assume there is 
        no other local variables other than the functional inputs.
        """
        self.function = func
        self._roots = None
        self._value = None
        self._der = None
        if not isinstance(func, list):
            try:
                self.input_dimension = func.__code__.co_nlocals
            except Exception as e:
                print(e)
            except:
                print("We might have a BaseException, or the system-exiting exceptions SystemExit, \
                KeyboardInterrupt and GeneratorExit")
        self.output_dimension = output_dimension
        

    def reverse(self, x):
        """
        Return a the function's gradient evaluated at x.
        Parameters
        ----------
        x : int, float, Node
        Input value to the primal trace of the computational graph.
        Returns
        -------
        gradient : int, float, jacobian
        The function value and gradient at the end of the computational graph.
        Examples
        --------
        >>> ad = AutoDiffpy_reverse(lambda x: 2*x)
        >>> ad.reverse(2)
        2
        >>> ad = AutoDiffpy_reverse(lambda x: 2*x**3 + 1)
        >>> ad.reverse(2)
        24
        """
        if self.input_dimension == 1: # if we are dealing with one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)):
                    result = []
                    for x_i in x:
                        self._roots = Node(x_i)
                        f = self.function(self._roots)
                        f.derivative = 1 # we need to input the derivative of the last node in the computational graph
                        result.append(self._roots.get_derivative()) 
                    return np.array(result)
                elif isinstance(x, (int, float)):
                    self._roots = Node(x)
                    f = self.function(self._roots)
                    f.derivative = 1 # we need to input the derivative of the last node in the computational graph
                    return self._roots.get_derivative()
                elif isinstance(x, Node):
                    self._roots = x
                    f = self.function(self._roots)
                    f.derivative = 1 # we need to input the derivative of the last node in the computational graph
                    return self._roots.get_derivative()
                else:
                    raise TypeError('Only integer, float, and Node are supported!')
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy_reverse(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.reverse(x))
                return np.array(result)
        else: # if we are dealing with more than one variable input
            if self.output_dimension == 1: # if we are dealing with a scalar output
                if isinstance(x, (list, np.ndarray)):
                    if np.all([isinstance(x_i, (int, float)) for x_i in x]):
                        try:
                            self._roots = [Node(x_i) for x_i in x]
                            f = self.function(*self._roots)
                            f.derivative = 1
                            return np.array([root_i.get_derivative() for root_i in self._roots])
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, Node) for x_i in x]):
                        try:
                            self._roots = x
                            f = self.function(*self._roots)
                            f.derivative = 1
                            return np.array([root_i.get_derivative() for root_i in self._roots])
                        except Exception as e:
                            print(e)
                    elif np.all([isinstance(x_i, (list, np.ndarray)) for x_i in x]): # if the input is a vector input 
                        result = []
                        for value in x:
                            if len(value) != self.input_dimension:
                                raise ValueError(f"There is a mismatch in input dimension {len(value)} \
                                and {self.input_dimension}!")
                            if np.all([isinstance(value_i, (int, float)) for value_i in value]):
                                self._roots = [Node(x_i) for x_i in value]
                                f = self.function(*self._roots)
                                f.derivative = 1
                                result.append([root_i.get_derivative() for root_i in self._roots])
                            elif np.all([isinstance(value_i, Node) for value_i in value]):
                                self._roots = value
                                f = self.function(*self._roots)
                                f.derivative = 1
                                result.append([root_i.get_derivative() for root_i in self._roots])
                            else:
                                raise TypeError('Only integer, float, and Node are supported!')
                        return np.array(result)
                    else:
                        raise TypeError('Only list/array of integer, float, Node, or list/array are supported!')
                else:
                    raise TypeError("We require the input to be list/numpy.ndarray!")
            else: # if we are dealing with more than 2 ouputs dimension
                result = []
                for i in range(self.output_dimension):
                    def func_i(*args): return self.function(*args)[i] # find func f_i
                    ad = AutoDiffpy_reverse(func_i)
                    ad.input_dimension = self.input_dimension
                    result.append(ad.reverse(x))
                return np.array(result)

# if __name__ == "__main__":
#     x = 0.2
#     ad_reverse = AutoDiffpy_reverse(lambda x: ElementaryFunc.sin(x)**2 + x)
#     ad_derivative = lambda x: 2 * np.sin(x) * np.cos(x) + 1
#     if ad_reverse.reverse(x) == ad_derivative(x):
#         print(ad_reverse.reverse(x))
#         print("One variable scalar input and one variable scalar output match!")
    
#     if np.all(ad_reverse.reverse([0, 1, 2]) == np.array([ad_derivative(x_i) for x_i in [0, 1, 2]])):
#         print(ad_reverse.reverse([0, 1, 2]))
#         print("One variable vector input and one variable scalar output match!")

#     ad2_reverse = AutoDiffpy_reverse(lambda x: [ElementaryFunc.sin(x)**2 + x, x**2], 2)
#     ad2_derivative = lambda x: [2 * np.sin(x) * np.cos(x) + 1, 2 * x]
#     if np.all(ad2_reverse.reverse(x) == ad2_derivative(x)):
#         print(ad2_reverse.reverse(x))
#         print("One variable scalar input and two variable scalar output match!")

#     if np.all(ad2_reverse.reverse([0, 1, 2]) == np.array([ad2_derivative(x_i) for x_i in [0, 1, 2]]).T):
#         print(ad2_reverse.reverse([0, 1, 2]))
#         print("One variable vector input and two variable scalar output match!")

#     x, y, z = 1, 2, 3        
#     ad3_reverse = AutoDiffpy_reverse(lambda x, y, z: ElementaryFunc.sin(x)**2 + y**2 + z**2)
#     ad3_derivative = lambda x, y, z: [2 * np.sin(x) * np.cos(x), 2*y, 2*z]
#     if np.all(ad3_reverse.reverse([x, y, z]) == np.array(ad3_derivative(x, y, z))):
#         print(ad3_reverse.reverse([x, y, z]))
#         print("Three variable scalar input and one variable scalar output match!")

#     if np.all(ad3_reverse.reverse([[x, y, z], [x, y, z]]) == np.array([ad3_derivative(x, y, z), ad3_derivative(x, y, z)])):
#         print(ad3_reverse.reverse([[x, y, z], [x, y, z]]))
#         print("Three variable vector input and one variable scalar output match!")


#     ad4_reverse = AutoDiffpy_reverse(lambda x, y: [ElementaryFunc.sin(x)**2, y**2], 2)
#     ad4_derivative = lambda x, y: np.array([[2 * np.sin(x) * np.cos(x), 0], [0, 2*y]])
#     if np.all(ad4_reverse.reverse([x, y]) == ad4_derivative(x, y)):
#         print(ad4_reverse.reverse([x, y]))
#         print("Two variable scalar input and two variable scalar output match!")

#     print(ad4_reverse.reverse([[x, y], [x, y]]))
#     # x = Dual(2, 1)
    # ad = AutoDiffpy(lambda x: ElementaryFunc.sin(x))
    # if ad.get_values(x) == np.sin(2):
    #     print(ad.get_values(x))
    #     print("One variable scalar input and one variable scalar output match!")
    
    # if np.all(ad.get_values(np.array([1,2,3], dtype=float)) == np.sin([1,2,3])):
    #     print(ad.get_values(np.array([1,2,3], dtype=float)))
    #     print("One variable vector input and one variable vector output match!")

    # ad2 = AutoDiffpy(lambda x: [ElementaryFunc.exp(x) + 1, ElementaryFunc.cos(x)], 2)
    # if np.all(ad2.get_values(x) == np.array([np.exp(2) + 1, np.cos(2)])):
    #     print(ad2.get_values(x))
    #     print("One variable scalar input and two variable scalar output match!")

    # if np.all(ad2.get_values(np.array([1,2], dtype=float)) == np.array(
    #     [[np.exp(1) + 1, np.exp(2) + 1], [np.cos(1), np.cos(2)]]
    #     )):
    #     print(ad2.get_values(np.array([1,2], dtype=float)))
    #     print("One variable vector input and two variable vector output match!")

    # x1 = Dual(1, 1); x2 = Dual(2, 1)
    # ad3 = AutoDiffpy(lambda x, y: ElementaryFunc.exp(x)*y)
    # if ad3.get_values([x1, x2]) == np.exp(1)*2:
    #     print(ad3.get_values([x1, x2]))
    #     print("Two variable scalar input and one variable scalar output match!")

    # if np.all(ad3.get_values([[x1, x2], [x1, x2]]) == [np.exp(1)*2, np.exp(1)*2]):
    #     print(ad3.get_values([[x1, x2], [x1, x2]]))
    #     print("Two variable vector input and one variable scalar output match!")

    # ad4 = AutoDiffpy(lambda x, y: [ElementaryFunc.exp(x), y], 2)
    # if np.all(ad4.get_values([x1, x2]) == np.array([np.exp(1), 2])):
    #     print(ad4.get_values([x1, x2]))
    #     print("Two variable scalar input and two variable vector output match!")

    # if np.all(ad4.get_values([[x1, x2], [x1, x2]]) == np.array(
    #     [[np.exp(1), np.exp(1)], [2, 2]])):
    #     print(ad4.get_values([[x1, x2], [x1, x2]]))
    #     print("Two variable vector input and two variable vector output match!")

    # if ad.forward(x) == np.cos(2):
    #     print(ad.forward(x))
    #     print("Forward: One variable scalar input and one variable scalar output match!")
    
    # if np.all(ad.forward(np.array([1,2,3], dtype=float)) == np.cos([1,2,3])):
    #     print(ad.forward(np.array([1,2,3], dtype=float)))
    #     print("Forward: One variable vector input and one variable vector output match!")

    # ad2 = AutoDiffpy(lambda x: [ElementaryFunc.exp(x) + 1, ElementaryFunc.cos(x)], 2)
    # if np.all(ad2.forward(x) == np.array([np.exp(2), -np.sin(2)])):
    #     print(ad2.forward(x))
    #     print("Forward: One variable scalar input and two variable scalar output match!")

    # if np.all(ad2.forward(np.array([1,2], dtype=float)) == np.array(
    #     [[np.exp(1), np.exp(2)], [-np.sin(1), -np.sin(2)]]
    #     )):
    #     print(ad2.forward(np.array([1,2], dtype=float)))
    #     print("Forward: One variable vector input and two variable vector output match!")

    # if ad3.forward([x1, x2]) == np.exp(1)*2 + np.exp(1):
    #     print(ad3.forward([x1, x2]))
    #     print("Forward: Two variable scalar input and one variable scalar output match!")

    # if np.all(ad3.forward([[x1, x2], [x1, x2]]) == [np.exp(1)*2 + np.exp(1), np.exp(1)*2 + np.exp(1)]):
    #     print(ad3.forward([[x1, x2], [x1, x2]]))
    #     print("Forward: Two variable vector input and one variable scalar output match!")

    # ad4 = AutoDiffpy(lambda x, y: [ElementaryFunc.exp(x), y], 2)
    # if np.all(ad4.forward([x1, x2]) == np.array([np.exp(1), 1])):
    #     print(ad4.forward([x1, x2]))
    #     print("Forward: Two variable scalar input and two variable vector output match!")

    # if np.all(ad4.forward([[x1, x2], [x1, x2]]) == np.array(
    #     [[np.exp(1), np.exp(1)], [1, 1]])):
    #     print(ad4.forward([[x1, x2], [x1, x2]]))
    #     print("Forward: Two variable vector input and two variable vector output match!")