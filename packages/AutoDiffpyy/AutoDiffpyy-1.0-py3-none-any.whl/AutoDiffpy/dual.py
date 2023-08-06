#!/usr/bin/env python3
# File       : dual.py
# Description: 
# Copyright 2022 Harvard University. All Rights Reserved.

"""Dual number implementation for forward AD mode.

This module overloads common built-in operators such as
addition, subtraction, multiplication and division
in Python to also include dual numbers. It also allows 
users to use standard objects such as int and float as usual. 

"""

import numpy as np

class Dual:
    """Class to implement dual numbers."""
    _supported_types = (int, float)

    def __init__(self, real, dual=1):
        """Constrctor for Dual class.
        
        Parameters
        ----------
        real : int, float
            Can either take in int or float type objects.
        dual: int, float
            Can either take in int or float type objects.

        """
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        """Overload the addition operator (+) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        elif not isinstance(other, self._supported_types):
            raise TypeError(f"Type {type(other)} is not supported for addition!")
        else: # supported types
            return Dual(self.real + other, self.dual)
    
    def __radd__(self, other):
        """Resort to .__add__() to take reversed input for addition.

        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        return self.__add__(other)
    
    def __sub__(self, other):
        """Overload the subtraction operator (-) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.

        """
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        elif not isinstance(other, self._supported_types):
            raise TypeError(f"Type {type(other)} is not supported for addition!")
        else:
            return Dual(self.real - other.real, self.dual)
    
    def __rsub__(self, other):
        """Take reversed input for subtraction.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual):
            return Dual(other.real - self.real, other.dual - self.dual)
        elif not isinstance(other, self._supported_types):
            raise TypeError(f"Type {type(other)} is not supported for addition!")
        else:
            return Dual(other.real - self.real, -self.dual)

    def __mul__(self, other):
        """Overload the multiplication operator (*) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual): # if other is dual
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        elif not isinstance(other, self._supported_types): # if other is not supported type
            raise TypeError(f"Type {type(other)} is not supported!")
        else: # if other is int or float
            return Dual(self.real * other, self.dual * other)
    
    def __rmul__(self, other):
        """Resort to .__mul__() to take reversed input for multiplication.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Overload the true division operator (/) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual): # if other is dual
            return Dual(
                self.real / other.real,
                self.dual / other.real - self.real * other.dual / other.real**2
            )
        elif not isinstance(other, self._supported_types): # if other is not supported type
            raise TypeError(f"Type {type(other)} is not supported!")
        else: # if other is int or float
            return Dual(self.real / other, self.dual / other)

    def __rtruediv__(self, other):
        """Take reversed input for division.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual): # if other is dual
            return Dual(
                other.real / self.real,
                other.dual / self.real - other.real * self.dual / self.real**2
            )
        elif not isinstance(other, self._supported_types): # if other is not supported type
            raise TypeError(f"Type {type(other)} is not supported!")
        else: # if other is int or float
            return Dual(other / self.real, -other * self.dual / self.real**2)
    
    def __pow__(self, other):
        """Overload the exponentiation operator (**) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual): # if other is dual
            return Dual(
                self.real**other.real,
                other.real * (self.real**(other.real - 1)) * self.dual + np.log(self.real) * self.real**other.real * other.dual
            )
        elif not isinstance(other, self._supported_types): # if other is not supported type
            raise TypeError(f"Type {type(other)} is not supported!")
        else: # if other is int or float
            return Dual(self.real**other, self.dual**other)
    
    def __rpow__(self, other):
        """Overload the reverse exponentiation operator (**) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        other : int, float, Dual
            Either a dual number of a real value.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.
        
        """
        if isinstance(other, Dual): # if other is dual
            return Dual(
                other.real**self.real,
                self.real * (other.real**(self.real - 1)) * other.dual + np.log(other.real) * other.real**self.real * self.dual
            )
        elif not isinstance(other, self._supported_types): # if other is not supported type
            raise TypeError(f"Type {type(other)} is not supported!")
        else: # if other is int or float
            return Dual(
                other**self.real,
                other**self.real * self.dual * np.log(other)
            )
    
    def __neg__(self):
        """Overload the negation operator (e.g. -x) to include dual numbers.
        
        Parameters
        ----------
        self : Dual
            Class object of "Dual" type.
        
        Returns
        -------
        value: Dual
            Returns the dual number with updated real and dual parts.

        """
        return Dual(-self.real, -self.dual)
    
    # def __eq__(self, other):
    #     """Overload the equality operator (e.g. x==y) to include dual numbers.
        
    #     Parameters
    #     ----------
    #     self : Dual
    #         Class object of "Dual" type.
    #     other : int, float, Dual
    #         Either a dual number of a real value.
        
    #     Returns
    #     -------
    #     value : bool
    #         Returns True if self and other is equal in all attributes.
        
    #     """
    #     if isinstance(other, Dual):
    #         return (self.real == other.real and self.dual == other.dual)
    #     else:
    #         return self.real == other
    
    # def __ne__(self, other):
    #     """Overload the inequality operator (e.g. x!=y) to include dual numbers.
        
    #     Parameters
    #     ----------
    #     self : Dual
    #         Class object of "Dual" type.
    #     other : int, float, Dual
    #         Either a dual number of a real value.
        
    #     Returns
    #     -------
    #     value : bool
    #         Returns True if self and other is not equal in any attribute.
        
    #     """
    #     if isinstance(other, Dual):
    #         return (self.real != other.real or self.dual != other.dual)
    #     else:
    #         return self.real != other
    
    def __repr__(self):
        """Print the content of dual class."""
        return f"Dual ({self.real}, {self.dual})"

    def __str__(self):
        """Print the content of dual class."""
        return f"Dual ({self.real}, {self.dual})"

# if __name__ == "__main__":
#     print("Addition:")
#     print(Dual(1, 3) + Dual(5.0, 2.0))
#     print(1 + Dual(2, 3))
#     print(Dual(2, 3) + 1)
#     print("\nSubtraction:")
#     print(Dual(3.0, 4.0) - Dual(2, 1))
#     print(Dual(3.0, 4.0) - 3)
#     print(3 - Dual(2, 1))
#     print("\nMultiplication:")
#     print(Dual(2, 3) * Dual(4, 5))
#     print(Dual(2, 3) * 4)
#     print(2 * Dual(4, 5))
#     print("\nTrue division:")
#     print(Dual(10, 3) / Dual(7, 5))
#     print(Dual(7, 5) / Dual(3, 10))
#     print(Dual(2, 3) / 3)
#     print(2 / Dual(3, 5))
#     print("\nExponentiation:")
#     print(Dual(3, 2)**Dual(4, 1))
#     print(Dual(4, 1)**Dual(3, 2))
#     print(Dual(3, 2)**2)
#     print(2**Dual(3, 2))
#     print("\nNegation:")
#     print(-Dual(3, 5))
#     print("\nEquality:")
#     x = Dual(3)
#     y = Dual(3)
#     print(x == y)
#     print("\nInequality:")
#     print(Dual(3) != Dual(4))