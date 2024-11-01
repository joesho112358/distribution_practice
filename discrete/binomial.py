# Binomial with n >= 1 and 0 <= p <= 1
# n identical repeated trials with probability p and failure q = 1 - p
from math import comb, exp


class Binomial:

  def __init__(self, n, p):
    self.n = n
    self.p = p
    self.q = 1 - p

  def probability_function(self, x):
    return comb(self.n, x) * (self.p ** x) * (self.q ** (self.n - x))

  def expected_value(self):
    return self.n * self.p

  def variance(self):
    return self.n * self.p * self.q

  def moment_generating_function(self, t):
    return (1 - self.p + self.p * exp(t)) ** self.n

  def probability_generating_function(self, t):
    return (1 - self.p + self.p * t) ** self.n

