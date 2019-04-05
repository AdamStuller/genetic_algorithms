from random import randint, choice
from virtual_machine import VirtualMachine
from map_generator import read_map
import numpy
import copy

steps = {
    'H': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'P': (0, 1)
}


def generate_population(n, k):
    population = []
    for i in range(0, n):
        individual = generate_individual(randint(k, 63))
        population.append(individual)
    pop = list(map(lambda x: {'Object': x, 'Fiitness': fiitness_function(x)}, population))
    print(pop)
    return pop


def generate_individual(initial_size):
    individual = [0 for x in range(0, 64)]
    for i in range(0, initial_size):
        individual[i] = randint(0, (1 << 8) - 1)
    return individual


def fiitness_function(individual):
    m = read_map()
    machine = VirtualMachine(500)
    curr = m['Start']
    fiitness = 1
    for step in machine.run_program(copy.deepcopy(individual)):
        if fiitness > m['Treasure_count']:
            return fiitness
        fiitness -= 0.0001
        curr = (curr[0] + steps[step][0], curr[1] + steps[step][1])
        if curr[0] < 0 or curr[1] < 0 or curr[0] > m['Height'] or curr[1] > m['Width']:
            return 0 if fiitness <= 0 else fiitness
        if m['Map'][curr[0]][curr[1]] == 'P':
            fiitness += 1
            m['Map'][curr[0]][curr[1]] = 'X'

    return 0 if fiitness <= 0 else fiitness


def exchange_mutation(individual):
    c1, c2 = randint(0, 63), randint(0, 63)
    while individual[c1] == 0:
        c1 = randint(0, 63)
    while individual[c2] == 0:
        c2 = randint(0, 63)
    temp = individual[c1]
    individual[c1] = individual[c2]
    individual[c2] = temp
    return individual


def add_mutation(individual):
    for i in range(0, len(individual)):
        if individual[i] == 0:
            individual[i] = randint(0, (1 << 8) - 1)
            return individual


def change_mutation(individual):
    c = randint(0, 63)
    try:
        individual[c] = randint(0, (1 << 8) - 1)
    except IndexError:
        pass
    return individual


def mutation(individual, pro):
    mutation_choice = numpy.random.choice([0, 1, 2], p=pro)

    if mutation_choice == 0:
        return exchange_mutation(individual)
    elif mutation_choice == 1:
        return change_mutation(individual)
    else:
        return individual


def crossover(father, mother):
    div = randint(0, 20)
    child = []
    for i in range(0, div):
        child.append(father[i])
    for i in range(div, 64):
        child.append(mother[i])
    return child


def crossover2(father, mother):
    child = []
    for i in range(0, len(father)):
        child.append(choice([father, mother])[i])
    return child


def requirement(fiitness):
    m = read_map()
    if fiitness >= m['Treasure_count'] :
        return True
    return False


def print_way(individual):
    m = read_map()
    machine = VirtualMachine(500)
    curr = m['Start']
    t_c = 0
    for step in machine.run_program(copy.deepcopy(individual)):
        if t_c == m['Treasure_count']:
            return
        curr = (curr[0] + steps[step][0], curr[1] + steps[step][1])
        print(curr)
        try:
            if curr[0] < 0 or curr[1] < 0 or curr[0] > m['Height'] or curr[1] > m['Width']:
                return
            if m['Map'][curr[0]][curr[1]] == 'P':
                t_c += 1
                print(t_c)
                m['Map'][curr[0]][curr[1]] = 'X'
        except:
            return
    return

