from array import array
from random import random

num_objs = 10 ** 7
floats = array('d', (random() for _ in range(num_objs)))

with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)

input_floats = array('d')
with open("floats.bin", 'rb') as fp:
    input_floats.fromfile(fp, num_objs)

assert floats[-1] == input_floats[-1]

