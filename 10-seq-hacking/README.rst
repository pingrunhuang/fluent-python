Sample code for Chapter 10 - "Sequence hacking, hashing and slicing"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# awesome lib
- reprlib

# slicing
when we use `array[1:]` syntax, we are actually passing a slice object into the `__getitem__` method.



__getattr__ is invoked when the named attribute is not found. obj.x  
__setattr__ is invoded when the named attribute is being set. obj.x = 1  
they should come together and calling super().__setattr__() to make it consistent.


itertools.zip_longest with fill value  


1. __getitem__ (for iteration) and __len__ to form a sequence (which is called protocol or duck typing aka determined by the methods not by the type)
2. __getattr__ and __setattr__ for customized attribute manipulation
3. __hash__ and __eq__ for comparison
4. __format__ to be used by format() function 

