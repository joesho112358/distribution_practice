# Uniform Distribution on N points (N > 0)
from math import exp


class UniformDiscrete:

  def __init__(self, N):
    # we expect 1, 2, 3, ..., N
    self.N = N

  def probability_function(self, _x):
    return 1 / self.N

  def expected_value(self):
    # since 1 + 2 + 3 + ... + N = N(N + 1)/2 and p(n) = 1/N
    # sum(range(N)) / N = N(N + 1)/2N = (N + 1)/2
    return (self.N + 1) / 2

  def variance(self):
    return (self.N**2 - 1) / 12

  def moment_generating_function(self, t):
    numerator = exp(t) * (exp(self.N * t) - 1)
    denominator = self.N * (exp(t) - 1)
    return numerator / denominator

  def probability_generating_function(self, t):
    numerator = t * ((t ** self.N) - 1)
    denominator = self.N * (t - 1)
    return numerator / denominator


