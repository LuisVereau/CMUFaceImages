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

X = [cv2.imread(data[0]) for data in dataSet_aux]
y = [data[1] for data in dataSet_aux]

X = np.asarray(X)
y = np.asarray(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=randint(0, 10000))

model = trainModel(X_train, y_train)

prediction = model.predict(X_test)

test_evaluation = model.evaluate(X_test, y_test)

seed = randint(0, len(X_test))

print('-'*60)
print(f'Classe real IMG de teste (escolhida aleatoriamente): {y_test[seed]}')
print(f'Classe predita dessa IMG de teste: {np.argmax(prediction[seed])}')
print(f'A taxa de acerto do modelo foi de {test_evaluation[1]*100:.4f}%')
print('-'*60)

cv2.imshow('IMG de teste', X_test[seed])
cv2.waitKey(0)
cv2.destroyAllWindows()