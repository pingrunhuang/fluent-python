Sample code for Chapter 17 - "Concurrency with futures"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do


For threading: use concurrent.futures.ThreadPoolExecutor
For multiprocessing: use concurrent.futures.ProcessPoolExecutor


Because CPython interpreter is not thread-safe, so python has GIL to ensure only one thread
is used. However, I/O bound operation utilizing the built-in function or extension written in
C can release the GIL.


