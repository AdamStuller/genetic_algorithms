import numpy


def roulette(fiitness_arr):
    s = sum(fiitness_arr)
    return list(map(lambda x: x / s, fiitness_arr))


def roulette_selection(population):
    fiitness_arr = list(map(lambda x: x['Fiitness'], population))
    probability_distribution = roulette(fiitness_arr)
    return numpy.random.choice(population, p=probability_distribution)


def tournament_selection(population, prob=0.3):
    for i in range(0, len(population)):
        main_p = prob*((1 - prob)**i)
        if numpy.random.choice([population[i], False], p=[main_p, 1-main_p]):
            return population[i]
    return population[0]


def max_fiitness(population):
    fiit = list(map(lambda x: x['Fiitness'], population))
    return max(fiit)


def average_fiitness(population):
    fiit = list(map(lambda x: x['Fiitness'], population))
    return sum(fiit)/len(fiit)


def anneal(p, time, c_avg, p_avg):
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


def genetic_algorithm(population, fiitness_fn, vm, mutate_fn, reproduce_fn, requirement_fn, mutate_pro, m_name):
    averages = [27]

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

            child['Fiitness'] = fiitness_fn(child['Object'], vm, m_name)
            if requirement_fn(child['Fiitness'], m_name):
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

