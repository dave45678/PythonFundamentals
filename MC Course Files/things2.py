Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter your name: dl
Enter your age: 22
dl is 22 years old.
>>> 8
8
>>> 8*2
16
>>> 8**2
64
>>> 8***3
SyntaxError: invalid syntax
>>> 8/12
0.6666666666666666
>>> 8//12
0
>>> 9/0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    9/0
ZeroDivisionError: division by zero
>>> 1//2
0
>>> 2//1
2
>>> 5/2
2.5
>>> 5//2
2
>>> 1/4
0.25
>>> 1//4
0
>>> 1/2
0.5
>>> 1//2
0
>>> 2//3
0
>>> 3//3
1
>>> 4//3
1
>>> 10001/10000
1.0001
>>> 10001//10001
1
>>> 5//2
2
>>> 
>>> 
>>> 10001/10000
1.0001
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.4's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> floor division
no Python documentation found for 'floor division'

help> division
no Python documentation found for 'division'

help> /
Operator precedence
*******************

The following table summarizes the operator precedence in Python, from
lowest precedence (least binding) to highest precedence (most
binding).  Operators in the same box have the same precedence.  Unless
the syntax is explicitly given, operators are binary.  Operators in
the same box group left to right (except for exponentiation, which
groups from right to left).

Note that comparisons, membership tests, and identity tests, all have
the same precedence and have a left-to-right chaining feature as
described in the *Comparisons* section.

+-------------------------------------------------+---------------------------------------+
| Operator                                        | Description                           |
+=================================================+=======================================+
| "lambda"                                        | Lambda expression                     |
+-------------------------------------------------+---------------------------------------+
| "if" -- "else"                                  | Conditional expression                |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | Boolean OR                            |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | Boolean AND                           |
+-------------------------------------------------+---------------------------------------+
| "not" "x"                                       | Boolean NOT                           |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparisons, including membership     |
| ">=", "!=", "=="                                | tests and identity tests              |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | Bitwise OR                            |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | Bitwise XOR                           |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | Bitwise AND                           |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Shifts                                |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Addition and subtraction              |
+-------------------------------------------------+---------------------------------------+
| "*", "/", "//", "%"                             | Multiplication, division, remainder   |
|                                                 | [5]                                   |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | Positive, negative, bitwise NOT       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponentiation [6]                    |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]",                   | Subscription, slicing, call,          |
| "x(arguments...)", "x.attribute"                | attribute reference                   |
+-------------------------------------------------+---------------------------------------+
| "(expressions...)", "[expressions...]", "{key:  | Binding or tuple display, list        |
| value...}", "{expressions...}"                  | display, dictionary display, set      |
|                                                 | display                               |
+-------------------------------------------------+---------------------------------------+

-[ Footnotes ]-

[1] While "abs(x%y) < abs(y)" is true mathematically, for floats
    it may not be true numerically due to roundoff.  For example, and
    assuming a platform on which a Python float is an IEEE 754 double-
    precision number, in order that "-1e-100 % 1e100" have the same
    sign as "1e100", the computed result is "-1e-100 + 1e100", which
    is numerically exactly equal to "1e100".  The function
    "math.fmod()" returns a result whose sign matches the sign of the
    first argument instead, and so returns "-1e-100" in this case.
    Which approach is more appropriate depends on the application.

[2] If x is very close to an exact integer multiple of y, it's
    possible for "x//y" to be one larger than "(x-x%y)//y" due to
    rounding.  In such cases, Python returns the latter result, in
    order to preserve that "divmod(x,y)[0] * y + x % y" be very close
    to "x".

[3] While comparisons between strings make sense at the byte
    level, they may be counter-intuitive to users.  For example, the
    strings ""\u00C7"" and ""\u0327\u0043"" compare differently, even
    though they both represent the same unicode character (LATIN
    CAPITAL LETTER C WITH CEDILLA).  To compare strings in a human
    recognizable way, compare using "unicodedata.normalize()".

[4] Due to automatic garbage-collection, free lists, and the
    dynamic nature of descriptors, you may notice seemingly unusual
    behaviour in certain uses of the "is" operator, like those
    involving comparisons between instance methods, or constants.
    Check their documentation for more info.

