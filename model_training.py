import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import models, layers
from random import randint
from sklearn.model_selection import KFold

def trainModel(X_train_arg, y_train_arg):
    seed = randint(0, 10000)

    # Hiperparameters
    learning_rate = 0.001
    input_dim = X_train_arg[0].shape
    output_num = len(np.unique(y_train_arg))
    max_epochs = 20

    kf = KFold(5, shuffle=True, random_state=seed)
    fold = 0
    accuracy_history = list()
    my_models = list()

    for train, val in kf.split(X_train_arg, y_train_arg):
        fold += 1

        X_train = X_train_arg[train]
        y_train = y_train_arg[train]
        X_val = X_train_arg[val]
        y_val = y_train_arg[val]

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

        evaluation = model.evaluate(X_val, y_val)
        accuracy_history.append(evaluation[1])
        my_models.append(model)
    
    my_model = my_models[np.argmax(accuracy_history)]

    return my_model