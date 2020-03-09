Sample code for Chapter 7 - "Closures and decorators"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do


# variable scopes demonstration.rst
In the code snippet of f2, we can see the process of running f2:
1. python compiles the code first and determine b is local
2. at run time, python could not find the local variable b which throw error
3. to solve this, key word `global` is introduced

# `from dis import dis`, disassembly is used to check the function excecution plan

# closure

A closure is function, that has non global variables in the extended scope. These variables are `referenced`
in the body of the function but not defined in the function.

- get function name by using `__name__` variable

# decorator can accept parameters
good example could be the functools.lru_cache
- decorator with parameters: function that return inner function which is the real decorator
- decorator only do extra operations: function that return the original function
- essentially, adding parameters to decorator require stacking one more level function

- functools.singledispatch is used to do function overloading in python (check out generic.py)

- locals() return a dictionary of all local variables 

