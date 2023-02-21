from sklearn.model_selection import train_test_split
import cv2
import os
import numpy as np
from random import randint
from my_resources import getFaces
from model_training import trainModel

main_dir = os.getcwd()
faces_dir = main_dir+'\\faces'

dataSet_aux = getFaces(faces_dir)

X = list()
y = list()
for data in dataSet_aux:
   X.append(cv2.imread(data[0]))
   y.append(data[1])

X = np.asarray(X)
y = np.asarray(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=randint(0, 10000))

model = trainModel(X_train, y_train)

test_evaluation = model.evaluate(X_test, y_test)

print(f'A taxa de acerto do modelo foi de {test_evaluation[1]*100:.4f}%')