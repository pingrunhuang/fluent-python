"""
Example of property documentation

    >>> f = Foo()
    >>> f.bar = 77
    >>> f.bar
    77
    >>> Foo.bar.__doc__
    'The bar attribute'
"""

# BEGIN DOC_PROPERTY
class Foo:

    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value
# END DOC_PROPERTY


class Class:
    """
    >>> obj = Class()
    >>> vars(obj)
    {}
    >>> obj.data
    'the class data attr'
    >>> obj.data = "bar"
    >>> vars(obj)
    {'data': 'bar'}
    >>> obj.data
    'bar'
    >>> Class.data # did not change the class property
    'the class data attr'
    >>> obj.prop = "foo" # try to assign new value to property will fail
    AttributeError: can't set attribute
    >>> obj.__dict__['prop'] = 'foo' 
    >>> vars(obj) # vars return __dict__, so this works 
    {'prop': 'foo', 'attr': 'bar'} 
    >>> obj.prop # but the instance property still return the class property
    'the prop value'
    >>> Class.prop = 'baz' # this will destroy the property
    >>> obj.prop  # since class property is destroyed, therefore the instance property will be returned  
    'foo'
    """
    data = "the class data attr"
    @property
    def prop(self):
        return "the prop value"



