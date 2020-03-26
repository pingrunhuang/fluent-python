Sample code for Chapter 15 - "Context managers and something else"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

The variable after the the as is a reference to what `__enter__` method will return 

the arguments of the __exit__ method are `__exit__(self, exc_type, exc_value, traceback)`

# How contextmanager works
everything before the `yield` statetment will be executed in the `__enter__`block
everything after it will be executed in the `__exit__` block 