[5] The "%" operator is also used for string formatting; the same
    precedence applies.

[6] The power operator "**" binds less tightly than an arithmetic
    or bitwise unary operator on its right, that is, "2**-1" is "0.5".

Related help topics: lambda, or, and, not, in, is, BOOLEAN, COMPARISON,BITWISE, SHIFTING, BINARY, FORMATTING, POWER, UNARY, ATTRIBUTES,SUBSCRIPTS, SLICINGS, CALLS, TUPLES, LISTS, DICTIONARIES

help> //
Operator precedence
*******************

The following table summarizes the operator precedence in Python, from
lowest precedence (least binding) to highest precedence (most
binding).  Operators in the same box have the same precedence.  Unless
the syntax is explicitly given, operators are binary.  Operators in
the same box group left to right (except for exponentiation, which
groups from right to left).

Note that comparisons, membership tests, and identity tests, all have
the same precedence and have a left-to-right chaining feature as
described in the *Comparisons* section.

+-------------------------------------------------+---------------------------------------+
| Operator                                        | Description                           |
+=================================================+=======================================+
| "lambda"                                        | Lambda expression                     |
+-------------------------------------------------+---------------------------------------+
| "if" -- "else"                                  | Conditional expression                |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | Boolean OR                            |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | Boolean AND                           |
+-------------------------------------------------+---------------------------------------+
| "not" "x"                                       | Boolean NOT                           |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparisons, including membership     |
| ">=", "!=", "=="                                | tests and identity tests              |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | Bitwise OR                            |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | Bitwise XOR                           |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | Bitwise AND                           |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Shifts                                |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Addition and subtraction              |
+-------------------------------------------------+---------------------------------------+
| "*", "/", "//", "%"                             | Multiplication, division, remainder   |
|                                                 | [5]                                   |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | Positive, negative, bitwise NOT       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponentiation [6]                    |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]",                   | Subscription, slicing, call,          |
| "x(arguments...)", "x.attribute"                | attribute reference                   |
+-------------------------------------------------+---------------------------------------+
| "(expressions...)", "[expressions...]", "{key:  | Binding or tuple display, list        |
| value...}", "{expressions...}"                  | display, dictionary display, set      |
|                                                 | display                               |
+-------------------------------------------------+---------------------------------------+

-[ Footnotes ]-

[1] While "abs(x%y) < abs(y)" is true mathematically, for floats
    it may not be true numerically due to roundoff.  For example, and
    assuming a platform on which a Python float is an IEEE 754 double-
    precision number, in order that "-1e-100 % 1e100" have the same
    sign as "1e100", the computed result is "-1e-100 + 1e100", which
    is numerically exactly equal to "1e100".  The function
    "math.fmod()" returns a result whose sign matches the sign of the
    first argument instead, and so returns "-1e-100" in this case.
    Which approach is more appropriate depends on the application.

[2] If x is very close to an exact integer multiple of y, it's
    possible for "x//y" to be one larger than "(x-x%y)//y" due to
    rounding.  In such cases, Python returns the latter result, in
    order to preserve that "divmod(x,y)[0] * y + x % y" be very close
    to "x".

[3] While comparisons between strings make sense at the byte
    level, they may be counter-intuitive to users.  For example, the
    strings ""\u00C7"" and ""\u0327\u0043"" compare differently, even
    though they both represent the same unicode character (LATIN
    CAPITAL LETTER C WITH CEDILLA).  To compare strings in a human
    recognizable way, compare using "unicodedata.normalize()".

[4] Due to automatic garbage-collection, free lists, and the
    dynamic nature of descriptors, you may notice seemingly unusual
    behaviour in certain uses of the "is" operator, like those
    involving comparisons between instance methods, or constants.
    Check their documentation for more info.

[5] The "%" operator is also used for string formatting; the same
    precedence applies.

[6] The power operator "**" binds less tightly than an arithmetic
    or bitwise unary operator on its right, that is, "2**-1" is "0.5".

