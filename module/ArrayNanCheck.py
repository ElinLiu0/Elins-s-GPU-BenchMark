#Author: Elin.Liu
# Date: 2022-09-14 16:17:15
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 16:17:15
import cupy as cp
import time


def ArrayNanCheck():
    print("Generating Array...")
    start = time.time()
    array = cp.random.randint(0, 2, (10000, 10000))
    print("Checking Array...")
    result = cp.nonzero(array)
    if result:
        end = time.time()
        print("Done! Start Next Step...")
        return (10000, 10000), end - start
    else:
        raise Exception("Array is not readable!")
