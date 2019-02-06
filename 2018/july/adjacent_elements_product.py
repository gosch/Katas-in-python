def adjacentElementsProduct(inputArray):
    size = len(inputArray)
    max_product = inputArray[0] * inputArray[1]
    for i in range(1, size - 1):
        product = inputArray[i] * inputArray[i+1]
        max_product = product if max_product < product else max_product
    return max_product


if __name__ == '__main__':
    print(adjacentElementsProduct([2, 4, 5, 7, -8]))
