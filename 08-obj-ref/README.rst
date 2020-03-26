Sample code for Chapter 8 - "Object references, mutability and recycling"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do


object has 3 required info: address, value and type


# Choosing between == and is
- `==` is value comparing based. `__eq__()` is invoked.

- `is` is address or id comparing based. `id()` is invoked.

# copies
shallow copies 
    1. l2 = list(l1) where l1 is a list
    2. l2 = l1[:]

__copy__()
__deepcopy__()

function can change mutable parameter but not immutable parameter

mutable parameter as default parameter may cause trouble because once mutable parameters
get changed, default value get change for every future call   


list and dict can not be referent but their sub class can

# weakref collections
- WeakValueDictionary
- WeakKeyDictionary
- WeakSet
- finalize
Essentially speaking, these tools are used when we want to keep a reference to an object but not increasing 
the number of reference count by itself.


www.pythontutor.com/
