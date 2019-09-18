def stolenLunch(note):
    r = ""
    for c in note:
        if c.isdigit():
            r += chr(int(c) + ord('a'))
        elif ord(c) >= ord('a') and ord(c) <= ord('j'):
            r += str(ord(c) - ord('a'))
        else:
            r += c
    return r

inp = "you'll n4v4r 6u4ss 8t: cdja"
print(stolenLunch(inp))