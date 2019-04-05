from evolution import genetic_algorithm
from treasure_finder import *
from virtual_machine import VirtualMachine
from map_generator import read_map
import matplotlib.pyplot as plt
from copy import deepcopy
from config import __config_values as config


def main():
    machine = VirtualMachine(config.get('machine_limit'))
    m = read_map(config.get('map_name'))
    pop = generate_population(config.get('population_size'), config.get('ind_min_size'), machine, deepcopy(m))
    mutation_probability = config.get('mutation_probability')
    el = config.get('elitarism_size')

    top, gen, avgs = genetic_algorithm(pop, fiitness_function, machine, mutation, crossover, requirement, mutation_probability, m, el)
    print_way(top['Object'], deepcopy(m))

    plt.plot([x for x in range(0, gen + 1)], avgs)
    plt.show()




if __name__ == "__main__":
    main()