Related help topics: lambda, or, and, not, in, is, BOOLEAN, COMPARISON,BITWISE, SHIFTING, BINARY, FORMATTING, POWER, UNARY, ATTRIBUTES,SUBSCRIPTS, SLICINGS, CALLS, TUPLES, LISTS, DICTIONARIES

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 1%2
1
>>> 20mod 60
SyntaxError: invalid syntax
>>> 20 mod 60
SyntaxError: invalid syntax
>>> 20 % 60
20
>>> 20 % 67
20
>>> 20 % 67
20
>>> name = input("Enter your name")
Enter your namebart
>>> print name
SyntaxError: Missing parentheses in call to 'print'
>>> print(name)
bart
>>> name = None
>>> print (name)
None
>>> ================================ RESTART ================================
>>> 
Enter the gross income: 50000
Enter the number of dependents: 2
The income tax is $6800.0
>>> 50000
50000
>>> ================================ RESTART ================================
>>> 
Enter the cube's edge: 50
The surface area is 15000.0 square units.
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> math.pi
3.141592653589793
>>> math.sqrt(2)
1.4142135623730951
>>> help(math.cos)
Help on built-in function cos in module math:

cos(...)
    cos(x)
    
    Return the cosine of x (measured in radians).

>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an int.
        This is the smallest integral value >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an int.
        This is the largest integral value <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    pi = 3.141592653589793

FILE
    (built-in)


>>> math.e
2.718281828459045
>>> from math import pi, sqrt
>>> print (pi)
3.141592653589793
>>> print (sqrt(9))
3.0
>>> import pandas
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    import pandas
ImportError: No module named 'pandas'
>>> ================================ RESTART ================================
>>> 
Enter the starting salary: $30000
Enter the annual % increase: 2
Enter the number of years: 11
Year   Salary
-------------
 1    30000.00
 2    30600.00
 3    31212.00
 4    31836.24
 5    32472.96
 6    33122.42
 7    33784.87
 8    34460.57
 9    35149.78
10    35852.78
11    36569.83
>>> 1 & 1
1
>>> A = True
>>> A
True
>>> A = 1
>>> A
1
>>> A or B
1
>>> B = False
>>> A = True
>>> A
True
>>> A and B
False
>>> A & B
False
>>> not A
False
>>> False and True
False
>>> False & True
False
>>> 1 and true
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    1 and true
NameError: name 'true' is not defined
>>> 1 and True
True
>>> True and 1
1
>>> False and 1 and True
False
>>> False and 0
False
>>> False and 0 and 0 and True and False
False
>>> 0 and False
0
>>> A = True
>>> B = True
>>> A
True
>>> A and B
True
>>> B = False
>>> A and B
False
>>> A = False
>>> A and B
False
>>> if A == True print "A is True"
SyntaxError: invalid syntax
>>> if A == True print ("A is True")
SyntaxError: invalid syntax
>>> if A == True print("A is True")
SyntaxError: invalid syntax
>>> if A = True print("A is True")
SyntaxError: invalid syntax
>>> if A = True: print("A is True")
SyntaxError: invalid syntax
>>> if A = True: print("A is True")
SyntaxError: invalid syntax
>>> if A = True:print("A is True")
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/temp/test.py", line 1, in <module>
    if A == True:
