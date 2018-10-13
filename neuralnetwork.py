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
    def __init__(self, *args, **kwargs):
        """
        DID SOMEONE SAY DICTIONARY COMPREHENSION?????
        Lmao jk jk it's not that bad.
        """
        self.neurons = []
        for i in range(0, kwargs['layers']):
            self.neurons.append([])
        for i in range(0, kwargs['inputs']):
            self.neurons[0].append(Neuron(weights=kwargs['inputs'],
                                          biases=kwargs['inputs']))
        for i in range(0, kwargs['outputs'] - 1):
            self.neurons[kwargs['layers'] - 1].append(Neuron(
                                                  weights=kwargs['inputs'],
                                                  biases=kwargs['inputs']))

    def start(self, inputs):
        """
        starts neuralnetwork. duh
        """
        for i in range(0, len(self.neurons) - 1):
            totals = []
            for j in range(0, len(self.neurons[i])):
                n = self.neurons[i][j]
                n.reel_it_in(inputs)
                n.pick_it_up()
                totals[j] += n.out_value

    def status(self):
        status = ''
        for layer in self.neurons:
            for n in self.neurons[layer]:
                status += n.status()
        return status


def main():
    """
    totally not the main method
    """
    inputs = [0.3, 0.2, 0.6, 0.7]
    neuralnet = NeuralNetwork(inputs=4, layers=3, outputs=3)
    neuralnet.start(inputs)
    # print(neuralnet.status())


if __name__ == '__main__':
    main()
