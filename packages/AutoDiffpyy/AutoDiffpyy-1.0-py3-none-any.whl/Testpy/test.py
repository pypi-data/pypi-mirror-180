import sys
sys.path.append('../AutoDiffpy')
sys.path.append('AutoDiffpy')
sys.path.append('C:/Users/Louisa Zhao/anaconda3/Lib/site-packages')

import numpy as np
import pytest
from AutoDiffpy import AutoDiffpy
from AutoDiffpy import AutoDiffpy_reverse
from AutoDiffpy import Dual
from AutoDiffpy import ElementaryFunc
from Node import Node


def test_add():
	"""Test of addition special method (__add__) of Dual class."""
	#Test for addition with a scalar Dual object and a float
	x = Dual(2)
	fx = x+2.5
	#print(fx)
	assert fx.real ==4.5
	assert fx.dual == 1

	# Test for addition with a scaler Dual object with real equal to 2 and dual equal to 3
	x = Dual(2,3)
	fx = x+1
	assert fx.real == 3
	assert fx.dual == 3

	# Test for addition with two scalers Dual objects
	x = Dual(1,3)
	y = Dual(5.0,2.0)
	fx = x+y
	assert fx.real == 6.0
	assert fx.dual == 5.0

	# Test for addition with a Dual object
	# Expected to raise Type Error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = x + '2'

	# Test for addition with a Node object
	x = Node(2)
	z = x+2.5
	z.derivative = 1.0
	assert z.value == x.value+2.5
	assert x.get_derivative() == sum(child['partial_der']*child['node'].get_derivative() for child in x.children)



def test_radd():
	"""Test of reverse addition special method (__radd__) of Dual class."""
	# Test for reverse addition with a scaler Dual object
	x = Dual(1)
	fx = 1.5+x 
	assert fx.real == 2.5
	assert fx.dual == 1.0

	# Test for reverse addition with a scaler Dual object with real equal to 2 and dual equal to 3
	x = Dual(2,3)
	y = Dual(1,2)
	fx = x+y
	assert fx.real==x.real+y.real
	assert fx.dual==x.dual+y.dual


def test_sub():
	"""Test of subtraction special method (__sub__) of Dual class."""
	#Test for addition with a scalar Dual object and a int
	x = Dual(3)
	fx = x - 1
	assert fx.real == 2
	assert fx.dual == 1

	#Test for subtraction with a scalar Dual object and a float
	x = Dual(3.0,4.0)
	fx = x - 3
	assert fx.real == 0
	assert fx.dual == 4.0

	#Test for subtraction with two scalar Dual objects
	x = Dual(3.0,4.0)
	y = Dual(2,1)
	fx = x-y
	assert fx.real == 1.0
	assert fx.dual == 3.0

	# Test for substraction with a Dual object
	# Expected to raise Type Error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = x - '2'


def test_rsub():
	"""Test of reverse subtraction special method (__rsub__) of Dual class."""
	#Test for reverse substraction with a Dual object
	x = Dual(2,1)
	fx = 3 - x
	assert fx.real == 3 - x.real
	assert fx.dual == -1

	#Test for reverse substraction with two Dual objects
	x = Dual(2,1)
	fx = Dual(3,2)
	fx -= x
	assert fx.real == 1
	assert fx.dual == 1

	#Test for reverse substraction with  Dual objects
	# Expected to raise Type Error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = '2' - x

def test_mul():
	"""Test of multiplication special method (__mul__) of Dual class."""
	#Test 1 for multiplication with two Dual objects 
	x = Dual(2,3)
	y = Dual(4,5)
	fx = x * y 
	assert fx.real == 8
	assert fx.dual == 22

	#Test for multiplication with a Dual object and a float value
	x = Dual(2,3)
	fx = x * 4.0
	assert fx.real == 8.0
	assert fx.dual == 12.0

	#Test for multiplication with two Dual objects 
	x = Dual(2)
	y = Dual(3)
	fx = x * y 
	assert fx.real == 6
	assert fx.dual == 5

	#Test for multiplication with  Dual objects
	# Expected to raise Type Error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = x * '2'


def test_rmul():
	"""Test of reverse multiplication special method (__rmul__) of Dual class."""
	#Test for reverse multiplication with a Dual object and a float value
	x = Dual(4, 5)
	fx = 2 * x
	assert fx.real == 8
	assert fx.dual == 10

