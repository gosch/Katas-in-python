def arrayComplexElementsProduct(real, imag):
    if len(real) > 2:
        return arrayComplexElementsProduct([real[0] * real[1] - imag[0] * imag[1]] + real[2:],
                                           [real[0] * imag[1] + real[1] * imag[0]] + imag[2:])
    else:
        return [real[0] * real[1] - imag[0] * imag[1], real[0] * imag[1] + real[1] * imag[0]]


print(arrayComplexElementsProduct([1, 2, 3], [0, 0, 0]))
