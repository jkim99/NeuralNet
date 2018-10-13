"""
File: neuralnetwork.py
Language: python3.7
Author: Jonathan Kim <jk7783@rit.edu>

flake8 verified.
"""
from neuron import Neuron


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

    def start(self, inputs):
        """
        starts neuralnetwork. duh
        """
        for i in range(0, len(inputs)):
            self.neurons['input'][i].reel_it_in(i, inputs[i])
        for layer in self.neurons:
            for neuron in layer:
                neuron.pick_it_up()


def main():
    """
    totally not the main method
    """
    neuralnet = NeuralNetwork()
    neuralnet.start()


if __name__ == '__main__':
    main()
