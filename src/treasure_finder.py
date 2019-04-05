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


def generate_population(n, k, vm, m_name):
    """
    This method creates new list of individuals
    :param n: int
                number of individuals in first generation
    :param k: int
                minimal number of commands in each individual
    :param vm: VirtualMachine
    :return: int[]
        population of size n
    """
    population = []
    for i in range(0, n):
        individual = generate_individual(randint(k, 63))
        population.append(individual)
    pop = list(map(lambda x: {'Object': x, 'Fiitness': fiitness_function(x, vm, m_name)}, population))
    print(pop)
    return pop


def generate_individual(initial_size):
    """
    Creates individual
    :param initial_size: int
                    Number of non-zero commands in individual
    :return: int []
        Individual, list of integers, each representing single command for virtual machine
    """
    individual = [0 for x in range(0, 64)]
    for i in range(0, initial_size):
        individual[i] = randint(0, (1 << 8) - 1)
    return individual


def fiitness_function(individual, machine, m_name):
    """
    Method to evaluate individual's fitness, runs virtual machine in itself and compares the
    result of program with map. Fitness starts at 1 and adds 1 for each found treasure and subtracts
    0.0001 for each field. That way, fitness function is made up by both, number of treachures and
    length of solution
    :param individual: int []
                    Program to be run on virtual machine
    :param machine: VirtualMachine
    :param m: str[][]
    :return: int
            Fitness of individual- number between up to 1 + number of treasures
    """
    m = read_map(m_name)
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
    """
    Mutation, that exchanges two random commands from individual
    :param individual: int []
                Program for virtual machine
    :return: int[]
            Mutated individual
    """
    c1, c2 = randint(0, 63), randint(0, 63)
    while individual[c1] == 0:
        c1 = randint(0, 63)
    while individual[c2] == 0:
        c2 = randint(0, 63)
    temp = individual[c1]
    individual[c1] = individual[c2]
    individual[c2] = temp
    return individual


def change_mutation(individual):
    """
    Mutation that changes one random command from individual
    :param individual: int[]
                Program for virtual machine
    :return: int[]
        mutated individual
    """
    c = randint(0, 63)
    individual[c] = randint(0, (1 << 8) - 1)
    return individual


def mutation(individual, pro):
    """
    Method that examines probability of each kind of mutation and randomly chooses either one of then
    or no mutation at all
    :param individual: int[]
                program to virtual machine
    :param pro:     int[]
                probability distribution
    :return: int []
        Either mutated or old individual
    """
    mutation_choice = numpy.random.choice([0, 1, 2], p=pro)

    if mutation_choice == 0:
        return exchange_mutation(individual)
    elif mutation_choice == 1:
        return change_mutation(individual)
    else:
        return individual


def crossover(father, mother):
    """
    Crossover method that randomly divides parents and creates their child by concatenating
    their respective parts
    :param father: int[]
                program individual
    :param mother: int[]
                program individual
    :return:int[]
            child individual
    """
    div = randint(0, 20)
    child = []
    for i in range(0, div):
        child.append(father[i])
    for i in range(div, 64):
        child.append(mother[i])
    return child


def crossover2(father, mother):
    """
    Another crossover method, that creates new individual taking odd commands from one parent and
    even from another
    :param father: int[]
    :param mother: int[]
    :return: int[]
    """
    child = []
    for i in range(0, len(father)):
        child.append(choice([father, mother])[i])
    return child


def requirement(fiitness, m_name):
    """
    Determines if current fiitness is enogh
    :param fiitness: int
                Current fitness
    :param m_name: str
                Name of the map to be used
    :return: bool
        true if it is enough else false
    """
    m = read_map(m_name)
    return True if fiitness >= m['Treasure_count'] else False


def print_way(individual, m_name):
    """
    Prints found way
    :param individual: int
    """
    m = read_map(m_name)
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

