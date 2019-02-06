

def calc_fact(n):
    result = 1
    for i in range(n):
        result = (i+1) * result
    return result

def calc_fact_recur(n):
    if n == 0:
        return 1
    return n * calc_fact_recur(n - 1)


def nextSecond(c):
    s = c[0] * 3600 + c[1]*60 + c[2] + 1
    return [s // 3600 % 24, s//60 % 60, s % 60]

def maxSubarray(inputArray):
    max_sum = 0
    for i in range(len(inputArray)):
        current_sum = inputArray[i]
        max_sum = current_sum if max_sum < current_sum else max_sum
        for j in range(i+1, len(inputArray)):
            current_sum = current_sum + inputArray[j]
            max_sum = current_sum if max_sum < current_sum else max_sum

    return max_sum


def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1+value2
    if weight1 > maxW and weight2 > maxW:
        return 0
    if weight1 > maxW:
        return value2
    if weight2 > maxW:
        return value1
    return value1 if value1 > value2 else value2


def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    result = []
    for i in range(len(matrix)):
        row =[]
        if i not in rowsToDelete:
            for j in range(len(matrix[i])):
                if j in columnsToDelete:
                    continue
                row.append(matrix[i][j])
        if len(row) > 0:
            result.append(row)
    print(result)

def lastDigitRegExp(inputString):
    for i in range(len(inputString)-1, -1, -1):
        flag = False
        if inputString[i].isdigit():
            end = i
            start = end
            for j in range(i, 0, -1):
                if not inputString[j].isdigit():
                    flag = True
                    break
                end = j
        if flag:
            break
    return inputString[start:end+1]


def subtractionByRegrouping(minuend, subtrahend):
    result = []
    borrow = 0
    minuend = str(minuend)
    subtrahend = str(subtrahend)
    for i in range(len(minuend) - 1, -1, -1):
        if int(minuend[i]) - borrow == int(subtrahend[i]):
            result.append(int(minuend[i]) - borrow)
            borrow = 0
        elif int(minuend[i]) - borrow < int(subtrahend[i]):
            result.append(int(minuend[i]) - borrow + 10)
            borrow = 1
        else:
            result.append(int(minuend[i]) - borrow)
            borrow = 0

    return result


def fractionComparison(a, b):
    if a[0]/a[1] == b[0]/b[1]:
        return "="
    elif a[0]/a[1] < b[0]/b[1]:
        return "<"
    else:
        return ">"

def rotateImage(a):
    mat = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])-1, -1, -1):
            row.append(a[j][i])
        mat.append(row)
    return mat

print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# print(subtractionByRegrouping(4567, 3456))

# print(lastDigitRegExp('3w2'))

# print(nextSecond([23,59,59]))
# print(maxSubarray([-1, 7, -2, 3, 4, 0, 1, -1]))
# print(knapsackLight(5, 3, 7, 4, 6))
# constructSubmatrix([[1, 0, 0, 2],
#                     [0, 5, 0, 1],
#                     [0, 0, 3, 5]], [1], [0, 2])


