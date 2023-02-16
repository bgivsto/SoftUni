population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

if min_wealth * len(population) > sum(population):
    print("No equal distribution possible")
else:
    for i in range(len(population) - 1):
        if population[i] < min_wealth:
            needed = min_wealth - population[i]
            population[population.index(max(population))] -= needed
            population[i] += needed

    print(population)