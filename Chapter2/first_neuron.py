def neuron():
    input = [3, 6, 12, 7]

    weights = [0.2, 0.64, -0.79, 0.91]

    bias = 1

    output = (input[0]* weights[0] +
              input[1]* weights[1] +
              input[2]* weights[2] +
              input[3]* weights[3]) + bias
    return output

if __name__ == '__main__':
    print(neuron())
