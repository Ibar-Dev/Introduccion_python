import random

class Individual:
    def __init__(self, genotype):
        self.genotype = genotype

class Population:
    def __init__(self, size, individual_length):
        self.individuals = [[random.choice([0, 1]) for _ in range(individual_length)] for _ in range(size)]

    def roulette_wheel_selection(self):
        return random.choice(self.individuals)

    def one_point_crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child1_genotype = parent1[:crossover_point] + parent2[crossover_point:]
        child2_genotype = parent2[:crossover_point] + parent1[crossover_point:]
        return child1_genotype, child2_genotype

    def bit_flip_mutation(self, individual, mutation_rate):
        return [1 - gene if random.random() < mutation_rate else gene for gene in individual]

# Ejemplo de uso:
population = Population(size=100, individual_length=10)
for generation in range(100):
    parent1 = population.roulette_wheel_selection()
    parent2 = population.roulette_wheel_selection()
    child1, child2 = population.one_point_crossover(parent1, parent2)
    child1 = population.bit_flip_mutation(child1, mutation_rate=0.01)
    child2 = population.bit_flip_mutation(child2, mutation_rate=0.01)
    # Actualizar la población con los nuevos individuos
