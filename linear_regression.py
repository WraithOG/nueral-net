import random
petal_length = ["3", "2", "4", "3", "3.5", "2", "5.5", "1", "4.5"]
petal_width = ["1.5", "1", "1.5", "1", ".5", ".5", "1", "1", "1"]

def pred(x, y):
    slope = random.random()
    intercept = random.random()
    initial_guess = slope * x + intercept
    #mse = (1 / len(petal_length)) * (true_value - prediction)
    return initial_guess
prediction = pred(1,2)
print(prediction)
