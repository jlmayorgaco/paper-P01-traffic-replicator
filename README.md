# P01 — Distributed Traffic Light Control via Replicator Dynamics  
### Bio-Inspired Evolutionary Game Control for Urban Intersections  
**Working Paper — 2025**

---

## 🧠 Overview
This repository contains all the code, simulations, datasets, literature review,
and LaTeX source files for the research paper:

> **“Distributed Traffic Light Control via Replicator Dynamics:  
> A Bio-Inspired Evolutionary Game Framework for Urban Intersections.”**

The goal of this work is to design and evaluate a **fully decentralized**,  
**adaptive**, and **mathematically grounded** traffic light controller based on  
**replicator dynamics**, inspired by evolutionary game theory.

Each intersection operates as an autonomous decision-making agent.  
Each signal phase (e.g., N–S, E–W) is treated as a “strategy.”  
Phase durations evolve dynamically according to:

- local queue measurements  
- local delay/stop metrics  
- replicator dynamics updating rule  
- optional weak communication with adjacent intersections

This allows the entire traffic network to **self-organize** without a  
central controller.

---

## 🚦 Why Replicator Dynamics for Traffic Control?
Replicator dynamics provide:

- **Distributed adaptation** (each intersection learns locally)
- **Smooth continuous adjustments** (avoids abrupt switching)
- **Inherent robustness** (evolutionary stability)
- **Low computational demand** (real-time feasible)
- **Biologically inspired coordination** (emergent patterns)

The controller adjusts green-time proportions based solely on local conditions.

---

## 📂 Repository Structure
paper-P01-traffic-replicator-2025/
│
├── paper/ # LaTeX source, figures, compiled PDFs
│ ├── main.tex
│ ├── sections/
│ └── figures/
│
├── code/ # Simulations, experiments, notebooks
│ ├── simulations/
│ │ └── traffic_sim.py
│ ├── notebooks/
│ │ └── exploration.ipynb
│ └── src/
│ └── replicator_controller.py
│
├── data/ # Synthetic and real traffic datasets
│ ├── raw/
│ └── processed/
│
├── literature-review/ # r-biblio-synth outputs and bib files
│ ├── r-bibliosynth/
│ └── bib/
│
├── results/ # Plots, tables, metrics from simulations
│
├── LICENSE
└── README.md

---

## 📊 Method Summary
At each intersection *i*, the controller maintains a probability vector  
representing the fraction of green time allocated to each phase:

\[
x_{i,k} \in [0,1], \quad \sum_k x_{i,k} = 1
\]

Phase payoffs are computed from queue lengths, waiting time, or throughput:

\[
f_{i,k} = -(\alpha \text{Queue}_{i,k} + \beta \text{Delay}_{i,k})
\]

Replicator update rule:

\[
x_{i,k}(t+1)
= x_{i,k}(t) +
\eta\, x_{i,k}(t)\left( f_{i,k}(t) - \bar{f}_i(t) \right)
\]

This results in:

- longer green times for overloaded directions,  
- shorter cycles for underused ones,  
- natural adaptation to changing demand.

---

## 🔧 Installation & Usage

### **1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/paper-P01-traffic-replicator-2025.git
cd paper-P01-traffic-replicator-2025
2. Install dependencies
bash
Copiar código
pip install -r requirements.txt
3. Run a basic simulation
bash
Copiar código
python code/simulations/traffic_sim.py
4. Explore via Jupyter Notebook
bash
Copiar código
jupyter notebook code/notebooks/exploration.ipynb
🧪 Experiments Included
Baseline fixed-time control

Actuated (sensor-based) control

Replicator-based distributed control (proposed)

Demand scenarios:

low / medium / high

sudden “rush hour” surges

anomalies (e.g. one blocked approach)

📈 Outputs
The results/ folder stores:

queue evolution plots

vehicle delay statistics

phase-ratio evolution

comparative performance tables

reproducible experiment logs

📚 Literature Review
The folder literature-review/ contains:

r-bibliosynth outputs

annotated bibliography

BibTeX files

This ensures the entire review pipeline is reproducible.

📄 License
This project is released under the MIT License.
See the LICENSE file for full details.

🧑‍💻 Author
Jorge Luis Mayorga
Full-Stack Engineer • Robotics & Control Researcher

⭐ Acknowledgements
Evolutionary Game Theory

Urban Traffic Control research community

Open-source tools and contributors

📬 Contact
For questions or collaboration opportunities:
EMAIL / GitHub / LinkedIn
