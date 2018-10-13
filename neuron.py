import math
import random


def sigmoid(x):
    """
    """
    return 1 / (1 + math.exp(-x))


class Neuron():
    def __init__(self, *args, **kwargs):
        self.weights = []
        self.biases = []
        for i in range(0, kwargs['weights']):
            try:
                self.weights[i] = random.uniform(0, 1)
            except IndexError:
                self.weights.append(random.uniform(0, 1))
        for i in range(0, kwargs['biases']):
            try:
                self.biases[i] = random.uniform(0, 1)
            except IndexError:
                self.biases.append(random.uniform(0, 1))
        self.in_value = []
        self.out_value = 0

    def reel_it_in(self, values):
        """
        I GOT THE BAG
        """
        for i in range(0, len(values)):
            try:
                self.in_value[i] = values[i]
            except IndexError:
                self.in_value.append(values[i])

    def pick_it_up(self):
        """
        pick it up, pick it up OOOOH baby gurl watch how i moooove
        """
        if not self.walk_it_like_i_talk_it():
            print("invalid node")
            return None
        for i in range(0, len(self.in_value)):
            self.out_value += sigmoid(self.in_value[i]
                                      * self.weights[i]
                                      + self.biases[i])

    def walk_it_like_i_talk_it(self):
        """
        walk it. walk it like I talk it.
        """
        return len(self.weights) == len(self.biases)

    def status(self):
        inputs = ''
        for i in self.in_value:
            inputs += '        ' + str(i) + '\n'
        return 'inputs: \n' + inputs
