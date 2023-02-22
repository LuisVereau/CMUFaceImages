import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import models, layers
from random import randint
from sklearn.model_selection import train_test_split

def trainModel(X_train_arr, y_train_arr):
    rand_seed = randint(0, 10000)

    X_train, X_val, y_train, y_val = train_test_split(X_train_arr, y_train_arr, test_size=0.25, random_state=rand_seed)

    # Hiperparameters
    learning_rate = 0.001
    input_dim = (X_train[0].shape)
    output_num = len(np.unique(y_train))
    max_epochs = 25

    model = models.Sequential(
        [
            layers.Dense(units=256, input_shape=input_dim, activation='relu'),
            layers.Flatten(),
            layers.Dense(units=128, activation='relu'),
            layers.Dense(units=64, activation='relu'),
            layers.Dense(units=output_num, activation='softmax')
        ]  
    )
    
    model.compile(optimizer=keras.optimizers.Adam(learning_rate), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=max_epochs, validation_data=(X_val, y_val))

    return model