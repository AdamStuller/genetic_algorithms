def reproduce(x, y):
    pass


def selection(population, fiitness_function):
    pass


def mutate(x):
    pass


def genetic_algorithm(population, fiitness_function):
    for i in range(0, 10000):
        new_population = set()
        for j in range(0, len(population)):
            father = selection(population, fiitness_function)
            mother = selection(population, fiitness_function)
            child = reproduce(father, mother)
            if True:
                child = mutate(child)
            new_population.add(child)
        population = new_population