def test_truediv():
	"""Test of the division special method (__truediv__) of Dual class."""
	#Test for division with a Dual object and an int value
	x = Dual(2, 3)
	fx = x / 2
	assert fx.real == 1.0
	assert fx.dual == 1.5

	#Test for division with two Dual objects 
	x = Dual(2.0)
	y = Dual(1.0)
	fx = x / y
	assert fx.real == 2.0
	assert fx.dual == -1.0

	#Test for division with two Dual objects 
	x = Dual(2, 4)
	y = Dual(1, 2)
	fx = x / y
	assert fx.real == 2.0
	assert fx.dual == 0.0

	#Test for division with Dual objects
	# Expected to raise Type Error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = x / '2'

def test_rtruediv():
	"""Test of the reverse division special method (__rtruediv__) of Dual class."""
	#Test for reverse division with a Dual object and an int value
	x = Dual(2,1)
	fx = 4 / x
	assert fx.real == 4 / x.real
	assert fx.dual == -1.0

	#Test for reverse division with two Dual objects 
	x = Dual(1)
	y = Dual(2)
	fx = y / x
	assert fx.real == y.real/x.real
	assert fx.dual == -1

	#Test for reverse division with Dual object
	#Expected to raise error
	x = Dual(2)
	with pytest.raises(TypeError) as e_info:
		fx = '2' / x

def test_pow():
	"""Test of the power special method (__pow__) of Dual class."""
	#Test for power method with a Dual object and a int value
	x = Dual(3)
	fx = x**2
	assert fx.real == 9
	assert fx.dual == 1

	#Test for  power method with a Dual object and a int value
	x = Dual(3,2)
	fx = x**2
	assert fx.real == 9
	assert fx.dual == 4

	#Test for power method with two Dual objects 
	x = Dual(1,3)
	y = Dual(4,5)
	fx = x ** y
	assert fx.real == 1
	assert fx.dual == 12

	#Test for power method with Dual object
	#Expected to raise error
	x = Dual(1,3)
	with pytest.raises(TypeError) as e_info:
		fx =  x ** '2'

	# Test for addition with a Node object
	x = Node(2)
	y = Node(3)
	z = x**y
	z.derivative = 1.0
	assert z.value == x.value**y.value
	assert x.get_derivative() == y.value * x.value ** (y.value - 1)
	assert x.get_derivative() == sum(child['partial_der']*child['node'].get_derivative() for child in x.children)
	


def test_rpow():
	"""Test of the reverse power special method (__rpow__) of Dual class."""
	#Test for reverse power method with a Dual object and a int value
	x = Dual(3,2)
	fx = 2**x
	assert fx.real == 8
	assert fx.dual == 11.090354888959125

	#Test for reverse power method with two Dual objects 
	x = Dual(3)
	y = Dual(2)
	fx = y**x
	assert fx.real == y.real ** x.real
	assert fx.dual == x.real * (y.real**(x.real - 1)) * y.dual + np.log(y.real) * y.real**x.real * x.dual

	#Test for reverse power method with two Dual objects
	#Excepted to raise error
	x = Dual(1,3)
	with pytest.raises(TypeError) as e_info:
		fx =  '2' ** x


def test_neg():
	"""Test of the negation special method (__neg__) of Dual class."""
	#Test for negation with a scalar Dual object
	x = Dual(3)
	fx = -x
	assert fx.real == -3
	assert fx.dual == -1

	#Test for negation with a scalar Dual object
	x = Dual(3,5)
	fx = -x
	assert fx.real == -3
	assert fx.dual == -5

# def test_eq():
# 	"""Test of the equality operator method (__eq__) of Dual class."""
# 	#Test for equality operator with a scalar Dual object
# 	x = Dual(1,2)
# 	y = Dual(1,2)
# 	assert (x.real == y.real and x.dual == y.dual) == True
# 	assert (x.real == 2 and x.dual == 1) == False

# 	#Test for equality operator with a scalar Dual object
# 	x = Dual(1)
# 	y = 1
# 	assert (x.real == y) == True

