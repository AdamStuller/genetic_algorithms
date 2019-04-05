from random import randint
from os import path


def generate_map(x, y):
    """
    Method that generates new map
    :param x:   int
        size of new map in x dimension
    :param y:   int
        size of new map in y dimension
    """
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


def read_map(name='map1.txt'):
    """
    Method, that reads given map in txt format
    :param name: str
                name of map to be read in maps folder
    :return: str[][]
    Two dimensional array of characters, representing map

    """
    m = []
    p = path.join('.', 'maps', name)
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

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j] == 'S':
                x, y = j, i

    map_object = {
        'Treasure_count': p_counter,
        'Map': m,
        'Start': (y, x),
        'Width': len(m[0])-1,
        'Height': len(m)-1
    }
    return map_object


def main():
    generate_map(6, 6)


if __name__ == "__main__":
    main()

