from keras.models import Sequential
from keras.layers import Dense
from code.parser import Collection


def main():
	collection = Collection()
	x_train, y_train = collection._divide()
	model = Sequential()
	model.add(Dense(units = 64, activation = 'relu', input_dim = 100))
	model.add(Dense(units = 10, activation = 'softmax'))

	model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])

	model.fit(x_train, y_train, epochs = 5, batch_size = 32)
	loss_and_metrics = model.evaluate(x_train, y_train, batch_size = 128)


if __name__ == '__main__':
	main()
