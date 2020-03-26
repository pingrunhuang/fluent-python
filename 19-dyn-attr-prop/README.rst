Sample code for Chapter 19 - "Dynamic attributes and properties"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# Variable naming
1. suffix _ to variable name to prevent reserved word
2. prefix _ to avoid naming like starting with number (str.isidentifier() method is used to tell if it is usable)



Use case of property decorator

property(fget=None, fset=None, fdel=None, doc=None)

value validation

fget, fset, fdel are functions that take only one argument which is the instance

statement like obj.attr will start at obj.__class__, only if there is no property named attr, will python looks at obj instance


Special Attributes:
__class__
__dict__
__slots__

Attribute handling:
    Built-in
        dir 
        getattr
        setattr
        hasattr
        vars
    Class method:
        __delattr__(self, name)
        __dir__(self)
        __getattr__(self, name)
        __getattribute__
        __setattr__





