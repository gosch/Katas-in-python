def encodingDecoding2(m):
    r = ""
    i = j = 0
    if m:
        if m[0].isdigit():
            while i < len(m):
                r += chr(int(m[i:i+2], 16)-j)
                i += 2
                j += 1
        else:
            for i in m:
                r += str('%x' % (ord(i)+j))
                j += 1
    return r






def encodingDecoding(messages):
    r = ""
    n = ""
    counter = 0
    for i, l in enumerate(messages):
        if len(n) > 0:
            if int(n) < 6:
                num = int(n + l) - 40 if l.isdigit() else (int(n) - 4) * 16 + (10 + ord(l) - ord('a'))
            else:
                num = int(n + l) - 60 if l.isdigit() else (int(n) - 6) * 16 + (10 + ord(l) - ord('a'))
            if int(n) < 6:
                r += chr(ord('A') - 1 + int(num) - counter)
            else:
                r += chr(ord('a') - 1 + int(num) - counter)
            counter += 1
            n = ""
        elif l.isdigit():
            n = l
        elif l == ' ':
            r += str(20+counter)
            counter += 1

        elif ord(l) < 91:
            num = ord(l) - ord('A') + counter + 1
            f1 = num // 16
            f1 = "4" if f1 == 0 else str(4+f1)
            f2 = num % 16
            f2 = chr(ord('a') + (f2 - 10)) if f2 > 9 else str(f2)
            r += f1+f2
            counter += 1
        else:
            num = ord(l) - ord('a') + counter + 1
            f1 = num // 16
            f1 = "6" if f1 == 0 else str(6+f1)
            f2 = num % 16
            f2 = chr(ord('a') + (f2 - 10)) if f2 > 9 else str(f2)
            r += f1+f2
            counter += 1
    return r

print(ord('A'))
print(encodingDecoding('0'))

