import textwrap

st = "This is a very long message that should be divided in different messages This is a very long message that should be divided in different messages "
st = st*2
st = st[:-1:]
result = textwrap.wrap(st, 15)

print(result)
total = len(result)
for i, m in enumerate(result):
    index = '[' + str(i+1) + '/' + str(total) + ']'
    print('Size: ' + str(len(m) + len(index)) + ' =' + index + m)
