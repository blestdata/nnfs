from Chapter2.Exception import ImproperConfiguredInput
import numpy as np

if __name__=="__main__":
    inputs = [3, 5, 1, 8]

    weights = [[0.1, 0.5, -0.2, 0.6],
               [0.4, 0.7, 0.3, 0.2],
               [0.2, 0.2, 0.9, 0.8]]

    bias = [5, 1.9, 4]

    if len(bias) != len(weights):
        raise ImproperConfiguredInput
    try:
        layer_output = np.dot(weights, inputs) + bias
    except Exception as e:
        print(e, e.args)

    print(layer_output)
