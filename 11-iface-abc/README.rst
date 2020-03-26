Sample code for Chapter 11 - "Interfaces, protocols and ABCs"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# Different protocols
1. sequence protocol

mutable item should implement __setitem__()
only __getitem__() means immutable

iterable: __iter__(), __getitem__()
container(is in): __contains__(), __getitem__()


