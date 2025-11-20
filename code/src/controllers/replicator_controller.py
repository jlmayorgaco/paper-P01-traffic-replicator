"""
Replicator Dynamics Controller for Traffic Light Phases
Author: Jorge L. Mayorga
Date: 2025
"""

import numpy as np

class ReplicatorController:
    def __init__(self, num_phases=2, alpha=1.0, beta=1.0, eta=0.05):
        """
        num_phases : number of traffic signal phases
        alpha      : weight for queue length
        beta       : weight for delay
        eta        : learning rate
        """
        self.num_phases = num_phases
        self.alpha = alpha
        self.beta = beta
        self.eta = eta

        # initial strategy distribution (equal green split)
        self.x = np.ones(num_phases) / num_phases

    def compute_payoffs(self, queues, delays):
        """
        Compute fitness/payoff for each phase.
        More queue or delay = lower payoff.

        queues: list or array of queue lengths for each phase
        delays: list or array of average delays for each phase
        """
        queues = np.array(queues)
        delays = np.array(delays)
        
        # payoff is negative: lower is better, replicator will maximize
        f = -(self.alpha * queues + self.beta * delays)
        return f

    def update(self, queues, delays):
        """
        Perform one replicator dynamics update step.
        """
        f = self.compute_payoffs(queues, delays)
        f_avg = np.dot(self.x, f)

        # continuous replicator discretized
        x_new = self.x + self.eta * self.x * (f - f_avg)

        # enforce valid simplex
        x_new = np.clip(x_new, 0, None)
        if x_new.sum() == 0:
            x_new = np.ones(self.num_phases) / self.num_phases
        else:
            x_new /= x_new.sum()

        self.x = x_new
        return self.x
