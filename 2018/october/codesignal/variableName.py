def variableName(name):
    if name[0].isdigit():
        return False
    for i in name:
        if not i.isdigit() and not i.isalpha() and i != '_':
            return False
    return True

print(variableName("var_1_Int"))
