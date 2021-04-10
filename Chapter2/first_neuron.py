class ImproperConfiguredInput(Exception):
    pass

def neuron():
    input = [3, 6, 12, 7]

    weights = [0.2, 0.64, -0.79, 0.91]

    bias = 1

    output = (input[0]* weights[0] +
              input[1]* weights[1] +
              input[2]* weights[2] +
              input[3]* weights[3]) + bias
    return output

def neuron_output(inputvalues, weightvalues, bias):
    """
    :param inputvalues: list of input values. eg [3, 2.4, 1, -2]
    :param weightvalues: list of weight values. eg [1.1, 0.7, -0.3, 0.2]
    :param bias: value of bias. eg 2
    :return:
    :exception if len(inputvalues) != len(weightvalues) then raise ImproperConfiguredInput error
    """
    if len(inputvalues) != len(weightvalues):
        raise ImproperConfiguredInput("Input and weight are of different length")
    result = 0
    for i in range(len(inputvalues)):
        result += inputvalues[i]*weightvalues[i]
    result += bias
    return result


if __name__ == '__main__':
    print(neuron())
    print(neuron_output([1, 5, 6, 23, -14, 9], [0.5, 0.9, 1.6, 0.4, 1.6, -0.1], 3))
