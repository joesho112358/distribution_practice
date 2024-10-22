# Poisson with parameter lambda_ (lambda_ > 0)
import math


class Poisson:

  def __init__(self, lambda_):
    self.lambda_ = lambda_
    self.negative_lambda = -1 * lambda_

  def probability_function(self, x):
    return (math.e**self.negative_lambda) * (self.lambda_ ** x) / math.factorial(x)

  def expected_value(self):
    return self.lambda_

  def variance(self):
    return self.lambda_


