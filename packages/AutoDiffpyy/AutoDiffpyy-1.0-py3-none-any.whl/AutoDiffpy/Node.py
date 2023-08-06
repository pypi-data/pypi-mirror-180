#!/usr/bin/env python3
# File       : AutoDiffpy.py
# Description: Node
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np

class Node():

    def __init__(self, value):
        """Constructor for Node class.
        Parameters
        ==========
        The numerical input to the Node.
        Notes
        =====
        The Node object contains the function value, partial derivative, and children nodes in the 
        computational graph.
        """
        self.value = value
        self.children = [] # list of dictionary
        self.derivative = None
    
    def get_derivative(self):
        """
        Return the evaluated derivative.
        Returns
        -------
        value : int, float, or array of int or float
        --------
        """
        if self.derivative is None: # if not last node
            self.derivative = sum(
                child['partial_der'] * child['node'].get_derivative() for child in self.children
                )

        return self.derivative

    def __add__(self, x):
        """
        Addition operator overloading for the Node class.
        Parameters
        ----------
        x : int, float, or Node.
        Returns
        -------
        value : Updated Node.
        """
        if isinstance(x, Node):
            child = Node(self.value + x.value)
            self.children.append({'partial_der':1, 'node':child})  
            x.children.append({'partial_der':1, 'node':child}) 
        elif isinstance(x, (int, float)):
            child = Node(self.value + x)
            self.children.append({'partial_der':1, 'node':child})

        return child

    def __pow__(self, x):
        """
        Power operator overloading for the Node class.
        Parameters
        ----------
        x : int, float, or Node.
        Returns
        -------
        value : Updated Node.
        """
        if isinstance(x, Node):
            child = Node(self.value ** x.value)
            self.children.append({'partial_der': x.value * self.value ** (x.value - 1), 'node': child})
            x.children.append({'partial_der': np.log(self.value) * self.value ** x.value, 'node': child})
        elif isinstance(x, (int, float)):
            child = Node(self.value ** x)
            self.children.append({'partial_der': x * self.value ** (x - 1), 'node': child})

        return child

# if __name__ == "__main__":
#     x = Node(0.2)
#     y = x**2 + x
#     y.derivative = 1 # we need to input the derivative of the last node in the computational graph
#     print(x.get_derivative())