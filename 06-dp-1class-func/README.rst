Sample code for Chapter 6 - "Design patterns with first class functions"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# Difference between strategy_best2.py and strategy_best3.py
- use globals() to get the promotions function in current module
- use inspect to get the promotion functions in another seperate module called promotions

# Difference between strategy_best.py and strategy_best2.py
- provide fixed list of strategy
- load dynamically from current module

# Command pattern

similar to callback function, could instantiate a callable object (contains __call__ method)


