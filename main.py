# importing libraies
import onnx
import tf2onnx
import tensorflow as tf
from tensorflow.keras.models import load_model


# loading and saving models models
loaded_cnn = load_model("Models/FunctionalAPI_CNN.h5")
tf.saved_model.save(loaded_cnn, "./tmp_model")

