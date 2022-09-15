#Author: Elin.Liu
# Date: 2022-09-14 18:06:46
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 18:06:46
import os
import onnxruntime as ort
from PIL import Image
import numpy as np
import time

_MODEL_NEURONS = 14716227


def VGGHalfPrecision():
    print("Detecting ONNX Model...")
    start_time = time.time()
    model_path = './module/models/model_fp16.onnx'
    print("Generating Session...")
    providers = [
        ('CUDAExecutionProvider', {
            'device_id': 0,
            'arena_extend_strategy': 'kNextPowerOfTwo',
            'gpu_mem_limit': 2 * 1024 * 1024 * 1024,
            'cudnn_conv_algo_search': 'EXHAUSTIVE',
            'do_copy_in_default_stream': True,
        }),
        'CPUExecutionProvider',
    ]

    session = ort.InferenceSession(model_path, providers=providers)

    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    fileCount = 0
    for root, path, files in os.walk("./data/valid"):
        fileCount = 0
        for i in files:
            image = Image.open(os.path.join(root, i))
            image = np.copy(image)
            image = np.resize(image, (1, 224, 224, 3))
            result = session.run(
                [output_name], {input_name: image.astype(np.float16)})[0]
            fileCount += 1
    end_time = time.time()
    print("Done! Start Next Step...")
    return fileCount, end_time - start_time, _MODEL_NEURONS * fileCount
