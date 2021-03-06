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

A list of lists is an __array__ when it is __homologous__ (i.e. same structure) in one dimension even if different dimensions have different length. For machine learning, __matrix__ is just a rectangular 2D array, and A __tensor__ object is an object that can be represented as an array.

A __vector__ in math is what we call a list
in Python or a 1-dimensional array in NumPy. A __dot product__ of two vectors is a sum of products of consecutive vector elements. Both vectors must be of the same size (have an equal number of elements).

A matrice with dimension of 1 horizontally is a **column vector** and same vertically is a **row vector**. 
And a dot product of two vectors equals a matrix product of
a row and column vector. 
**Transpose** interchanges rows and columns.


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

Neural networks typically have layers that consist of more than one neuron. Each neuron in a layer takes exactly the same input but contains its own set of weights and its own bias, producing its own unique output. This is called a __fully connected neural network__ every
neuron in the current layer has connections to every neuron from the previous layer.

```python
input_values = [3, 5, 1, 8]
weights_list_of_list = [[0.1, 0.5, -0.2, 0.6], [0.4, 0.7, 0.3, 0.2], [0.2, 0.2, 0.9, 0.8]]
bias_list = [5, 1.9, 4]

output_list = []

for i in range(len(weights_list_of_list)):
    intermediate_output = 0
    for j in range(len(input_values)):
        intermediate_output += (input_values[j])*(weights_list_of_list[i][j])
    intermediate_output += bias_list[i]
    output_list.append(intermediate_output)
```

for a set of points and values, the number of neurons would be the number of sublist in the weights list. This should be the same as the number of values in bias as each neuron should have its own sets of weights and its own bias. 

Also, for each input each neuron should have a weight corresponding to the input. For successive layers, the number of neurons may increase, decrease or stay the same value. 

Instead of loops above, Numpy implementation of the dot product would be:- 
```python
output = np.dot(input_list, weights_list) + bias
```

To convert a list into a numpy matrice, make an array out of it by contining it into a list.
```python
a = np.array([[1, 2, 3, 4, 5]])
# transpose
a.T
# dot product
np.dot(a, a.T)
```

### Layer of Neurons