# def test_ne():
# 	"""Test of the inequality operator (e.g. x!=y) (__ne__) of Dual class."""
# 	#Test for inequality operator with a scalar Dual object
# 	x = Dual(1,2)
# 	y = Dual(10,20)
# 	assert (x.real != y.real or x.dual != y.dual) == True
# 	assert (x.real == 2 or x.dual == 1) == False

# 	#Test for inequality operator with a scalar Dual object
# 	x = Dual(1)
# 	y = 10
# 	assert (x.real != y) == True


def test_repr():
	"""Print the content of dual class."""
	x = Dual(1,2)
	return repr(x) == f"Dual ({x.real}, {x.dual})"

def test_str():
	"""Print the content of dual class."""
	x = Dual(1,2)
	return  str(x)== f"Dual ({x.real}, {x.dual})"



# Test for Elementary functions
def test_sin():
	"""Test of the sine elementary function (sin) of ElementaryFunc class."""
	#Test for sine with a scalar Dual object
	x=Dual(2,1)
	z = ElementaryFunc.sin(x)
	assert z.real == np.sin(x.real)
	assert z.dual == np.cos(x.real)*x.dual

	# Test for sine with a Node object
	x=Node(2)
	z = ElementaryFunc.sin(x)
	z.derivative = 1
	# print(z.value,z.get_derivative(),np.cos(x.value))
	assert z.value == np.sin(x.value)
	assert x.get_derivative() == np.cos(x.value)

	# Test for sine with an int 
	x=2
	z = ElementaryFunc.sin(x)
	assert z.real == np.sin(x)


def test_cos():
	"""Test of the cosine elementary function (cos) of ElementaryFunc class."""
	#Test for cosine with a scalar Dual object
	x=Dual(2,1)
	z = ElementaryFunc.cos(x)
	assert z.real == np.cos(x.real)
	assert z.dual == -np.sin(x.real)*x.dual

	# Test for cosine with a Node object
	x=Node(2)
	z = ElementaryFunc.cos(x)
	z.derivative = 1
	assert z.value == np.cos(x.value)
	assert x.get_derivative() == -np.sin(x.value)

	# Test for cosine with an int 
	x=2
	z = ElementaryFunc.cos(x)
	assert z.real == np.cos(x)

def test_tan():
	"""Test of the tangent elementary function (tan) of ElementaryFunc class."""
	#Test for tangent with a scalar Dual object
	x=Dual(2,1)
	z = ElementaryFunc.tan(x)
	assert z.real == np.tan(x.real)
	assert z.dual == 1/np.cos(x.real)**2 * x.dual

	# Test for tangent with a Node object
	x=Node(2)
	z = ElementaryFunc.tan(x)
	z.derivative = 1
	assert z.value == np.tan(x.value)
	assert x.get_derivative() == 1/ np.cos(x.value)**2

	# Test for cosine with an int 
	x=2
	z = ElementaryFunc.tan(x)
	assert z.real == np.tan(x)

def test_exp():
	"""Test of the exponential elementary function (exp) of ElementaryFunc class."""
	#Test for exponential with a scalar Dual object
	x=Dual(2,1)
	z = ElementaryFunc.exp(x)
	assert z.real == np.exp(x.real)
	assert z.dual == np.exp(x.real) * x.dual

	# Test for exponential with a Node object
	x=Node(2)
	z = ElementaryFunc.exp(x)
	z.derivative = 1
	assert z.value == np.exp(x.value)
	assert x.get_derivative() == np.exp(x.value)

	# Test for cosine with an int 
	x=2
	z = ElementaryFunc.exp(x)
	assert z.real == np.exp(x)

# Test for new elementary funcs
def test_arcsin():
	"""Test of the arcsine elementary function (arcsin) of ElementaryFunc class."""
	#Test for arcsine with a scalar Dual object
	x=Dual(0.5)
	z=ElementaryFunc.arcsin(x)
	temp = 1-x.real**2
	# if temp <= 0:
	# 	raise ValueError('Domain of sqrt should be {x>=0}')
	assert z.real == np.arcsin(x.real)
	assert z.dual == 1/np.sqrt(temp)

	#Test for arcsine with a Node object
	x=Node(0.5)
	z=ElementaryFunc.arcsin(x)
	z.derivative = 1
	temp = 1-x.value**2
	# if temp <= 0:
	# 	raise ValueError('Domain of sqrt should be {x>=0}')
	assert z.value == np.arcsin(x.value)
	assert x.get_derivative() == 1/np.sqrt(temp)

	#Test for arcsine with an int
	x=0.5
	z=ElementaryFunc.arcsin(x)
	assert z == np.arcsin(x)

	#Test for arcsine value with a Node object 
	#should raise valueerror
	x=Node(5.0)
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.arcsin(x)
		# z.derivative=1
		# assert z.value == np.sinh(x.value)


