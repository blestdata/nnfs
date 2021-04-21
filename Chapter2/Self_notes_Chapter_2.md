# Introduction to neural Networks

For a neural network with `n1, n2, n3, .... ni` neurons in layer 1, 2, 3, ... i
then the number of biases would be :-

`bias = n2 + n3 + ... + ni`

And the number of weights would be :-

`weights = n2 * n1 + n3 * n2 + n4 * n3 + ..... + ni * n(i-1)`

# Definitions

for a set of data coming from a bunch of sensors :-

_Each Measurement will be a **feature**._
_A group of features will be a **feature set**._
_Value of a feature set is referred as a **sample**_

**output = `activation`(weights * inputs + bias)**