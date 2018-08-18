from collections import OrderedDict
def stringsRearrangement(inputArray):
    d = OrderedDict()
    counter = [0] * len(inputArray)
    for i, val in enumerate(inputArray):
        word = list(val)
        for j in range(len(word)):
            temp = list(word)
            temp[j] = '_'
            temp = ''.join(temp)
            if temp not in d:
                d[temp] = [i]
            else:
                d[temp].append(i)
    new_d = OrderedDict()

    for key in sorted(list(d.keys()), key=lambda v: len(d[v]), reverse=True):
        new_d[key] = d[key]
    print(new_d)



inputArray1 =  ["aba",
             "bbb",
             "bab"]
inputArray2 = ["ab", "bb", "aa"]
inputArray3 = ["zzzzab",
               "zzzzbb",
               "zzzzaa"]
inputArray4 = ["ab",
 "ad",
 "ef",
 "eg"]

inputArray5 = ["abc",
 "bef",
 "bcc",
 "bec",
 "bbc",
 "bdc"]
inputArray6 = ["abc",
 "abx",
 "axx",
 "abc"]

inputArray7 = ["abc",
 "abx",
 "axx",
 "abx",
 "abc"]

# print(stringsRearrangement(inputArray1))
# print(stringsRearrangement(inputArray2))
# print(stringsRearrangement(inputArray3))
# print(stringsRearrangement(inputArray4))
print(stringsRearrangement(inputArray5))
# print(stringsRearrangement(inputArray6))
# print(stringsRearrangement(inputArray7))

