def pressingButtons(buttons):
    k = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    r = [""]
    for button in buttons[::-1]:
        t = [c for c in k[int(button)]]
        r = [c + v for c in t for v in r]
    return r


print(pressingButtons("42"))
