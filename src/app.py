from evolution import genetic_algorithm
from treasure_finder import fiitness_function, mutation, crossover, requirement, print_way, generate_population


def main():
    top = genetic_algorithm(generate_population(150, 64), fiitness_function, mutation, crossover, requirement)
    print(top['Fiitness'])
    print(top['Object'])
    print_way(top['Object'])


if __name__ == "__main__":
    main()
