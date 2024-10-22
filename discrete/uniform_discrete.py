# Uniform Distribution on N points (N > 0)

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


