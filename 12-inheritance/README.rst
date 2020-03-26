Sample code for Chapter 12 - "Inheritance: for good or for worse"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

- don't subclass from multiple concrete class
- aggregate many ABCs or mixins that are used together a lot into one empty class
    ```python 
    class Widget(BaseWidget, Pack, Place, Grid):
        pass
    ```


