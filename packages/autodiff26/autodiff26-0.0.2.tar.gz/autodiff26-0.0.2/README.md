# AUTODIFF26
CI TESTS

[![.github/workflows/coverage.yml](https://code.harvard.edu/CS107/team26/actions/workflows/coverage.yml/badge.svg)](https://code.harvard.edu/CS107/team26/actions/workflows/coverage.yml)
[![.github/workflows/test.yml](https://code.harvard.edu/CS107/team26/actions/workflows/test.yml/badge.svg)](https://code.harvard.edu/CS107/team26/actions/workflows/test.yml)



## HOW TO USE PACKAGE
The easiest way to install autodiff_26 library is using pip install. We encourage using a virtual environment

```python

# start virtual environment
python3 -m venv <DIR>

# activate virtual enviroment
source <DIR>/bin/activate
```

Install Package from pip

```python
pip install autodiff26
```

Currently we support forward and reverse modes of automatic differentiation. We provide autodiff function for the forward mode differentiation and
reversediff function for reverse mode differentiation. Please find detailed description of implementation in our [Autodiff26 Documentation](https://code.harvard.edu/pages/CS107/team26/)\
To use forward mode, import the library

```python
from autodiff26 import autodiff, ad

```

If you would prefer to use reverse mode, import it as follows

```python
from autodiff26 import reversediff, rev_ad

```

## Forward mode
Forward mode supports both univariate and multivariate functions. The ad object imported gives access to elementary operations such as trigonometric functions,logarithmic , logistic, exponential among others. autodiff function returns an object with value and derivative of function at the point. Note that for a multivariate function if variable to differentiate with respect to is not specified we default to the first variable.

#### 1. Single Variable functions 

```python
>>> from autodiff26 import autodiff, ad
>>> x_val = 10
>>> f = lambda x: ad.sin(x) + ad.cos(x) + ad.tan(x)
>>> res = autodiff(f, x_1 = x_val)
# to access function value
>>> print(res.val)
-0.7347318125067355
# to access the derivative
>>> print(res.der)
1.1253213443963488

```

#### 2. Multivariable functions

```python
>>> from autodiff26 import autodiff, ad
>>> x = 1
>>> y = 3
>>> f = lambda x, y: ad.sin(x*y) * ad.sin(0.5)
>>> res = autodiff(f, x_1 = x_val, x_2 = y_val)
# to access function value
>>> print(res.val)
0.06765654
# to access the derivative
>>> print(res.der)
-1.89851074

```

Input can be np array, single numeral or list.
#### np array input example

```python
"""2 variable input, np array inputs"""
x = np.array([0.5,1,2])
y = np.array([0.5,3,4])

# ad object provides sin, cos, tan, exp , log methods to use
f = lambda x_1,x_2: ad.sin(x_1*x_2) * ad.sin(0.5)
fn = autodiff(f, x_1= x, x_2=y)

# returned object has value(val) and derivative(der) depending on inputs provided
print(fn.val)
[0.11861178 0.06765654 0.47432361]
print(fn.der)
[ 0.46452136 -1.89851074 -0.41853859]
```


#### single point input example

```python
x = 5.0
y = 7

# define function
f = lambda x,y: x*y
fn = autodiff(f, x = x, y = y)

# value and derivative at input points
print(fn.val)
35.0
print(fn.der)
12.0

```

## Reverse mode
Reverse mode also supports both univariate and multivariate functions. The rev_ad object imported gives access to elementary operations such as trigonometric functions,logarithmic , logistic, exponential among others. reversediff function returns derivative of function at the point(s) specified. As with the forward mode,for a multivariate function if variable to differentiate with respect to is not specified we default to the first variable.

#### 1. Single Variable functions 

```python
>>> from autodiff26 import reversediff, rev_ad
>>> x_val = 10
>>> f = lambda x: rev_ad.sin(x) + rev_ad.cos(x) + rev_ad.tan(x)
>>> res = reversediff(f, x_1 = x_val)
# to access the derivative
>>> print(res)
1.1253213443963488

```

#### 2. Multivariable functions

```python
>>> from autodiff26 import reversediff, rev_ad
>>> x = 1
>>> y = 3
>>> f = lambda x, y: rev_ad.sin(x*y) * rev_ad.sin(0.5)
>>> res = reversediff(f, x_1 = x_val, x_2 = y_val)
# to access the derivative
>>> print(res)
-1.89851074

```
As with forward mode, Input can be np array, single numeral or list.

## Broader Impact

autodiff26 was developed to promote the progress of computational science, machine learning, and their uses. The team developing autodiff26 comes from
different scientific and educational backgrounds, which helped us promote cross-disciplinary thinking regarding its application in different fields. The program was
also developed with the goal to be as user-friendly and accesible as possible, with the assumption that the user has had experience in Python. Our program can be utilized in virtually any scientific field, from optimizing drug development, projecting a country's financial growth, to modelling rising
temperatures due to climate change. In addition, the developers of this program come from diverse cultural background, most of which are from minority groups. We hope that we can set an example that computational science and software development
are possible for anyone, regardless of their background. 

While the benefits of our project are plenty, it is not without its potentially negative consequences. As with any other scientific tools, our program bear the burden of
misuse, both intentional and unintentional, that may be caused; however, our program warrants additional scrutiny due to the essential nature of Automatic Differentiation
in machine learning. For example, racial bias in machine learning algorithms utilized in the medical field can result in misdiagnosis of minority groups due to differences in physiology.
Our algorithm can be intentionally used for subjectively detrimental purposes, such as development of automated military weapons. It is the developers' hope that this program be used solely for academic and scientific uses that
helps progress technology in a positive light  

## SOFTWARE INCLUSIVITY

We have designed our software package so that it would be accessible to all users. We have implemented an extensive detailed note in our README.md file in which users could find details about our implementation and the purpose of our work in this software. Our team welcomes feedback from any users regardless of age, background, gender and culture. If any user wishes to make changes or believes that our software lacks important elements, our team is more than welcome to listen to those requests and make immediate arrangements. As our package is uploaded on the github page, it would allow for anyone to make a branch and make changes, which is a great feature that would allow for users to demonstrate how we can be able to better our software. Our package is for the people and we will not hold back from making it as best a usable and understandable interface as we can. Our team is made up of a diverse mix of engineers from different parts of the world, we deeply value the opinions and contributions of the international community that wishes to use our software. For the larger international community that wishes to make use of our package, our team is willing to make as many accommodations as possible if users report any problems and feedback. 



