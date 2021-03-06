import random
import numpy as np


class ThompsonSampling():
  def __init__(self, n_arms):
    self.n_arms = n_arms
    self.counts = [0] * n_arms
    self.values = [0.0] * n_arms
    self.s_counts = [0] * n_arms
    self.alpha = [2] * n_arms
    self.beta = [2] * n_arms

  def reset(self):
    self.counts = [0] * self.n_arms
    self.values = [0.0] * self.n_arms
    self.s_counts = [0] * self.n_arms
    self.alpha = [1] * self.n_arms
    self.beta = [1] * self.n_arms

  def select_arm(self):
    rho = [random.betavariate(self.alpha[i], self.beta[i]) for i in range(self.n_arms)]
    return rho

  def update(self, chosen_arm, reward):
    self.counts[chosen_arm] += 1
    self.alpha[chosen_arm] += reward
    self.beta[chosen_arm] += 1 - reward
    n = float(self.counts[chosen_arm])
    value = self.values[chosen_arm]
    new_value = ((n - 1) / n) * value + (1 / n) * reward
    self.values[chosen_arm] = new_value
