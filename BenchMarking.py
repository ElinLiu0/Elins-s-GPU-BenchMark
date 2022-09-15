#Author: Elin.Liu
# Date: 2022-09-14 20:25:06
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 20:25:06

from module.ArrayConvert import ArrayConvert
from module.VGGFullPrecision import VGGFullPrecision
from module.ArrayNanCheck import ArrayNanCheck
from module.VGGHalfPrecision import VGGHalfPrecision
from module.DataRead import ReadData
from pynvml import *


def main():
    print("Start Benchmarking...")
    nvmlInit()
    deviceGPUName = nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(0))

    print("Initialized With GPU Model: " + str(deviceGPUName))
    print("Starting ArrayConvert...")
    ArraySize1, ArrayConvertTiming = ArrayConvert()
    print("Starting Array Nan Check...")
    ArraySize2, ArrayNanCheckTiming = ArrayNanCheck()
    print("Starting Data Read...")
    DataSize1, DataReadTiming = ReadData()
    print("Starting VGG Full Precision...")
    DataSize2, VGGFullPrecisionTiming, Connections = VGGFullPrecision()
    print("Starting VGG Half Precision...")
    DataSize3, VGGHalfPrecisionTiming, Connections = VGGHalfPrecision()
    with open("./result/BenchMarkingResult.txt", "w") as f:
        f.write(f"---------------------------------------------------------\n")
        f.write("Device Information:\n")
        f.write(f"\tGPU Model: {deviceGPUName}\n")
        f.write(
            f"\tGPU Memory: {nvmlDeviceGetMemoryInfo(nvmlDeviceGetHandleByIndex(0)).total / 1024 / 1024 / 1024} GB\n")
        f.write(
            f"\tGPU Computue Capability: {nvmlDeviceGetCudaComputeCapability(nvmlDeviceGetHandleByIndex(0))[0]}\n")
        f.write("----------------------\n")
        f.write("Benchmarking Results:\n")
        f.write("----------------------\n")
        f.write("Array Convert:\n")
        f.write(f"\tArray Size: {ArraySize1}\n")
        f.write(f"\tArrayConvert Timing: {ArrayConvertTiming} Seconds\n")
        f.write("----------------------\n")
        f.write("Array Nan Check:\n")
        f.write(f"\tArray Size: {ArraySize2}\n")
        f.write(f"\tArrayNanCheck Timing: {ArrayNanCheckTiming} Seconds\n")
        f.write("----------------------\n")
        f.write("Data Read:\n")
        f.write(f"\tData Size: {DataSize1}\n")
        f.write(f"\tDataRead Timing: {DataReadTiming} Seconds\n")
        f.write("----------------------\n")
        f.write("VGG Full Precision:\n")
        f.write(f"\tData Size: {DataSize2}\n")
        f.write(
            f"\tVGGFullPrecision Timing: {VGGFullPrecisionTiming} Seconds\n")
        f.write(f"\tConnections: {Connections}\n")
        f.write("----------------------\n")
        f.write("VGG Half Precision:\n")
        f.write(f"\tData Size: {DataSize3}\n")
        f.write(
            f"\tVGGHalfPrecision Timing(In TensorRT): {VGGHalfPrecisionTiming} Seconds\n")
        f.write(f"\tConnections: {Connections}\n")
        f.write("----------------------\n\n")

        f.write("Benchmarking Finished!")
    print("Result Generated!Checkout ./result/BenchMarkingResult.txt")


if __name__ == "__main__":
    main()
