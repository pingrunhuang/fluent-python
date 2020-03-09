Sample code for Chapter 5 - "First-class functions"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

7 callable objects:
1. user-defined functions
2. built-in functions
3. built-in methods (dict.get)
4. methods
5. classes
6. class instances
7. generator functions

#### Key word only argument
>>> def f(a, *, b):
...     return a, b
>>> f(1, b=2)


#### higher order functions
- operator.mul
- operator.itemgetter
- operator.attrgetter
- operator.methodcaller: generate a function object that can call the method of a given argument
- functools.partial: 

##### function declaration with types
``def func(text:str, max_len:'int > 0'=80) -> str: pass``

