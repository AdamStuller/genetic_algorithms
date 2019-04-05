from evolution import genetic_algorithm
from treasure_finder import *
import matplotlib.pyplot as plt


def main():
    top, gen, avgs = genetic_algorithm(generate_population(150, 32), fiitness_function, mutation, crossover2, requirement, [0.4, 0.3, 0.3])
    print(top['Fiitness'])
    print(top['Object'])
    print_way(top['Object'])
    plt.plot([x for x in range(0, gen + 1)], avgs)
    plt.show()




if __name__ == "__main__":
    main()

