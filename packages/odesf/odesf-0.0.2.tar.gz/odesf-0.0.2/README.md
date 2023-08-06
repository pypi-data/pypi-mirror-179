# String format function of ODEs
This package provides a simple function - transform a list of ODEs in string format into a string of a function in Python/C++.

Examples are as follows.

## For python

To transform a list of ODE strings into function string format:

- the left hand side must be written with derivitive form `d()/d()`
```python
from odesf import eq_to_pyfunc_string

stiff_equation = ['dy/dt = z + t',
                  'dz/dt = -100 * y * t']

funcstr = eq_to_pyfunc_string(stiff_equation)

print(funcstr)

>> "def func(_x_, _y_, _f_): _f_[0] = _y_[1] + _x_; _f_[1] = -100 * _y_[0] * _x_;"
```



If constants exist, a list of constant equations must be passed over:

- The constant variable name at the left hand side must be the same as in ODE strings
```python
from odesf import eq_to_pyfunc_string

lorenz_equation_strs = ['dx/dt = sigma * (y - x)',
                        'dy/dt = rho * x - y - x * z',
                        'dz/dt = x * y - beta * z']

lorenz_constants = ['sigma = 10e0',
                    'rho = 28e0',
                    'beta = 8e0 / 3e0']

funcstr = eq_to_pyfunc_string(lorenz_equation_strs, lorenz_constants)

print(funcstr)

>> "def func(_x_, _y_, _f_): sigma = 10e0; rho = 28e0; beta = 8e0 / 3e0;  _f_[0] = sigma * (_y_[1] - _y_[0]); _f_[1] = rho * _y_[0] - _y_[1] - _y_[0] * _y_[2]; _f_[2] = _y_[0] * _y_[1] - beta * _y_[2];"

```



## For C++

Unlike for python, the result is a tuple:

- function string in `.cpp` format
- function head string in `.h` format

```python
from odesf import eq_to_cfunc_string

stiff_equation = ['dy/dt = z + t',
                  'dz/dt = -100 * y * t']

funcstr, funch = eq_to_cfunc_string(stiff_equation)

print(funcstr)
print(funch)

>> "Function str: void template_func(double _x_, double _y_[], double _f_[]) { _f_[0] = _y_[1] + _x_; _f_[1] = -100 * _y_[0] * _x_; }"
>> "Head str:  void template_func(double _x_, double _y_[], double _f_[]);"
```

