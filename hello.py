#hello.py
import math
import random

ui = input("I'm a simple neural network of 3 neurons, please enter a number:")
ui = int(ui)

w1 = random.random()
w2 = random.random()

b1 = random.random()
b2 = random.random()


def sigmoid(x):
    return 1/(1+ math.exp(-x))

n1 = sigmoid(ui*w1 + b1)
n2 = sigmoid(n1*w2 + b2)

print(f"Hello World! The output is {n2}.")