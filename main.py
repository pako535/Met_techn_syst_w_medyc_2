# from keras.models import Sequential
# from keras.layers import Dense
# from code.parser import Collection
#
#
# def main():
# 	collection = Collection()
# 	x_train, y_train = collection._divide()
# 	model = Sequential()
# 	model.add(Dense(units = 64, activation = 'relu', input_dim = 100))
# 	model.add(Dense(units = 10, activation = 'softmax'))
#
# 	model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
#
# 	model.fit(x_train, y_train, epochs = 5, batch_size = 32)
# 	loss_and_metrics = model.evaluate(x_train, y_train, batch_size = 128)
#
#
# if __name__ == '__main__':
# 	main()

import tensorflow as tf
import matplotlib.pyplot as plt
# from code.parser import Collection
# from sklearn.model_selection import train_test_spli
#


# split into 67% for train and 33% for test
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)
# mnist = tf.keras.datasets.mnist
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(type(x_train), type(x_test))
# x_train = tf.keras.utils.normalize(x_train, axis = 1)
# x_test = tf.keras.utils.normalize(x_test, axis = 1)
# plt.imshow(x_train[0])
#
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu, use_bias = True, bias_initializer = 'zeros'))
# model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu, use_bias = True, bias_initializer = 'zeros'))
# model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
#
# model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
# model.fit(x_train, y_train, epochs = 5)
#
# val_loss, val_acc = model.evaluate(x_test, y_test)
# print(val_loss, val_acc)
#
# model_2 = tf.keras.models.Sequential()
#
# model.summary()

from code.parser import Collection

coll = Collection()

Y = coll.headers
print(coll.excel_data.shape)
