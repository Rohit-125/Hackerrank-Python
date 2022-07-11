#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    z = Counter(s)
#   print(z)
    z = Counter(s).most_common(3)
#   print(z)
    for x in z:
        print(*x)
