# Hyper Geometric distribution with parameters M, K, and n
# M > 0, 0 <= K <= M, 1 <= n <= M
from math import comb


class HyperGeometric:

  def __init__(self, M, K, n):
    self.M = M
    self.K = K
    self.n = n

  def probability_function(self, x):
    if x >= min(self.n, self.K):
      return 0
    if x < self.n - (self.M - self.K):
      return 0

    return comb(self.K, x) * comb(self.M - self.K, self.n - x) / comb(self.M, self.n)

  def expected_value(self):
    return self.n * self.K / self.M

  def variance(self):
    return ((self.n * self.K * (self.M - self.K) * (self.M - self.n)) /
            ((self.M ** 2) * (self.M - 1)))

