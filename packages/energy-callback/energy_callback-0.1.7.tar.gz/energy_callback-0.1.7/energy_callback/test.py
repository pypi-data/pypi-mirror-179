import tensorflow as tf
import datetime
import energy_callback


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])


model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

callback = energy_callback.Callback()

history = model.fit(x=x_train,
          y=y_train,
          epochs=2,
          validation_data=(x_test, y_test),
          callbacks=[tensorboard_callback, callback])


print(history)
print(history.params)
print(history.history.keys())
print(history.history['duration'])
print(callback.get_joules(), callback.get_co2e())
callback.get_csv(history)