def test_arccos():
	"""Test of the arccos elementary function (arccos) of ElementaryFunc class."""
	#Test for arccos with a scalar Dual object
	x=Dual(0.5)
	z=ElementaryFunc.arccos(x)
	temp=1-x.real**2
	# if temp <= 0:
	# 	raise ValueError('Domain of sqrt should be {x>=0}')
	assert z.real == np.arccos(x.real)
	assert z.dual == -1/np.sqrt(temp)
	# pass

	#Test for arcsine with an int
	x=0.5
	z=ElementaryFunc.arccos(x)
	assert z == np.arccos(x)

	#Test for arccos with a Node object
	x=Node(0.5)
	z=ElementaryFunc.arccos(x)
	z.derivative = 1
	temp = 1-x.value**2
	# if temp <= 0:
	# 	raise ValueError('Domain of sqrt should be {x>=0}')
	assert z.value == np.arccos(x.value)
	assert x.get_derivative() == -1/np.sqrt(temp)

	#Test for arcsine value with a Node object 
	#should raise valueerror
	x=Node(5.0)
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.arccos(x)
		# z.derivative=1
		# assert z.value == np.sinh(x.value)


def test_arctan():
	"""Test of the arctan elementary function (arctan) of ElementaryFunc class."""
	#Test for arctan with a scalar Dual object
	x=Dual(0.5)
	z=ElementaryFunc.arctan(x)
	temp=1+x.real**2
	# if temp <= 0:
	# 	raise ValueError('Domain of sqrt should be {x>=0}')
	assert z.real == np.arctan(x.real)
	assert z.dual == 1/temp

	#Test for arctan with an int
	x=0.5
	z=ElementaryFunc.arctan(x)
	assert z == np.arctan(x)

	#Test for arctan with a Node object
	x=Node(0.5)
	z=ElementaryFunc.arctan(x)
	z.derivative = 1
	assert z.value == np.arctan(x.value)
	assert x.get_derivative() == 1/(1+x.value**2)



def test_exponential():
	"""Test of the exponential elementary function (exponential) of ElementaryFunc class."""
	#Test for exponential value with a scalar Dual object and specified base
	x=Dual(5)
	base=2
	z=ElementaryFunc.exponential(base,x)
	assert z.real == base**x.real
	assert z.dual == np.log(base)*(base**x.real)

	#Test for exponential  with int
	x=5
	base=2
	z=ElementaryFunc.exponential(base,x)
	assert z.real == base**x

	#Test for exponential with a Node object
	x=Node(5)
	base=2
	z=ElementaryFunc.exponential(base,x)
	z.derivative = 1
	print(z.value,z.get_derivative())
	assert z.value == np.exp(x.value)
	# assert z.get_derivative() == base**x.value


def test_sinh():
	"""Test of the sinh elementary function (sinh) of ElementaryFunc class."""
	#Test for sinh value with a scalar Dual object and specified base
	x=Dual(1.0)
	z=ElementaryFunc.sinh(x)
	assert z.real == np.sinh(x.real)
	assert z.dual == np.cosh(x.real)

	#Test for sinh value with a int
	x=3.0
	z=ElementaryFunc.sinh(x)
	assert z.real == np.sinh(x)

	#Test for sinh value with a Node object
	x=Node(1.0)
	z=ElementaryFunc.sinh(x)
	z.derivative=1
	print(z.value, z.get_derivative(),np.cosh(x.value))
	assert z.value == np.sinh(x.value)
	# assert z.get_derivative() == np.cosh(x.value)



