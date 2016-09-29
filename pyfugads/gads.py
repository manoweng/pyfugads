#!/usr/bin/env python3

from math import sqrt
import numpy as np
import pandas as pd


class GADS():
    """Class to generate the DSNSF from an input."""

    def __init__(self, dataset, pop_size, generations, crossover_rate,
                 mut_prob, mut_rate, selection=0):
        """Just defines the GA parameters."""
        self.dataset = np.transpose(dataset)
        self.population_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_probability = mut_prob
        self.mutation_rate = mut_rate
        self.selection_method = selection

        self.run(0)

    def run(self, idx):
        """Runs the gads of a single interval."""
        self.idx = idx
        self.best_chromosome = np.zeros(self.population_size)
        self.best_fitness = np.zeros(self.population_size)
        self.generate_population()
        self.population_fitness()

        best_idx = np.argmax(self.fitness)
        self.best_fitness[0] = self.fitness[best_idx]
        self.best_chromosome[0] = self.population[best_idx]

        selected = self.selection()
        print(selected)

    def generate_population(self):
        """Generate initial population based on input."""
        self.inferior_limit = np.min(self.dataset[self.idx])
        self.superior_limit = np.max(self.dataset[self.idx])
        self.population = np.random.uniform(self.inferior_limit,
                                            self.superior_limit,
                                            self.population_size)

    def calculate_fitness(self, chromosome):
        """Calculates the fitness of a chromosome."""
        distance = 0.0
        for point in self.dataset[self.idx]:
            distance += (point - chromosome) ** 2
        return ((self.inferior_limit+self.superior_limit) / sqrt(distance))

    def population_fitness(self):
        """Calculates the fitness of a population."""
        fitness = np.array(list(map(self.calculate_fitness, self.population)))
        self.fitness = fitness

    def tournament(self):
        """Selects a chromosome with a tournament."""
        return np.random.choice(self.population)

    def selection(self):
        """Returns a population of selected chromosomes."""
        selected = [self.tournament() for i in range(self.population_size)]
        return np.array(selected)


gads = GADS([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
            20, 50, 0.9, 0.03, 0.01)
