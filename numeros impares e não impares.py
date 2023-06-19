import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    m = n % 2
    if m != 0:
        print("Weird")
    elif 6 <= n <= 20:
        m == 0
        print('Weird')
    elif m == 0:
        print("Not Weird")