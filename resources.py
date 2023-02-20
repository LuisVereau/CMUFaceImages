import os
import random

def splitDataset(dataset, train_size, shuffle: bool=True):
    if (shuffle == True):
        random.shuffle(dataset)

    first_split = int(len(dataset)*train_size)

    train_dataset = dataset[0:first_split]
    test_dataset = dataset[first_split:]

    return [train_dataset, test_dataset]

def getFaces(dir):
    os.chdir(dir)
    imgs = list()
    for folder in os.listdir():
        os.chdir(folder)
        for img in os.listdir():
            if (img.split('_')[-1] == '4.pgm'):
                imgs.append(img)
        os.chdir(dir)
    return imgs