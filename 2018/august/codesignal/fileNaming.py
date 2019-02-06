def fileNaming(names):
    names_set = set()
    dict_names_count = dict()
    res = []
    for i in names:
        if i not in names_set:
            names_set.add(i)
            dict_names_count[i] = 1
            res.append(i)
        else:

            new_name = i + '(' + str(dict_names_count[i]) + ')'
            while new_name in names_set:
                dict_names_count[i] += 1
                new_name = i + '(' + str(dict_names_count[i]) + ')'
            names_set.add(new_name)
            dict_names_count[i] += 1
            dict_names_count[new_name] = 1
            res.append(new_name)

    return res

names = ["doc",
         "doc",
         "image",
         "doc(1)",
         "doc"]

print(fileNaming(names))