NameError: name 'A' is not defined
>>> ================================ RESTART ================================
>>> 
A is True
>>> ================================ RESTART ================================
>>> 
A is True
>>> ================================ RESTART ================================
>>> 
A is not True
>>> ================================ RESTART ================================
>>> 
A is not True
>>> ================================ RESTART ================================
>>> 
A is not True
>>> ================================ RESTART ================================
>>> 
A is False
>>> ================================ RESTART ================================
>>> 
A is not True and not False
>>> import os
>>> files = os.listdir("c:\")
		   
SyntaxError: EOL while scanning string literal
>>> files = os.listdir('c:\')
		   
SyntaxError: EOL while scanning string literal
>>> ================================ RESTART ================================
>>> 
Enter your gross income: 84000
Enter the number of dependents: 12
Traceback (most recent call last):
  File "C:/temp/test.py", line 10, in <module>
    (DEPENDNET_DEDUCTION * numDependents)
NameError: name 'DEPENDNET_DEDUCTION' is not defined
>>> 
>>> ================================ RESTART ================================
>>> 
Enter your gross income: 84000
Enter the number of dependents: 12
The income tax is $7600.0
>>> test.py
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    test.py
NameError: name 'test' is not defined
>>> os.listdir()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    os.listdir()
NameError: name 'os' is not defined
>>> ================================ RESTART ================================
>>> 
Enter your gross income: 20000
Enter the number of dependents: 1
The income tax is $1400.0
>>> dir()
['DEPENDENT_DEDUCTION', 'STANDARD_DEDUCTION', 'TAX_RATE', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'grossIncome', 'incomeTax', 'numDependents', 'taxableIncome']
>>> help(test.py)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    help(test.py)
NameError: name 'test' is not defined
>>> test.py
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    test.py
NameError: name 'test' is not defined
>>> test
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    test
NameError: name 'test' is not defined
>>> print %__name__
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print %__name__
TypeError: unsupported operand type(s) for %: 'builtin_function_or_method' and 'str'
>>> ================================ RESTART ================================
>>> 
Enter a number5
Traceback (most recent call last):
  File "C:/temp/test.py", line 2, in <module>
    print(nmbr + 1)
TypeError: Can't convert 'int' object to str implicitly
>>> ================================ RESTART ================================
>>> 
Enter a number5
6
>>> ================================ RESTART ================================
>>> 
Help on module calendar:

NAME
    calendar - Calendar printing functions

DESCRIPTION
    Note when comparing these calendars to the ones printed by cal(1): By
    default, these calendars have Monday as the first day of the week, and
    Sunday as the last (the European convention). Use setfirstweekday() to
    set the first day of the week (0=Monday, 6=Sunday).

CLASSES
    builtins.ValueError(builtins.Exception)
        IllegalMonthError
        IllegalWeekdayError
    
    class IllegalMonthError(builtins.ValueError)
     |  # Exceptions raised for bad input
     |  
     |  Method resolution order:
     |      IllegalMonthError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, month)
     |  
     |  __str__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.ValueError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class IllegalWeekdayError(builtins.ValueError)
     |  Method resolution order:
     |      IllegalWeekdayError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, weekday)
     |  
     |  __str__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.ValueError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    calendar = formatyear(theyear, w=2, l=1, c=6, m=3) method of TextCalendar instance
        Returns a year's calendar as a multi-line string.
    
    firstweekday = getfirstweekday() method of TextCalendar instance
    
    isleap(year)
        Return True for leap years, False for non-leap years.
    
    leapdays(y1, y2)
        Return number of leap years in range [y1, y2).
        Assume y1 <= y2.
    
    month = formatmonth(theyear, themonth, w=0, l=0) method of TextCalendar instance
        Return a month's calendar string (multi-line).
    
    monthcalendar = monthdayscalendar(year, month) method of TextCalendar instance
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
    
    monthrange(year, month)
        Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
        year, month.
    
    prcal = pryear(theyear, w=0, l=0, c=6, m=3) method of TextCalendar instance
        Print a year's calendar.
    
    prmonth(theyear, themonth, w=0, l=0) method of TextCalendar instance
        Print a month's calendar.
    
    setfirstweekday(firstweekday)
    
    timegm(tuple)
        Unrelated but handy function to calculate Unix timestamp from GMT.
    
    weekday(year, month, day)
        Return weekday (0-6 ~ Mon-Sun) for year (1970-...), month (1-12),
        day (1-31).

