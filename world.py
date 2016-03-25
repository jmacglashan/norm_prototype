__author__ = 'alerus'

import random
from sets import Set

class World:

    def __init__(self, n, score, population):
        self.n = n
        self.score = score
        self.population = population
        self.game = 0

    def run_game(self):
        indices = range(len(self.population))
        random.shuffle(indices)
        for i in xrange(0, len(self.population) / 2, 2):
            a0 = self.population[indices[i]]
            a1 = self.population[indices[i+1]]
            for j in xrange(self.n):
                a0.start_game()
                a1.start_game()

                p0 = a0.norm
                p1 = a1.norm

                a0.receive_result(p1)
                a1.receive_result(p0)

    def run_games(self, k):
        for i in xrange(k):
            self.print_statistics()
            self.run_game()
            self.game += 1
        print 'Finished.'
        self.print_statistics()

    def print_statistics(self):
        score = self.score
        scores = [score(a.norm) for a in self.population]
        best_score = max(scores)

        score_sum = 0
        for a in self.population:
            score_sum += score(a.norm)
        avg = score_sum / len(self.population)

        norms = [a.norm for a in self.population]
        u_norms = Set(norms)
        #counts = [norms.count(key) for key in u_norms]
        #max_count = max(counts)

        print self.game, best_score, avg, len(u_norms)


