"""
Simple Traffic Simulation for Replicator Dynamics Controller
Run:
    python traffic_sim.py
"""

import numpy as np
from src.network import Network

def main():
    net = Network(names=["A", "B"], num_phases=2)

    T = 200  # time steps
    log = []

    for t in range(T):
        arrivals_A = np.random.poisson([8, 4])   # NS, EW
        arrivals_B = np.random.poisson([5, 10])  # NS, EW

        outputs = net.step([arrivals_A, arrivals_B])
        log.append(outputs)

        if t % 20 == 0:
            print(f"t={t} | A greens={outputs['A']['green_split']} | queues={outputs['A']['queues']}")

    print("Simulation complete.")

if __name__ == "__main__":
    main()
