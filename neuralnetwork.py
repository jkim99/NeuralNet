"""
File: neuralnetwork.py
Language: python3.7
Author: Jonathan Kim <jk7783@rit.edu>

flake8 verified.
"""
import math


def sigmoid(x):
    """
    """
    return 1 / (1 + math.exp(-x))


class NeuralNetwork():
    """
    NeuralNetwork Object. Handles backpropogation and initialization of nodes.
    Also every 5 minutes it kicks you really hard in the balls.
    """
    def __init__(self, layers, inputs, outputs):
        """
        DID SOMEONE SAY DICTIONARY COMPREHENSION?????
        Lmao jk jk it's not that bad.
        """
        self.neurons = {}
        self.neurons['input'] = []
        self.neurons['output'] = []
        for i in range(0, inputs):
            self.neurons['input'].append(Neuron())
        for i in range(0, outputs):
            self.neurons['output'].append(Neuron())

    def start():
        """
        starts neuralnetwork. duh
        """


class Neuron():
    def __init__(self):
        self.weights = []
        self.in_value = []
        self.out_value = []

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
            return
        out = 0
        for i in range(0, len(self.in_value)):
            out += self.in_value[i] * self.weights[i]
        out = sigmoid(out)

    def verify(self):
        """
        verifies node integrity/validity
        """
        return len(self.weights) == len(self.in_value)


def main():
    """
    totally not the main method
    """
    neuralnet = NeuralNetwork()
    neuralnet.start()


if __name__ == '__main__':
    main()
