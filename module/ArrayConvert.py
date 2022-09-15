#Author: Elin.Liu
# Date: 2022-09-14 16:24:04
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 16:24:04

import time
import cupy as cp


def ArrayConvert():
    print("Generating Array...")
    start = time.time()
    arrayA = cp.random.randint(0, 2, (10000, 10000))
    print("Converting Array...")
    arrayA = arrayA.T
    end = time.time()
    print("Done! Start Next Step...")
    return (10000, 10000), end - start
