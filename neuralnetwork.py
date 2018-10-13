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
        self.neurons = {}
        self.neurons['input'] = []
        self.neurons['output'] = []
        for i in range(0, kwargs['inputs']):
            self.neurons['input'].append(Neuron())
        for i in range(0, kwargs['outputs']):
            self.neurons['output'].append(Neuron())

    def start(self, inputs):
        """
        starts neuralnetwork. duh
        """
        for i in range(0, len(inputs)):
            self.neurons['input'][i].reel_it_in(inputs)
        for layer in self.neurons:
            for neuron in self.neurons[layer]:
                neuron.pick_it_up()

    def status(self):
        status = ''
        for layer in self.neurons:
            for n in layer:
                status += n.status()
        return status


def main():
    """
    totally not the main method
    """
    inputs = [3, 2, 6, 7]
    neuralnet = NeuralNetwork(inputs=4, outputs=10)
    neuralnet.start(inputs)
    print(neuralnet.status())


if __name__ == '__main__':
    main()
