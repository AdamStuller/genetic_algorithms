import numpy
from copy import deepcopy


def roulette(fiitness_arr):
    """
    This method creates list of all individuals with their respective probability of being
    chosen for crossover
    :param fiitness_arr: list
            list of fitnesses of each individual
    :return:list
            of probabilities
    """
    s = sum(fiitness_arr)
    return list(map(lambda x: x / s, fiitness_arr))


def roulette_selection(population):
    """
    Method of selection roulette divides probability among individuals proportionally
    to their fiitness
    :param population: list
            of all individuals in given generation
    :return: list
            one individual
    """
    fiitness_arr = list(map(lambda x: x['Fiitness'], population))
    probability_distribution = roulette(fiitness_arr)
    return numpy.random.choice(population, p=probability_distribution)


def tournament_selection(population, prob=0.3):
    """
    Tournament selection either chooses the best individual with probability p passed as argument
    or the next one with probability given by formula in the method. Finally after all indiviuals,
    if no one is selected, it returns the best one.
    :param population: list
    :param prob: int
    :return: list
        individual
    """
    for i in range(0, len(population)):
        main_p = prob*((1 - prob)**i)
        if numpy.random.choice([population[i], False], p=[main_p, 1-main_p]):
            return population[i]
    return population[0]


def max_fiitness(population):
    """
    Counts maximal fitness in given population
    :param population: list
    :return:int
        maximal fitness
    """
    fiit = list(map(lambda x: x['Fiitness'], population))
    return max(fiit)


def average_fiitness(population):
    """
    Counts average fitness in given population
    :param population: list
    :return: int
        average fitness
    """
    fiit = list(map(lambda x: x['Fiitness'], population))
    return sum(fiit)/len(fiit)


def anneal(p, time, c_avg, p_avg):
    """
    Counts current probability of mutation
    :param p: int       => last probability
    :param time: int    => number of iteration in main loop
    :param c_avg: int   => current average fitness
    :param p_avg: int   => previous average fitness
    :return: list of probabilities of individual mutations
    """
    p[-1] = 1
    for i in range(0, len(p)-1):
        sup_p = p[i] - (time / 10000)
        p[i] = 0.1 if sup_p <= 0.05 else sup_p
        p[-1] -= p[i]

    if abs(c_avg - p_avg) < 0.02:
        for i in range(0, len(p)-1):
            p[i] = 1/(len(p)-1)
        p[-1] = 0
    return p


def genetic_algorithm(population, fiitness_fn, vm, mutate_fn, reproduce_fn, requirement_fn, mutate_pro, m):
    """
    Main method of project, represent evolution algorithm
    :param population: list     => starting population of individuals
    :param fiitness_fn: fn      => function to calculate fiitness
    :param vm: VirtualMachine   => Virtual machine on which all programs are run
    :param mutate_fn: fn        => Mutation function
    :param reproduce_fn: fn     => Crossover function
    :param requirement_fn: fn   => Function checking ic fitness is good enough
    :param mutate_pro:  list    => Probability distribution
    :param m: list              => Map on which solution is to be found
    :return: dict, int, list
        Best individual, number of generations it took to find him and list of average fitnesses
    """
    averages = [27]  # custom first value, is used in anneal calculation, as it needs -2 item

    for i in range(0, 10000):
        new_population = []

        population = list(reversed(sorted(population, key=lambda x: x['Fiitness'])))
        print('Population #: ' + str(i) + '\nMax: ' + str(max_fiitness(population)))
        avg = average_fiitness(population)
        print('Avg: ' + str(avg))
        averages.append(avg)

        for j in range(0, 10):
            population[j]['Object'] = mutate_fn(population[j]['Object'], mutate_pro) # this can be turned off
            new_population.append(population[j])

        for j in range(0, len(population) - 10):
            child = {}
            father = roulette_selection(population)
            mother = roulette_selection(population)

            child['Object'] = reproduce_fn(father['Object'], mother['Object'])
            child['Object'] = mutate_fn(child['Object'], mutate_pro)

            child['Fiitness'] = fiitness_fn(child['Object'], vm, deepcopy(m))
            if requirement_fn(child['Fiitness'], deepcopy(m)):
                return child, i, [averages[x] for x in range(1, len(averages))]

            new_population.append(child)
        mutate_pro = anneal(mutate_pro, i, averages[-1], averages[-2])
        population = new_population

    return {
        'Object': None,
        'Fiitness': None
    }, i, averages


def test_selection():
    test_population = [{'Object': 1, 'Fiitness': 20}, {'Object': 2, 'Fiitness': 30}, {'Object': 3, 'Fiitness': 100}]
    assert roulette_selection(test_population)['Object'] in set(list(map(lambda x: x['Object'], test_population)))

