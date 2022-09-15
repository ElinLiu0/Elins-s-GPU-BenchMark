#Author: Elin.Liu
# Date: 2022-09-14 18:52:39
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 18:52:39
import onnxmltools
from onnxmltools.utils.float16_converter import convert_float_to_float16

onnx_model = onnxmltools.load_model('../module/models/model.onnx')
onnx_model_fp16 = convert_float_to_float16(onnx_model)
onnxmltools.utils.save_model(onnx_model_fp16, '../module/models/model_fp16.onnx')