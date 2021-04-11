class ImproperConfiguredInput(Exception):
    def __init__(self, position = -1, message="Please check inputs"):
        self.position = position
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        if self.position==-1:
            return "{}".format(self.message)
        else:
            return "Check position at {} - {}".format(self.position, self.message)


def neuron_layer(input_values, weights_list_of_list, bias_list):
    """
    Calculate the output of each neuron and give out output list.
    :param input_values: list of input values common to all neurons in the layer.
    :param weights_list_of_list: a combined list of lists of weights.
           For m inputs and n neurons in the layer, each sublist would be of size m for
           a total of n lists
    :param bias_list:  a list of size n containing bias foe each neuron
    :return: a list of output values for the layer
    :exception if len(input_values) != len(weights_list_of_list[sublist])
               then raise ImproperConfiguredInput error got the neuron
    :exception if len(weight_list_of_list)!=len(bias_list) then
               raise ImproperConfiguredInput error
    """
    output_list = []

    if len(weights_list_of_list)!=len(bias_list):
        raise ImproperConfiguredInput

    for i in range(len(weights_list_of_list)):
        if len(weights_list_of_list[i])!=len(input_values):
            raise ImproperConfiguredInput(message="Sublist of length {} while input list of lenght {}".format(
                len(weights_list_of_list[i]), len(input_values)), position= i)

        intermediate_output = 0

        for j in range(len(input_values)):
            print("neuron {} input {} has input value {} and weight {} with total value {}".format(i, j, input_values[j], weights_list_of_list[i][j], input_values[j]*weights_list_of_list[i][j]))
            intermediate_output += (input_values[j])*(weights_list_of_list[i][j])
        intermediate_output += bias[i]
        output_list.append(intermediate_output)

    return output_list

if __name__ == '__main__':
    inputs = [3, 5, 1, 8]

    weights_1 = [0.1, 0.5, -0.2, 0.6]
    weights_2 = [0.4, 0.7, 0.3, 0.2]
    weights_3 = [0.2, 0.2, 0.9, 0.8]

    bias_1 = 5
    bias_2 = 1.9
    bias_3 = 4

    weights = [weights_1, weights_2, weights_3]
    bias = [bias_1, bias_2, bias_3]

    print(neuron_layer(inputs, weights, bias))

    """
    Observation:- python is producing numbers after decimal for first neuron where the input does not have that precision.
                  eg, for first:- neuron 0 input 0 has input value 3 and weight 0.1 with total value 0.30000000000000004
                  This is said to be due to the internal representation of numbers in python. (+/- mantisse)*2^exponential
                  if precision of output is needed to be the same as input, all numbers should either be in float 32 
                  or float 64 forms. check for the functionality in numpy.
    """