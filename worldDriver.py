__author__ = 'alerus'

from normAgent import NormAgent
from world import World

def score(norm):
    return min(sum(norm), 2)


population = [NormAgent(10, score) for i in xrange(30)]
world = World(20, score, population)

world.run_games(1000)
