__author__ = 'alerus'

import random

class NormAgent:

    def __init__(self, n, score, beta=0.5, alpha=0.1):
        self.beta = beta
        self.norm = tuple([random.randint(0, 1) for i in xrange(n)])
        self.score = score
        self.game = 0
        self.alpha = alpha
        self.have_matched = False
        self.lead_last = True

    def start_game(self):
        self.game = 0
        self.have_matched = False
        self.lead_last = True

    def receive_result(self, p_norm):
        lead = self.lead(p_norm)
        self.update_beta(p_norm, lead)

        self.have_matched = self.norms_equal(p_norm)
        self.lead_last = lead
        self.game += 1
        if not lead:
            self.norm = tuple([xi for xi in p_norm])

    def lead(self, p_norm):
        score = self.score

        if self.norms_equal(p_norm):
            return True

        if score(self.norm) > score(p_norm):
            return True

        if score(self.norm) < score(p_norm):
            return False

        roll = random.random()
        if roll < self.beta:
            return True

        return False

    def update_beta(self, p_norm, lead):
        if not lead or not self.norms_equal(p_norm):
            self.beta = self.beta + self.alpha * -self.beta
        elif self.norms_equal(p_norm) and (not self.have_matched and self.lead_last):
            self.beta = self.beta + self.alpha * (1. - self.beta)

    def norms_equal(self, p_norm):
        for i in xrange(len(self.norm)):
            if self.norm[i] != p_norm[i]:
                return False
        return True
