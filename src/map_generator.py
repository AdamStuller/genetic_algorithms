from random import randint

def generate_map(x , y ):
    start_x = int(randint(0, x-1))
    start_y = int(randint(0, y-1))

    for i in range(0 , x):
        for j in range(0 , y):
            rand = randint(0, 100)
            if i == start_x and j == start_y:
                print('S', end='')
                continue
            if (rand ) < 15:
                print('P', end='')
            else:
                print('X', end='')
        print()


generate_map(20 , 20)