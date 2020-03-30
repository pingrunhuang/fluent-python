Sample code for Chapter 20 - "Attribute descriptors"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

use descriptors to prevent value error such as price negative


Descriptor class: class implementing descriptor protocol

Managed class: class containing instance of descriptor class as attribute

Descriptor instance: 

Managed instance: 

Storage attribute: 

Relationship between managed and descriptor is aggregation



# pattern for a descriptor
```python
class Descriptor:
    def __init__(self, id_val):
        self.id_val = id_val
    def __set__(self, instance, val):
        # special manipulation here
        pass
    def __get__(self):
        pass

```
the overriding `__set__()` method of a descriptor class is noted at page 630

`managed class`: a class that has the descriptor's instance as an attribute 
`storage attribute`: an attribute of the instance of the managed class
`managed attribue`: class attribute

onething to notice here, in order to avoid mannually typing the id_val which will cause future fault typo, 
we could use a class attribute counter as the automatic incrementing id.

```python
class Descriptor:
    __counter = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.id_val = "_{}#{}".format(prefix, index)
        self.counter += 1
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass 
```
could use getattr or instance.__dict__ to get the value corresponding to the target class attribute

owner is the managed class, instance is the instance of the managed class

