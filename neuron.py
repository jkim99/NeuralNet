import math
from random import random


def sigmoid(x):
    """
    """
    return 1 / (1 + math.exp(-x))


class Neuron():
    def __init__(self, *args, **kwargs):
        self.weights = []
        for i in range(0, len(self.weights)):
            self.weights[i] = random()
        self.biases = []
        self.in_value = []
        self.out_value = 0

    def reel_it_in(self, values):
        """
        I GOT THE BAG
        """
        try:
            for i in range(0, len(values)):
                self.in_value[i] = values[i]
        except IndexError:
            self.in_value.append(values[i])

    def pick_it_up(self):
        """
        pick it up, pick it up OOOOH baby gurl watch how i moooove (DEXTER)
        """
        if not self.verify():
            print("invalid node")
            return None
        for i in range(0, len(self.in_value)):
            self.out_value += self.in_value[i] \
                             * self.weights[i] \
                             + self.biases[i]
        self.out_value = sigmoid(self.out_value)

    def verify(self):
        """
        verifies node integrity/validity
        """
        return len(self.weights) == len(self.in_value) == len(self.biases)

    def status(self):
        return 'inputs: ' + self.in_value
