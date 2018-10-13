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

    def forward_propogate(self, inputs, layer):
        """
        starts neuralnetwork. duh
        """
        for j in range(0, len(self.neurons[layer])):
            self.neurons[layer][j].reel_it_in(inputs)
            self.neurons[layer][j].pick_it_up()

    def start(self, inputs):
        """
        POP THAT GOLD (GOLD). COLLAD GREENS
        """
        for i in range(0, len(self.neurons) - 1):
            self.forward_propogate(inputs, i)
            for j in range(0, len(self.neurons[i])):
                inputs.append(self.neurons[i][j].out_value)
            inputs = []

    def status(self):
        """
        checks the status of the neural network
        """
        status = ''
        for i in range(0, len(self.neurons)):
            for j in range(0, len(self.neurons[i])):
                n = self.neurons[i][j]
                status += n.status()
        return status

    def back_propergate(self):
        """
        hi jeff
        """


def main():
    """
    totally not the main method
    """
    inputs = [0.3, 0.2, 0.6, 0.7]
    neuralnet = NeuralNetwork(inputs=4, layers=2, outputs=3)
    neuralnet.start(inputs)
    print(neuralnet.status())


if __name__ == '__main__':
    main()
