import re


def wailingGhosts(sounds):
    if sounds[0] == 'u' or sounds[-1] == 'u':
        return False

    sounds_flags = [False] * len(sounds)
    # words = re.split(r"u+", sounds)
    find_u = re.finditer(r"u+", sounds)
    previous_limit = 0
    for i in find_u:
        s = i.start()
        e = s + len(i.group())
        for j in range(s, e):
            sounds_flags[j] = True
        c = 0
        if previous_limit == s:
            return False
        for j in range(previous_limit, s):

            if sounds_flags[j]:
                return False
            else:
                sounds_flags[j] = True

            if e+c == len(sounds) or sounds_flags[e+c] or sounds[e+c] == 'u':
                return False
            else:
                sounds_flags[e+c] = True
            c += 1
        previous_limit = e+c
    return False not in sounds_flags


print(wailingGhosts("ouououo"))