def test_cosh():
	"""Test of the cosh elementary function (cosh) of ElementaryFunc class."""
	#Test for cosh value with a scalar Dual object and specified base
	# pass
	x=Dual(1.0)
	z=ElementaryFunc.cosh(x)
	assert z.real == np.cosh(x.real)
	assert z.dual == np.sinh(x.real)

	#Test for cosh value with a int
	x=3.0
	z=ElementaryFunc.cosh(x)
	assert z.real == np.cosh(x)

	#Test for sinh value with a Node object
	x=Node(1.0)
	z=ElementaryFunc.cosh(x)
	z.derivative=1
	assert z.value == np.cosh(x.value)
	# assert z.get_derivative() == np.sinh(x.value)

def test_tanh():
	"""Test of the tanh elementary function (tanh) of ElementaryFunc class."""
	#Test for tanh value with a scalar Dual object and specified base
	x=Dual(2.0)
	z=ElementaryFunc.tanh(x)
	assert z.real == np.tanh(x.real)
	assert z.dual == 1-np.tanh(x.real)**2*x.dual

	#Test for tanh value with a int
	x=3.0
	z=ElementaryFunc.tanh(x)
	assert z.real == np.tanh(x)

	#Test for sinh value with a Node object
	x=Node(1.0)
	z=ElementaryFunc.tanh(x)
	z.derivative=1
	assert z.value == np.tanh(x.value)


def test_logistic():
	"""Test of the logistic elementary function (logistic) of ElementaryFunc class."""
	#Test for logistic value with a scalar Dual object and specified base
	x=Dual(3.0)
	z=ElementaryFunc.logistic(x)
	nom = np.exp(x.real)
	denom = (1+np.exp(x.real))**2
	tol = 1e-6
	assert z.real == 1/(1+np.exp(-x.real))
	assert abs(z.dual - (nom / denom)) < tol

	#Test for logistic with int
	x = 3
	z=ElementaryFunc.logistic(x)
	assert z == 1/(1+np.exp(-x))

	#Test for logistic value with a Node object
	x=Node(3.0)
	z=ElementaryFunc.logistic(x)
	z.derivative=1
	nom = np.exp(x.value)
	denom = (1+np.exp(x.value))**2
	assert z.value == 1/(1+np.exp(-x.value))
	# assert z.get_derivative() == nom/dom



def test_log():
	"""Test of the logistic elementary function with base e (log) of ElementaryFunc class."""
	#Test for logistic value with a scalar Dual object and base of e
	x=Dual(3.0)
	# print(x)
	z=ElementaryFunc.log(x)
	# print(z)
	assert z.real == np.log(x.real)
	assert z.dual == x.dual/x.real

	#Test for log with int
	x=3.0
	z=ElementaryFunc.log(x)
	assert z.real == np.log(x)

	#Test for log value with a Node object 
	x=Node(3.0)
	z=ElementaryFunc.log(x)
	z.derivative=1
	assert z.value == np.log(x.value)

	#Test for log value with a Dual object
	# Expected to raise value error
	x=Dual(-1.0)
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.log(x) 

def test_log2():
	"""Test of the logistic elementary function with base 2 (log2) of ElementaryFunc class."""
	#Test for logistic value with a scalar Dual object and base of 2
	x=Dual(3.0)
	z=ElementaryFunc.log2(x)
	assert z.real ==np.log2(x.real)
	assert z.dual == x.dual/(x.real*np.log(2))

	#Test for log2 with int
	x=3.0
	z=ElementaryFunc.log2(x)
	assert z.real == np.log2(x)

	#Test for log2 value with a Node object 
	x=Node(3.0)
	z=ElementaryFunc.log2(x)
	z.derivative=1
	assert z.value == np.log2(x.value)

	#Test for log2 value with a Dual object
	# Expected to raise value error
	x=Dual(-1.0)
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.log2(x) 

def test_log10():
	"""Test of the logistic elementary function with base 10 (log10) of ElementaryFunc class."""
	#Test for logistic value with a scalar Dual object and base of 10
	x=Dual(3.0)
	z=ElementaryFunc.log10(x)
	assert z.real ==np.log10(x.real)
	assert z.dual == x.dual/(x.real*np.log(10))

	#Test for log10 with int
	x=3.0
	z=ElementaryFunc.log10(x)
	assert z.real == np.log10(x)

	#Test for log value with a Node object 
	x=Node(3.0)
	z=ElementaryFunc.log10(x)
	z.derivative=1
	assert z.value == np.log10(x.value)

	#Test for log10 value with a Dual object
	# Expected to raise value error
	x=Dual(-1.0)
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.log10(x) 

