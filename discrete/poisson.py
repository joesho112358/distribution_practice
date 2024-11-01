# Poisson with parameter lambda_ (lambda_ > 0)
from math import exp, factorial


class Poisson:

  def __init__(self, lambda_):
    self.lambda_ = lambda_
    self.negative_lambda = -1 * lambda_

  def probability_function(self, x):
    return (exp(self.negative_lambda)) * (self.lambda_ ** x) / factorial(x)

  def expected_value(self):
    return self.lambda_

  def variance(self):
    return self.lambda_

  def moment_generating_function(self, t):
    return exp(self.lambda_ * (exp(t) - 1))

  def probability_generating_function(self, t):
    return exp(self.lambda_ * (t - 1))


