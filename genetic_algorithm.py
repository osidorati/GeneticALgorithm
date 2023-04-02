import random
import math

# Функция приспособленности
def fitness_func(x):
    return 10**(2*x)*math.sin(x)

# Создание начальной популяции
def generate_population(population_size, chromosome_length):
    population = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population

# Расчет значения функции приспособленности для каждого кандидата в популяции
def evaluate_population(population):
    fitness_values = []
    for chromosome in population:
        x = decode_chromosome(chromosome)
        fitness_values.append(fitness_func(x))
    return fitness_values

# Декодирование хромосомы в значение x
def decode_chromosome(chromosome):
    n = len(chromosome)
    decimal_value = 0
    for i in range(n):
        decimal_value += chromosome[i] * (2**(n-i-1))
    x = decimal_value / (2**n-1) * 0.31
    return x

# Турнирная селекция
def tournament_selection(population, fitness_values, tournament_size):
    tournament = random.sample(range(len(population)), tournament_size)
    winner_index = tournament[0]
    for i in tournament[1:]:
        if fitness_values[i] > fitness_values[winner_index]:
            winner_index = i
    return population[winner_index]

# Кроссинговер
def crossover(parent1, parent2, crossover_probability):
    if random.random() < crossover_probability:
        crossover_point = random.randint(1, len(parent1)-1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    else:
        return parent1, parent2

# Мутация
def mutate(chromosome, mutation_probability):
    for i in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Генетический алгоритм
def genetic_algorithm(population_size, chromosome_length, tournament_size, crossover_probability, mutation_probability, num_generations):
    population = generate_population(population_size, chromosome_length)
    for i in range(num_generations):
        fitness_values = evaluate_population(population)
        parents = [tournament_selection(population, fitness_values, tournament_size) for i in range(population_size)]
        offspring = []
        for j in range(0, population_size-1, 2):
            parent1 = parents[j]
            parent2 = parents[j+1]
            child1, child2 = crossover(parent1, parent2, crossover_probability)
            child1 = mutate(child1, mutation_probability)
            child2 = mutate(child2, mutation_probability)
            offspring.append(child1)
            offspring.append(child2)
        population = offspring
        best_fitness = max(fitness_values)
        best_chromosome = population[fitness_values.index(best_fitness)-1]
        best_x = decode_chromosome(best_chromosome)
        print(f"Поколение {i+1}:")
        print(f"Лучшее решение: x = {best_x}, f(x) = {best_fitness}")
        print("Хромосомы:")
        for chromosome in population:
            x = decode_chromosome(chromosome)
            fitness = fitness_func(x)
            print(f"{chromosome} -> x = {x}, f(x) = {fitness}")
        print("="*20)

# Задаем параметры генетического алгоритма
population_size = 11
chromosome_length = 5
tournament_size = 2
crossover_probability = 1
mutation_probability = 0.008
num_generations = 5

# Запускаем генетический алгоритм
genetic_algorithm(population_size, chromosome_length, tournament_size, crossover_probability, mutation_probability, num_generations)