DATA
    __all__ = ['IllegalMonthError', 'IllegalWeekdayError', 'setfirstweekda...
    day_abbr = <calendar._localized_day object>
    day_name = <calendar._localized_day object>
    month_abbr = <calendar._localized_month object>
    month_name = <calendar._localized_month object>

FILE
    c:\python34\lib\calendar.py


>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/temp/test.py", line 3, in <module>
    HTMLCalendar.formatyearpage(2015)
NameError: name 'HTMLCalendar' is not defined
>>> ================================ RESTART ================================
>>> 
<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">July 2009</th></tr>
<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td class="fri">3</td><td class="sat">4</td></tr>
<tr><td class="sun">5</td><td class="mon">6</td><td class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td></tr>
<tr><td class="sun">12</td><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td class="thu">16</td><td class="fri">17</td><td class="sat">18</td></tr>
<tr><td class="sun">19</td><td class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td class="sat">25</td></tr>
<tr><td class="sun">26</td><td class="mon">27</td><td class="tue">28</td><td class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td></tr>
</table>

>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/temp/test.py", line 9, in <module>
    f = open(os.path.realpath(filename),'w')
NameError: name 'os' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> import datetime<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">July 2009</th></tr>
<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td class="fri">3</td><td class="sat">4</td></tr>
<tr><td class="sun">5</td><td class="mon">6</td><td class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td></tr>
<tr><td class="sun">12</td><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td class="thu">16</td><td class="fri">17</td><td class="sat">18</td></tr>
<tr><td class="sun">19</td><td class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td class="sat">25</td></tr>
<tr><td class="sun">26</td><td class="mon">27</td><td class="tue">28</td><td class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td></tr>
SyntaxError: invalid syntax
>>> import datetime
>>> help(datetime)
Help on module datetime:

NAME
    datetime - Fast implementation of the datetime type.

CLASSES
    builtins.object
        date
            datetime
        time
        timedelta
        tzinfo
            timezone
    
    class date(builtins.object)
     |  date(year, month, day) --> date object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp -> local date from a POSIX timestamp (like time.time()).
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  replace(...)
     |      Return date with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  day
     |  
     |  month
     |  
     |  year
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.date(9999, 12, 31)
     |  
     |  min = datetime.date(1, 1, 1)
     |  
     |  resolution = datetime.timedelta(1)
    
    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].
     |      
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      timestamp -> UTC datetime from a POSIX timestamp (like time.time()).
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    
    class time(builtins.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |  
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Methods defined here:
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].
     |  
     |  replace(...)
     |      Return time with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.time(23, 59, 59, 999999)
     |  
     |  min = datetime.time(0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
    
    class timedelta(builtins.object)
     |  Difference between two datetime values.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  total_seconds(...)
     |      Total seconds in the duration.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  days
     |      Number of days.
     |  
     |  microseconds
     |      Number of microseconds (>= 0 and less than 1 second).
     |  
     |  seconds
     |      Number of seconds (>= 0 and less than 1 day).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.timedelta(999999999, 86399, 999999)
     |  
     |  min = datetime.timedelta(-999999999)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
    
    class timezone(tzinfo)
     |  Fixed offset from UTC implementation of tzinfo.
     |  
     |  Method resolution order:
     |      timezone
     |      tzinfo
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getinitargs__(...)
     |      pickle support
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  dst(...)
     |      Return None.
     |  
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |  
     |  tzname(...)
     |      If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'.
     |  
     |  utcoffset(...)
     |      Return fixed offset.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.timezone(datetime.timedelta(0, 86340))
     |  
     |  min = datetime.timezone(datetime.timedelta(-1, 60))
     |  
     |  utc = datetime.timezone.utc
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tzinfo:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      -> (cls, state)
    
    class tzinfo(builtins.object)
     |  Abstract base class for time zone info objects.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      -> (cls, state)
     |  
     |  dst(...)
     |      datetime -> DST offset in minutes east of UTC.
     |  
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |  
     |  tzname(...)
     |      datetime -> string name of time zone.
     |  
     |  utcoffset(...)
     |      datetime -> timedelta showing offset from UTC, negative values indicating West of UTC

DATA
    MAXYEAR = 9999
    MINYEAR = 1
    datetime_CAPI = <capsule object "datetime.datetime_CAPI">

FILE
    c:\python34\lib\datetime.py


>>> datetime.today()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    datetime.today()
AttributeError: 'module' object has no attribute 'today'
>>> print(today())
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(today())
NameError: name 'today' is not defined
>>> datetime.date.today()
datetime.date(2015, 9, 24)
>>> print(str(datetime.datetime(2008, 11, 22, 19, 53, 42)))
2008-11-22 19:53:42
>>> print( datetime.date.today())
2015-09-24
>>> print( datetime.date.today()+5)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print( datetime.date.today()+5)
TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
>>> print( datetime.date.today())
2015-09-24
>>> help(strftime)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    help(strftime)
NameError: name 'strftime' is not defined
>>> print(strftime(%A))
SyntaxError: invalid syntax
>>> print(strftime('%A'))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(strftime('%A'))
NameError: name 'strftime' is not defined
>>> today = datetime.date.today()
>>> print(today.strftime('%A'))
Thursday
>>> print(today.strftime('%A hello'))
Thursday hello
>>> print(today.strftime('%A %B %d %y'))
Thursday September 24 15
>>> print(today.strftime('%A %B %d %Y'))
Thursday September 24 2015
>>> print(today.strftime('Today is %A, %B %d %Y'))
Today is Thursday, September 24 2015
>>> 
>>> tomorrow = today+timedelta(days=1)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    tomorrow = today+timedelta(days=1)
NameError: name 'timedelta' is not defined
>>> from datetime import timedelta
>>> tomorrow = today+timedelta(days=1)
>>> tomorrow
datetime.date(2015, 9, 25)
>>> print tomorrow
SyntaxError: Missing parentheses in call to 'print'
>>> print(tomorrow)
2015-09-25
>>> ================================ RESTART ================================
>>> 
2008-11-22 19:53:42
2015-09-24
Today is a Thursday
Thursday September 24 2015
Today is Thursday, September 24 2015
Traceback (most recent call last):
  File "C:/temp/test.py", line 28, in <module>
    d = datetime.strptime('2011-03-05','%Y-%m-%d')
AttributeError: 'module' object has no attribute 'strptime'
>>> ================================ RESTART ================================
>>> 
2008-11-22 19:53:42
2015-09-24
Today is a Thursday
Thursday September 24 2015
Today is Thursday, September 24 2015
2011-03-05 00:00:00
2011-03-06 00:00:00
>>> import openpyxl
>>> help(openpyxl)
Help on package openpyxl:

NAME
    openpyxl - Imports for the openpyxl package.

PACKAGE CONTENTS
    cell (package)
    charts (package)
    comments (package)
    compat (package)
    conftest
    descriptors (package)
    drawing (package)
    formatting (package)
    reader (package)
    styles (package)
    utils (package)
    workbook (package)
    worksheet (package)
    writer (package)
    xml (package)

DATA
    LXML = False
    __author_email__ = 'eric.gazoni@gmail.com'
    __license__ = 'MIT/Expat'
    __maintainer_email__ = 'openpyxl-users@googlegroups.com'
    __url__ = 'http://openpyxl.readthedocs.org'

VERSION
    2.2.6

AUTHOR
    Eric Gazoni

FILE
    c:\python34\lib\site-packages\openpyxl\__init__.py


>>> xml (package)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    xml (package)
NameError: name 'xml' is not defined
>>> print z
SyntaxError: Missing parentheses in call to 'print'
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> z
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> name
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = input('enter your name')
enter your namedave
>>> name
'dave'
>>> print(name)
dave
>>> name = input('enter your name: ')
enter your name: Bart Simpson
>>> name
'Bart Simpson'
>>> int(name)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'Bart Simpson'
>>> three
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    three
NameError: name 'three' is not defined
>>> three = int(3)
>>> three
3
>>> three + 4
7
>>> print "I will not chew gum in class"
SyntaxError: Missing parentheses in call to 'print'
>>> print ("I will not chew gum in class")
I will not chew gum in class
>>> print ('I will not chew gum in class')
I will not chew gum in class
>>> print ('I will not chew gum in class') * 100
I will not chew gum in class
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print ('I will not chew gum in class') * 100
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> print ('I will not chew gum in class' * 100)
I will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in classI will not chew gum in class
>>> print ('I will not chew gum in class\n' * 100)
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class

>>> i=0
>>> print (i++ + 'I will not chew gum in class\n' * 100)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print (i++ + 'I will not chew gum in class\n' * 100)
TypeError: bad operand type for unary +: 'str'
>>> print (str(i++) + 'I will not chew gum in class\n' * 100)
SyntaxError: invalid syntax
>>> print (str(i +=1) + 'I will not chew gum in class\n' * 100)
SyntaxError: invalid syntax
>>> print ('I will not chew gum in class\n' * 100)
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class

>>> for eachPass in range(4):
	print("It's alive!", end="")
	i += 1
	print str(i) + '\n'
	
SyntaxError: invalid syntax
>>> for eachPass in range(4):
	print("It's alive!", end="")
	i += 1

It's alive!It's alive!It's alive!It's alive!
>>> for eachPass in range(4):
	print("It's alive!", end="\n\n\n")
	i += 1

	
It's alive!


It's alive!


It's alive!


It's alive!


>>> for eachPass in range(4):
	print("It's alive!", end=" ")

	
It's alive! It's alive! It's alive! It's alive! 
>>> number = 2
>>> exponent = 3
>>> product = 1
>>> for eachPass in range(exponent):
	product = product * number
	print(product, end=' ')

	
2 4 8 
>>> exponent = 14
>>> for eachPass in range(exponent):
	product = product * number
	print(product, end=' ')

	
16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 
>>> exponent = 128
>>> for eachPass in range(exponent):
	product = product * number
	print(product, end=' ')

	
262144 524288 1048576 2097152 4194304 8388608 16777216 33554432 67108864 134217728 268435456 536870912 1073741824 2147483648 4294967296 8589934592 17179869184 34359738368 68719476736 137438953472 274877906944 549755813888 1099511627776 2199023255552 4398046511104 8796093022208 17592186044416 35184372088832 70368744177664 140737488355328 281474976710656 562949953421312 1125899906842624 2251799813685248 4503599627370496 9007199254740992 18014398509481984 36028797018963968 72057594037927936 144115188075855872 288230376151711744 576460752303423488 1152921504606846976 2305843009213693952 4611686018427387904 9223372036854775808 18446744073709551616 36893488147419103232 73786976294838206464 147573952589676412928 295147905179352825856 590295810358705651712 1180591620717411303424 2361183241434822606848 4722366482869645213696 9444732965739290427392 18889465931478580854784 37778931862957161709568 75557863725914323419136 151115727451828646838272 302231454903657293676544 604462909807314587353088 1208925819614629174706176 2417851639229258349412352 4835703278458516698824704 9671406556917033397649408 19342813113834066795298816 38685626227668133590597632 77371252455336267181195264 154742504910672534362390528 309485009821345068724781056 618970019642690137449562112 1237940039285380274899124224 2475880078570760549798248448 4951760157141521099596496896 9903520314283042199192993792 19807040628566084398385987584 39614081257132168796771975168 79228162514264337593543950336 158456325028528675187087900672 316912650057057350374175801344 633825300114114700748351602688 1267650600228229401496703205376 2535301200456458802993406410752 5070602400912917605986812821504 10141204801825835211973625643008 20282409603651670423947251286016 40564819207303340847894502572032 81129638414606681695789005144064 162259276829213363391578010288128 324518553658426726783156020576256 649037107316853453566312041152512 1298074214633706907132624082305024 2596148429267413814265248164610048 5192296858534827628530496329220096 10384593717069655257060992658440192 20769187434139310514121985316880384 41538374868278621028243970633760768 83076749736557242056487941267521536 166153499473114484112975882535043072 332306998946228968225951765070086144 664613997892457936451903530140172288 1329227995784915872903807060280344576 2658455991569831745807614120560689152 5316911983139663491615228241121378304 10633823966279326983230456482242756608 21267647932558653966460912964485513216 42535295865117307932921825928971026432 85070591730234615865843651857942052864 170141183460469231731687303715884105728 340282366920938463463374607431768211456 680564733841876926926749214863536422912 1361129467683753853853498429727072845824 2722258935367507707706996859454145691648 5444517870735015415413993718908291383296 10889035741470030830827987437816582766592 21778071482940061661655974875633165533184 43556142965880123323311949751266331066368 87112285931760246646623899502532662132736 174224571863520493293247799005065324265472 348449143727040986586495598010130648530944 696898287454081973172991196020261297061888 1393796574908163946345982392040522594123776 2787593149816327892691964784081045188247552 5575186299632655785383929568162090376495104 11150372599265311570767859136324180752990208 22300745198530623141535718272648361505980416 44601490397061246283071436545296723011960832 
>>> exponent = 0
>>> for eachPass in range(exponent):
	product = product * number
	print(product, end=' ')

	
>>> for count in range(4):
	print(count, end = " ")

	
0 1 2 3 
>>> for count in range(4):
	print(count)

	
0
1
2
3
>>> for count in range(1,4):
	print(count)

	
1
2
3
>>> for count in range(-10,4):
	print(count)

	
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
>>> 
