#Author: Elin.Liu
# Date: 2022-09-14 18:15:12
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 18:15:12

import tensorflow as tf

model_path = './models/model.h5'                    # 模型文件
model = tf.keras.models.load_model(model_path)
model.save('tfmodel', save_format='tf')
