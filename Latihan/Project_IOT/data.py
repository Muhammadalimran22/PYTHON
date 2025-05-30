# import numpy as np

# # Membaca file .npy
# data = np.load('sample_0_20241203_220204.npy')

# # Menampilkan data yang dimuat
# print(data)


# import tensorflow as tf

# # Memuat model yang disimpan dengan ekstensi .keras
# model = tf.keras.models.load_model('sound_recognition_model.keras')

# # Menampilkan ringkasan model
# model.summary()


import tensorflow as tf

# Muat model
model = tf.keras.models.load_model('sound_recognition_model.keras')  # Ganti dengan model .h5 atau .keras

# Konversi model ke TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Simpan model TFLite ke file
with open('sound_recognition_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model successfully converted to TensorFlow Lite!")
