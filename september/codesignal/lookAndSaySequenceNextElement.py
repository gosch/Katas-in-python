def lookAndSaySequenceNextElement(element):
    counter = 0
    last_element = 'a'
    r = ''
    i = 0
    while i < len(element):
        if last_element == element[i]:
            counter += 1
        else:
            if last_element == 'a':
                last_element = element[i]
                counter = 1
            else:
                r += str(counter) + str(last_element)
                last_element = element[i]
                counter = 1
        i+=1
    r += str(counter) + str(last_element)
    return r

print(lookAndSaySequenceNextElement('1'))

