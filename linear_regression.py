import random
import numpy as np
import matplotlib.pyplot as plt

training_x = [1, 2, 3, 4, 5, 6, 7, 8]
training_y = [5, 6.5, 8, 12.5, 14, 15, 18.5, 21]
learning_rate = .01
w1 = random.random()
w2 = random.random()
mse = 0

for i in range(50000):
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

print(f"The slope of our regression is: {w1}\n The intercept of our function is {w2}")

def predictions(w, b, x):
    stored_preds = []
    for i in range(len(x)):
        prediction = w * x[i] + b
        stored_preds.append(prediction)
    return stored_preds

predicted_y = predictions(w1, w2, training_x)
print(f"Predicted y-values: {predicted_y}\n Actual y-values: {training_y}")
print(f"Error: {mse}")

#plot data and line
x = np.linspace(0.0, 10.0, 25)
y = x
plt.plot(x, w1 * y + w2, '-')
plt.plot([training_x], [training_y], 'ro')
plt.grid()
plt.show()