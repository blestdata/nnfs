# Introduction to neural Networks

For a neural network with `n1, n2, n3, .... ni` neurons in layer 1, 2, 3, ... i
then the number of biases would be :-

`bias = n2 + n3 + ... + ni`

And the number of weights would be :-

`weights = n2 * n1 + n3 * n2 + n4 * n3 + ..... + ni * n(i-1)`

# Definitions

For a set of data coming from a bunch of sensors :-

_Each Measurement will be a **feature**._
_A group of features will be a **feature set**._
_Value of a feature set is referred as a **sample**_

**output = `activation`(weights * inputs + bias)**

weights and biases are adjustible paramaters of a neural network

# First Neurons

When you initialize parameters in neural networks, our network will have weights initialized randomly, and biases set as zero to start. The values for weights and biases are what get “trained,” and they are what make a model actually work (or not work).

for a set of inputs for a single neuron:-
```python
result = 0
inputvalues = [1, 5, 6, 23, -14, 9]
weightvalues = [0.5, 0.9, 1.6, 0.4, 1.6, -0.1]
bias = 3
for i in range(len(inputvalues)):
    result += inputvalues[i]*weightvalues[i]
result += bias
```