"""
Intersection Model
Represents a traffic light with queue dynamics
"""

import numpy as np
from replicator_controller import ReplicatorController

class Intersection:
    def __init__(self, name, num_phases=2, cycle_time=60):
        self.name = name
        self.num_phases = num_phases
        self.controller = ReplicatorController(num_phases=num_phases)
        self.cycle_time = cycle_time

        # state
        self.queues = np.zeros(num_phases)
        self.delays = np.zeros(num_phases)

    def update_state(self, arrivals, discharge_rate):
        """
        arrivals: vehicles arriving this timestep per phase
        discharge_rate: vehicles that can leave when phase is active
        """
        # accumulate queues
        self.queues += arrivals

        # discharge based on green proportion
        green_split = self.controller.x
        served = green_split * discharge_rate
        self.queues = np.maximum(self.queues - served, 0)

        # estimate delay ~ queue size (simplified)
        self.delays = self.queues.copy()

    def update_controller(self):
        self.controller.update(self.queues, self.delays)

    def step(self, arrivals, discharge_rate=20):
        """
        arrivals: array of arriving cars
        """
        self.update_state(arrivals, discharge_rate)
        self.update_controller()
        return self.controller.x
