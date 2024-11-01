# Geometric distribution with parameter 0 <= p <= 1
# Repeated trials with probability p and failure q = 1 - p
from math import exp

class Geometric:

  def __init__(self, p):
    self.p = p
    self.q = 1 - p

  def probability_function(self, x):
    return (self.q ** x) * self.p

  def expected_value(self):
    return self.q / self.p

  def variance(self):
    return self.q / (self.p ** 2)

  def moment_generating_function(self, t):
    return self.p / (1 - (1 - self.p) * exp(t))

  def probability_generating_function(self, t):
    return self.p / (1 - (1 - self.p) * t)

