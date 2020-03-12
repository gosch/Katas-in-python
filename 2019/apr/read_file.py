import sys

if __name__ == '__main__':
    my_props = {}
    if len(sys.argv) < 2:
        # print("Need more arguments")
        # exit(0)
        input_file = "properties.txt"
    else:
        input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if "=" not in line or line.startswith("#"):
                continue
            k, v = line.split("=", 1)
            value = v.strip()
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    value = value
            my_props[k.strip()] = value

    print(my_props)

