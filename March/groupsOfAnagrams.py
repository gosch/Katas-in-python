def groupsOfAnagrams(words):
    v = set()
    for i in range(len(words)):
        v.add("".join(sorted(words[i])))
    return len(v)


test = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
print(groupsOfAnagrams(test))
