file_name = "dicts/negative.yml"
string_to_add = ": [negative]"

with open(file_name, 'r') as f:
    i = 0
    for line in f:
        i = i +1
        x = f.readline()
        x = x.split()
        print(type(x[0]))
        print(i)
