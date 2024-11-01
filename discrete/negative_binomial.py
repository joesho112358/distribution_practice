# Negative Binomial with r > 0 1 and 0 <= p <= 1
# n identical repeated trials with probability p and failure q = 1 - p
from math import comb, exp


class NegativeBinomial:

  def __init__(self, r, p):
    self.r = r
    self.p = p
    self.q = 1 - p

  def probability_function(self, x):
    return comb(self.r + x - 1, x) * (self.p ** self.r) * (self.q ** x)
    # equivalent to:
    # return comb(self.r + x - 1, r - 1) * (self.p ** self.r) * (self.q ** x)

  def expected_value(self):
    return self.r * self.q / self.p

  def variance(self):
    return self.r * self.q / (self.p ** 2)

  def moment_generating_function(self, t):
    return (self.p / (1 - (1 - self.p) * exp(t))) ** self.r

  def probability_generating_function(self, t):
    return (self.p / (1 - (1 - self.p) * t)) ** self.r
