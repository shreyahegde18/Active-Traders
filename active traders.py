#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    from collections import defaultdict
    
    c=defaultdict(int)
    for i in customers:
        c[i] +=1
    return sorted([i for i, cnt in c.items() if cnt/len(customers) >=0.05])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
