# Distributed Traffic Light Control via Replicator Dynamics  
### Bio-Inspired Evolutionary Game Control for Urban Intersections  
**Working Paper — 2025**

---

## Overview

The goal of this work is to design and evaluate a **fully decentralized**,  
**adaptive**, and **mathematically grounded** traffic light controller based on  
**replicator dynamics**, inspired by evolutionary game theory. Each intersection operates as an autonomous decision-making agent. Each signal phase (e.g., N–S, E–W) is treated as a “strategy.” Phase durations evolve dynamically according to:

- local queue measurements  
- local delay/stop metrics  
- replicator dynamics updating rule  
- optional weak communication with adjacent intersections

This allows the entire traffic network to **self-organize** without a  
central controller.

---

## Why Replicator Dynamics for Traffic Control?
Replicator dynamics provide:

- **Distributed adaptation** (each intersection learns locally)
- **Smooth continuous adjustments** (avoids abrupt switching)
- **Inherent robustness** (evolutionary stability)
- **Low computational demand** (real-time feasible)
- **Biologically inspired coordination** (emergent patterns)

The controller adjusts green-time proportions based solely on local conditions.
