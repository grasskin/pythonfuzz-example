from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import struct

from pythonfuzz.main import PythonFuzz
from module import math

assert math.add(1, 1) == 2
assert math.subtract(1, 1) == 0

# Lint as: python3

@PythonFuzz
def decode_image_fuzz(buff):
    size = len(buff)
    if size < 1:
    	return
    num = int.from_bytes(buff, "big") % 10000
    math.add(num, num)

decode_image_fuzz()
