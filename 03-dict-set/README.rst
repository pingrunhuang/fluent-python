Sample code for Chapter 3 - "Dictionaries and sets"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

__missing__() behind the scene of defaultdict

collections.OrderedDict
collections.ChainMap
collections.Counter
collections.UserDict


# Set infix operation
In [1]: a = {'asd', 'qwe', 'zzz'}

In [2]: b = {'asd', 'qwe', 'z'}

In [3]: a-b
Out[3]: {'zzz'}

In [4]: a&b
Out[4]: {'asd', 'qwe'}

In [5]: a|b
Out[5]: {'asd', 'qwe', 'z', 'zzz'}


overwrite `__eq__` requrires define `__hash__` as well

if a == b then hash(a) == hash(b)


* `dialcodes.py` demonstrate that even the keys are in different orders, the dictionaries 
are equal only because they contains same (key, value).


* the difference between subclassing from `UserDict` and `dict` is the previous one has builtin
method of `update` and `get` which could be used directly without rewriting it.

* from types import MappingProxyType 
- to create a view of an existing dict which could not be modified

* use FrozenSet for set to be immutable

* dict and set are fast, unordered and will reorder while adding new items

