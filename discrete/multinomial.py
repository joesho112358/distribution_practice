# Multinomial with n >= 1 and 0 <= p1, p2, p3, ..., pk <= 1 and sum(pi) = 1
# n identical repeated trials with probability p and failure q = 1 - p
from math import factorial


class Multinomial:

  def __init__(self, n, p_list):
    self.n = n
    self.p_list = p_list
    self.q_list = [ 1 - p for p in p_list ]

  def probability_function(self, x_list):
    denominator = 1
    for x in x_list:
      denominator *= factorial(x)
    probability_factor = 1
    for i, p in enumerate(self.p_list):
      probability_factor *= p ** x_list[i]
    return (factorial(self.n) / denominator) * probability_factor

  def expected_value(self):
    return_list = []
    for p in self.p_list:
      return_list.append(self.n * p)
    return return_list

  def variance(self):
    return_list = []
    for i, p in enumerate(self.p_list):
      return_list.append(self.n * p * self.q_list[i])
    return return_list

