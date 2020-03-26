Sample code for Chapter 14 - "Iterables, iterators and generators"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

Implementing __iter__ can make an object iterable. 
Also, __getitem__ can make the object iterable. 
Sequence is iterable because it implement __getitem__. 

# Better way to check iterable
```
try:
    iter(x)
except TypeError:
    # handle here
```
because implementing __getitem__ can also make it iterable


Iterators implement __next__ and __iter__ return self
Iterables implement __iter__. So Iterator is iterable but not the other way.


re.finditer is a generator version of re.findall method

# Some interesting built-in generator

- os.walk: traverse the directory tree and yield as generator

### itertools
- itertools.takewhile(predicate, it): iter until predicate met
- itertools.compress(it, selector_it): only yield items in it that is true in selector_it
- iterators.islice(): generator version of list slicing

- itertools.starmap(func, it): like map, but the item of it is an iterable so that func is applied as func(*item)
- itertools.accumulate(func, it): apply func on it pairs by pairs, accumulate the result for each pair
- enumerate(it, start=0): return tuple of (index, value), specify the first index in start


running average:
x =  [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