def test_logarithm():
	"""Test of the logistic elementary function with a specified base (logarithm) of ElementaryFunc class."""
	#Test for logistic value with a scalar Dual object and specified base
	x=Dual(3.0)
	base=3
	z=ElementaryFunc.logarithm(x,base)
	assert z.real == np.log(x.real) / np.log(base)
	assert z.dual == x.dual / (x.real*np.log(base))

	#Test for logarithm with int
	x=3.0
	base=3
	z=ElementaryFunc.logarithm(x,base)
	assert z.real == np.log(x)/np.log(base)

	#Test for log value with a Node object 
	x=Node(3.0)
	base=3
	z=ElementaryFunc.logarithm(x, base)
	z.derivative=1
	assert z.value == np.log(x.value)/np.log(base)

	#Test for logarithm value with a Dual object
	# Expected to raise value error
	x=Dual(-1.0)
	base=3
	with pytest.raises(ValueError) as e_info:
		z=ElementaryFunc.logarithm(x,base) 

def test_sqrt():
	"""Test of the square root elementary function with a specified base (logarithm) of ElementaryFunc class."""
	#Test for sqrt with Dual object
	x=Dual(3.0)
	z=ElementaryFunc.sqrt(x)
	assert z.real == np.sqrt(x.real)
	assert z.dual == 2*x.real * x.dual

	#Test for sqrt with int
	x=3
	z=ElementaryFunc.sqrt(x)
	assert z.real == np.sqrt(x)

	#Test for log value with a Node object 
	x=Node(3.0)
	z=ElementaryFunc.sqrt(x)
	z.derivative=1
	assert z.value == x.value**(1/2)

def test_reverse():
	"""Test for reverse mode"""
	# Test for sine with a vector object
	x=[1,2,3]
	ad = AutoDiffpy(lambda x: ElementaryFunc.sin(x))
	assert np.all(ad.get_values(np.array(x, dtype=float)) == np.sin(x))

	# Test for sine in reverse mode
	x = 0.2
	ad_reverse = AutoDiffpy_reverse(lambda x: ElementaryFunc.sin(x)**2 + x)
	ad_derivative = lambda x: 2 * np.sin(x) * np.cos(x) + 1
	assert np.all(ad_reverse.reverse(x) == ad_derivative(x))

	ad2_reverse = AutoDiffpy_reverse(lambda x: [ElementaryFunc.sin(x)**2 + x, x**2], 2)
	ad2_derivative = lambda x: [2 * np.sin(x) * np.cos(x) + 1, 2 * x]
	assert np.all(ad2_reverse.reverse(x) == ad2_derivative(x))

	x, y, z = 1, 2, 3        
	ad3_reverse = AutoDiffpy_reverse(lambda x, y, z: ElementaryFunc.sin(x)**2 + y**2 + z**2)
	ad3_derivative = lambda x, y, z: [2 * np.sin(x) * np.cos(x), 2*y, 2*z]
	assert ad3_reverse.reverse([x, y, z])[0] == np.array(ad3_derivative(x, y, z))[0]
	# Three variable vector input and one variable scalar output match
	assert np.all(ad3_reverse.reverse([[x, y, z], [x, y, z]]) == np.array([ad3_derivative(x, y, z), ad3_derivative(x, y, z)]))

	ad4_reverse = AutoDiffpy_reverse(lambda x, y: [ElementaryFunc.sin(x)**2, y**2], 2)
	ad4_derivative = lambda x, y: np.array([[2 * np.sin(x) * np.cos(x), 0], [0, 2*y]])
	assert np.all(ad4_reverse.reverse([x, y]) == ad4_derivative(x, y))

	x = Node(0.2)
	ad5_reverse = AutoDiffpy_reverse(lambda x: x+1)
	ad5_derivative = lambda x: 1
	assert np.all(ad5_reverse.reverse(x) == ad5_derivative(x))

	with pytest.raises(TypeError) as e:
		ad3_reverse.reverse([[x, "2", z], [x, "2", z]])

	with pytest.raises(TypeError) as e:
		ad4_reverse.reverse([x, "1"])


