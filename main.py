#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    N = len(petrolpumps)
    start, passed, gas = 0, 0, 0
    i = 0
    while passed < N:
        gas += petrolpumps[i][0] - petrolpumps[i][1]
        if gas < 0:
            # The correct starting point, if exists, cannot be anything between 'start'
            # and the current point. Because we checked every interval beginning with
            # 'start' and ending before while having a non-negative cumulative sum. So,
            # if we started anywhere there, the cumulative sum would have been even less
            # than now which is already negative. Therefore, the correct starting point
            # can only be found ahead.
            start += passed + 1
            passed, gas = 0, 0
        else:
            passed += 1
        i = (i + 1) % N

        # Check if there is no solution -> negative loop
        if start >= N:
            return -1
    return start


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f, open(os.environ["OUTPUT_PATH"], "w") as fptr:
        n = int(f.readline().strip())

        petrolpumps = []

        for _ in range(n):
            petrolpumps.append(list(map(int, f.readline().rstrip().split())))

        result = truckTour(petrolpumps)

        fptr.write(str(result) + "\n")
