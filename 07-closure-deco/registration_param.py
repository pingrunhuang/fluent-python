"""
>>> import registration_param 
running register(active=False)->decorate(<function f1 at 0x10063c1e0>)
running register(active=True)->decorate(<function f2 at 0x10063c268>)


meaning at import time, python will run the code inside the decorator since we called it 
"""

# BEGIN REGISTRATION_PARAM

registry = set()  # <1>

def register(active=True):  # <2>
    def decorate(func):  # <3>
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:   # <4>
            registry.add(func)
        else:
            registry.discard(func)  # <5>

        return func  # <6>
    return decorate  # <7>

@register(active=False)  # <8>
def f1():
    print('running f1()')

@register()  # <9>
def f2():
    print('running f2()')

def f3():
    print('running f3()')

# END REGISTRATION_PARAM
