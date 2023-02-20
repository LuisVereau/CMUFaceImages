import os
from my_modules import *

main_dir = os.getcwd()
faces_dir = main_dir+'\Faces'

classes = [folder for folder in os.listdir()]
images = getFaces(faces_dir)

train_dataset, test_dataset = splitDataset(images, 0.75)

print(len(train_dataset))
print(len(test_dataset))

