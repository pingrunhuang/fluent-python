import weakref

s1 = {1,2,3}
s2 = s1

def bye():
    print("SET IS GARBAGE COLLECTED")

ref = weakref.finalize(s1, bye)

del s1 # delete first reference
print(ref.alive)
del s2 # delete second reference trigger the callback, modify s2 referencing is also ok

print(ref.alive)


a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref())
a_set = {2,3,4}
print(wref())

