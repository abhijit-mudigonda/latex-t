import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

model = Sequential()

model.add(Dense(output_dim=64,input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax")


model.compile(loss='categorical_crossentropy',optimizer=SGD(lr=0.01,momentum=0.9,nesterov=True))

model.fit(X_train,Y_train,nb_epoch=5,batch_size=32)