def test_forward():
	"""Test for forward mode"""
	x = Dual(2, 1)
	ad = AutoDiffpy(lambda x: ElementaryFunc.sin(x))
	assert ad.get_values(x) == np.sin(2)
	assert np.all(ad.get_values(np.array([1,2,3], dtype=float)) == np.sin([1,2,3]))

	# Test forward mode
	assert ad.forward(x) == np.cos(2)
	assert np.all(ad.forward(np.array([1,2,3], dtype=float)) == np.cos([1,2,3]))

	# Test list of functions for forward mode
	ad2 = AutoDiffpy(lambda x: [ElementaryFunc.exp(x) + 1, ElementaryFunc.cos(x)], 2)
	assert np.all(ad2.get_values(x) == np.array([np.exp(2) + 1, np.cos(2)]))
	assert np.all(ad2.get_values(np.array([1,2], dtype=float)) == np.array([[np.exp(1) + 1, np.exp(2) + 1], [np.cos(1), np.cos(2)]]))
	assert np.all(ad2.forward(x) == np.array([np.exp(2), -np.sin(2)]))


	x1 = Dual(1, 1); x2 = Dual(2, 1)
	ad3 = AutoDiffpy(lambda x, y: ElementaryFunc.exp(x)*y)
	assert ad3.get_values([x1, x2]) == np.exp(1)*2
	assert np.all(ad3.get_values([[x1, x2], [x1, x2]]) == [np.exp(1)*2, np.exp(1)*2])
	assert ad3.forward([x1, x2]) == np.exp(1)*2 + np.exp(1)
	assert np.all(ad3.forward([[x1, x2], [x1, x2]]) == [np.exp(1)*2 + np.exp(1), np.exp(1)*2 + np.exp(1)])

	ad4 = AutoDiffpy(lambda x, y: [ElementaryFunc.exp(x), y], 2)
	assert np.all(ad4.get_values([x1, x2]) == np.array([np.exp(1), 2]))
	assert np.all(ad4.get_values([[x1, x2], [x1, x2]]) == np.array([[np.exp(1), np.exp(1)], [2, 2]]))
	assert np.all(ad4.forward([[x1, x2], [x1, x2]]) == np.array([[np.exp(1), np.exp(1)], [1, 1]]))

	# forward mode test for a vector input
	x = [1,2]
	ad5 = AutoDiffpy(lambda x:2*x)
	assert np.all(ad5.get_values(x) == 2*np.array(x))
	assert np.all(ad5.forward(x) == [2,2]) 

	with pytest.raises(TypeError) as e:
		ad2.get_values([[x, "2"], [x, "2"]])

	with pytest.raises(TypeError) as e:
		ad2.get_values('x')

	with pytest.raises(TypeError) as e:
		ad5.get_values('x')


# def test_special_pytest():
# 	"""Test of special methods of Dual class."""
# 	#Test for all functions in Dual with a scalar 
# 	with pytest.raises(AssertionError) as excinfo:
# 		test_add()
# 		test_radd()
# 		test_sub()
# 		test_rsub()
# 		test_sub()
# 		test_rsub()
# 		test_mul()
# 		test_rmul()
# 		test_truediv()
# 		test_rtruediv()
# 		test_pow()
# 		test_rpow()
# 		test_neg()
# 		test_sin()
# 		test_cos()
# 		test_exp()
# 		assert excinfo.type == AssertionError 
# 		#raise AssertionError("Failed in Special Methods.")


# def test_element_pytest():
# 	"""Test of all elementary methods of Dual class."""
# 	#Test for all elementary functions with a scalar 
# 	with pytest.raises(AssertionError) as excinfo:
# 		test_sin()
# 		test_cos()
# 		test_exp()
# 		test_arcsin()
# 		test_arccos()
# 		test_tanh()
# 		test_logistic()
# 		test_log()
# 		test_log2()
# 		test_log10()
# 		test_logarithm()
# 		test_sqrt()
# 		test_exponential()
# 		assert excinfo.type == AssertionError 
# 		#raise AssertionError("Failed in Elementary Functions.")

# if __name__ == "__main__":
# 	test_rpow()
# 	test_pow()
# 	test_forward()
# 	test_reverse()
