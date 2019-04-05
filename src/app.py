from evolution import genetic_algorithm
from treasure_finder import *
from virtual_machine import VirtualMachine
from map_generator import read_map
import matplotlib.pyplot as plt
from copy import deepcopy


def main():
    machine = VirtualMachine(500)
    m = read_map('map1.txt')
    pop = generate_population(150, 32, machine, deepcopy(m))
    mutation_probability = [0.4, 0.3, 0.3]
    top, gen, avgs = genetic_algorithm(pop, fiitness_function, machine, mutation, crossover, requirement, mutation_probability, m)
    print(top['Fiitness'])
    print(top['Object'])
    print_way(top['Object'], deepcopy(m))
    plt.plot([x for x in range(0, gen + 1)], avgs)
    plt.show()




if __name__ == "__main__":
    main()

