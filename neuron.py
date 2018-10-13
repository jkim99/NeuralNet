import math


def sigmoid(x):
    """
    """
    return 1 / (1 + math.exp(-x))


class Neuron():
    def __init__(self):
        self.weights = []
        self.in_value = []
        self.out_value = 0

    def reel_it_in(self, keys, values):
        """
        I GOT THE BAG
        """
        for key in keys:
            self.in_value[key] = values[key]

    def pick_it_up(self):
        """
        pick it up, pick it up OOOOH baby gurl watch how i moooove (DEXTER)
        """
        if not self.verify():
            print("invalid node")
            return None
        for i in range(0, len(self.in_value)):
            self.out_value += self.in_value[i] * self.weights[i]
        self.out_value = sigmoid(self.out_value)

    def verify(self):
        """
        verifies node integrity/validity
        """
        return len(self.weights) == len(self.in_value)