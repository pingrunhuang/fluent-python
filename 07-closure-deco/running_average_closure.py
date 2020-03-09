"""
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__  # doctest: +ELLIPSIS
(<cell at 0x...: list object at 0x...>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

DEMO = """
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
"""


def make_averager():
    series = []

    def averager(new_value:'float > 0'=0)->float:
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

def make_averager_v2():
    """
    UnboundLocalError: local variable 'total' referenced before assignment

    modifying number or immutable object in closure is not allowed (list is mutable) 
    """
    total = 0
    num = 0
    def averager(new_value):
        total += new_value
        num += 1
        return total / num
    return averager

def make_averager_v3():
    """
    this is why we need the nonlocal keyword
    """
    total = 0 
    num = 0
    def averager(new_value):
        nonlocal total, num
        total += new_value
        num += 1
        return total / num
    return averager


if __name__ == "__main__":
    avg = make_averager_v3()
    print(avg(10))
    print(avg(11))