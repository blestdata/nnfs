from .Exception import ImproperConfiguredInput

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

    for neuron_weight, neuron_bias in zip(weights_list_of_list, bias_list):
        intermediate_output = 0
        for input_value, weight_value in zip(input_values, neuron_weight):
            intermediate_output += input_value*weight_value

        intermediate_output += neuron_bias

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

