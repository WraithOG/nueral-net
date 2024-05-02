import random
petal_length = ["3", "2", "4", "3", "3.5", "2", "5.5", "1", "4.5"]
petal_width = ["1.5", "1", "1.5", "1", ".5", ".5", "1", "1", "1"]
training_iterations = 100


def loss(guess, y):
    cost = (1 / len(petal_length)) * ((y - guess) ** 2)
    return cost

def pred(x, w1, w2):
    prediction = w1 * x + w2
    return prediction

def gradient_descent(learning_rate, w1, w2, cost):
    w1 = w1 - (learning_rate * cost)
    w2 = w2 - (learning_rate * cost)
    return w1, w2

def initialize_weights():
    slope = random.random()
    intercept = random.random()
    return slope, intercept

slope, intercept = initialize_weights()
print(f"w1: {slope}\n w2: {intercept}")
test_pred = pred(3, slope, intercept)
print(f"Initial prediction: {test_pred}")
cost = loss(test_pred, 1.5)
print(f"Cost: {cost}")
w1, w2 = gradient_descent(20, slope, intercept, cost=cost)
print(f"New w1: {w1}\n New w2: {w2}")
new_pred = pred(3, w1, w2)
print(f"New pred: {new_pred}")
