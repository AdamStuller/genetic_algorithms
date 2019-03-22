import numpy


def roulette_pro_dist(fiitness_arr):
    s = sum(fiitness_arr)
    return list(map(lambda x: x / s, fiitness_arr))


def selection(population):
    fiitness_arr = list(map(lambda x: x['Fiitness'], population))
    probability_distribution = roulette_pro_dist(fiitness_arr)
    return numpy.random.choice(population, p=probability_distribution)


def max_fiitness(population):
    fiit = list(map(lambda x: x['Fiitness'], population))
    return max(fiit)


def average_fiitness(population):
    fiit = list(map(lambda x: x['Fiitness'], population))
    return sum(fiit)/len(fiit)


def genetic_algorithm(population, fiitness_fn, mutate_fn, reproduce_fn, requirement_fn):
    for i in range(0, 10000):
        new_population = []

        population = list(reversed(sorted(population, key=lambda x: x['Fiitness'])))
        print('Max: ' + str(max_fiitness(population)))
        print('Avg: ' + str(average_fiitness(population)))
        # print(population)

        for j in range(0, 8):
            new_population.append(population[j])

        for j in range(0, len(population) - 8):
            child = {}
            father = selection(population)
            mother = selection(population)
            child['Object'] = reproduce_fn(father['Object'], mother['Object'])

            child['Object'] = mutate_fn(child['Object'])

            child['Fiitness'] = fiitness_fn(child['Object'])
            if requirement_fn(child['Fiitness']):
                return child

            new_population.append(child)

        # print(population)
        population = new_population

    return {
        'Object': None,
        'Fiitness': None
    }


def test_selection():
    test_population = [{'Object': 1, 'Fiitness': 20}, {'Object': 2, 'Fiitness': 30}, {'Object': 3, 'Fiitness': 100}]
    assert selection(test_population)['Object'] in set(list(map(lambda x: x['Object'], test_population)))
