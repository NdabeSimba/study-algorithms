
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    line = s.split()

    for i in range(len(line)):
        line[i][0].upper()

    return line


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
