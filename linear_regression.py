import random
import numpy as np
import matplotlib as plt

training_x = [1, 2, 3, 4, 5, 6, 7, 8]
training_y = [5, 6.5, 8, 12.5, 14, 15, 18.5, 21]
learning_rate = .01
w1 = random.random()
w2 = random.random()
mse = 0
for i in range(100000):
    random_int = np.random.randint(0, 8)
    data_x = training_x[random_int]
    data_y = training_y[random_int]
    dcdw = 2 * ((w1 * data_x + w2) - data_y) * data_x
    dcdb = 2 * ((w1 * data_x + w2) - data_y)
    w1 = w1 - (learning_rate * dcdw)
    w2 = w2 - (learning_rate * dcdb)
    pred = w1 * data_x + w2
    mse = ((pred) - data_y) ** 2
    mse = mse / len(training_x)
    if i % 1000 == 0:
        print(mse)
