from random import randint
from os import path


def generate_map(x, y):
    start_x = int(randint(0, x - 1))
    start_y = int(randint(0, y - 1))

    for i in range(0, x):
        for j in range(0, y):
            rand = randint(0, 100)
            if i == start_x and j == start_y:
                print('S', end='')
                continue
            if rand < 15:
                print('P', end='')
            else:
                print('X', end='')
        print()


def read_map():
    m = []
    p = path.join('.', 'src', 'maps', 'map1.txt')
    p_counter = 0
    with open(p) as fp:
        for line in fp:
            line_arr = []
            for ch in line:
                if ch != '\n':
                    line_arr.append(ch)
                if ch == 'P':
                    p_counter += 1
            m.append(line_arr)

    for i in range(0 , len(m)):
        for j in range(0 , len(m[i])):
            if m[i][j] == 'S':
                x, y = i, j

    map_object = {
        'Treasure_count': p_counter,
        'Map': m,
        'Start': (x, y)
    }
    return map_object


# generate_map(50 , 50)
print(read_map())
