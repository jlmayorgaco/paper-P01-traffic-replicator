"""
Traffic Network (Optional)
Manages multiple intersections
"""

from intersection import Intersection

class Network:
    def __init__(self, names, num_phases=2):
        self.intersections = [
            Intersection(name, num_phases=num_phases)
            for name in names
        ]

    def step(self, arrivals_list):
        """
        arrivals_list: list of arrival vectors, one per intersection
        """
        outputs = {}
        for inter, arr in zip(self.intersections, arrivals_list):
            green = inter.step(arr)
            outputs[inter.name] = {
                "queues": inter.queues.copy(),
                "green_split": green.copy()
            }
        return outputs
