from collections import UserDict

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)


class DoppelDict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)



if __name__ == "__main__":
    dd = DoppelDict(one=1)
    print(dd) # get ignore by __init__
    dd.update('three'=3)
    print(dd) # get ignore by __update__

    '''using UserDict'''
    

