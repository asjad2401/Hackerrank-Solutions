#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    desc_sum = [0]
    zero_counts = [0]  # Stores the count of zeros for each prefix sum range
    for num in numbers:
        desc_sum.append(desc_sum[-1] + num)
        zero_counts.append(zero_counts[-1] + (num == 0))

    # Process queries
    sums = []
    for query in queries:
        left_idx = query[0] - 1
        right_idx = query[1]
        sumi = desc_sum[right_idx] - desc_sum[left_idx] + (zero_counts[right_idx] - zero_counts[left_idx]) * query[2]
        sums.append(sumi)
    
    return sums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
