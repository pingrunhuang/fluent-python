Sample code for Chapter 16 - "Coroutines"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

use inspect.getgenerateorstate() to get the status of a coroutine:
GEN_CREATED
GEN_RUNNING
GEN_PENDING
GEN_CLOSED


The first call of next() to the coroutine is called priming.

# Question: Do you know the coroutine in python needs to be primed so that client can send value
into it? How to write a decorator to eliminate this step?

```
from functools import wraps

def couroutine(func):
    @wraps(func)
    def inner(*args, **kwargs):
        cor = func(*args, **kwargs)
        res = next(cor)
        return res
    return inner
```
essentially, this wrapper advance the first yield.


# Exception handling: yield from <subgenerator>

`yield from` is equivelant to `await` in other language but with iterable variable(could be 
itertable)



coorperative multitasking: coroutine
preemptive multitasking: threads



http://seriously.dontusethiscode.com/2013/05/01/greedy-coroutine.html
https://www.zopatista.com/python/2013/11/26/inplace-file-rewriting/
http://www.dabeaz.com/generators/
