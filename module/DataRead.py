#Author: Elin.Liu
# Date: 2022-09-14 16:13:12
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 16:13:12
import time
import cudf as cf


def ReadData():
    print("Reading Data From Already Prepared...")
    start = time.time()
    df = cf.read_csv("./data/data.csv")
    if df.shape[0] > 0:
        end = time.time()
        print("Done! Start Next Step...")
        return df.shape,end - start
    else:
        raise Exception("Data is not readable!")
