from Chapter2.Exception import ImproperConfiguredInput
import numpy as np

if __name__ == '__main__':
    input_list = [4, 2, 7, 5]
    weights_list = [0.9, -0.6, 1.3, 0.2]
    bias = 2

    if len(input_list)!= len(weights_list):
        raise ImproperConfiguredInput

    output = np.dot(input_list, weights_list) + bias
    
    print(output)