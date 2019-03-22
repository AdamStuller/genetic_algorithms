import numpy


def reproduce(x, y, reproduce_fn):
    return reproduce_fn(x, y)


def roulette_pro_dist(fiitness_arr):
    s = sum(fiitness_arr)
    return list(map(lambda x: x / s, fiitness_arr))


def selection(population):
    fiitness_arr = list(map(lambda x: x['Fiitness'], population))
    probability_distribution = roulette_pro_dist(fiitness_arr)
    return numpy.random.choice(population, p=probability_distribution)


def test_selection():
    test_population = [{'Object': 1, 'Fiitness': 20}, {'Object': 2, 'Fiitness': 30}, {'Object': 3, 'Fiitness': 100}]
    assert selection(test_population)['Object'] in set(list(map(lambda x: x['Object'], test_population)))


def mutate(x, mutate_fn):
    return mutate_fn(x)

def max_fiitness(population):
    fiit = list(map(lambda x: x['Fiitness'], population))
    return max(fiit)


def genetic_algorithm(population, fiitness_fn, mutate_fn, reproduce_fn, requirement_fn):
    for i in range(0, 10000):
        new_population = []

        population = list(reversed(sorted(population, key=lambda x: x['Fiitness'])))
        print(max_fiitness(population))
        # print(population)

        for j in range(0, 5):
            new_population.append(population[j])

        for j in range(0, len(population) - 5):
            child = {}
            father = selection(population)
            mother = selection(population)
            child['Object'] = reproduce(father['Object'], mother['Object'], reproduce_fn)

            child['Object'] = mutate(child['Object'], mutate_fn)

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
