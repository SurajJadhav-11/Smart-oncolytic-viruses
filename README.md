# Smart-oncolytic-viruses-
# Dual-Control Safety Architecture for KRAS-Targeted Oncolytic Virotherapy

## Project Overview
This repository contains the computational modeling and simulation framework for a "Smart" Oncolytic Virus (OV) designed to target KRAS-mutant adenocarcinoma. The project focuses on a **Triple-Lock Safety System** that integrates genetic engineering (Software) with biochemical modifications (Hardware) to maximize tumor-specific lysis while ensuring rapid clearance in healthy tissue.

## The Problem: Off-Target Toxicity & Immune Clearance
Current oncolytic therapies face two primary hurdles:
1. **Systemic Neutralization:** The immune system often clears the virus before it reaches the tumor.
2. **Leaky Expression:** "Off-target" replication in healthy cells can lead to adverse side effects.

## The 3-Lock Architecture (Patent Pending)
This project simulates a modular safety system to solve these challenges:

### 1. The Hardware Lock: Shielding & Environment-Specific Activation
* **Mechanism:** Cleavable PEGylation.
* **Function:** The virus is coated in Polyethylene Glycol (PEG) to evade immune detection. A tumor-specific protease linker ensures the shield is "dropped" only within the acidic, enzyme-rich tumor microenvironment.

### 2. The Software Lock: Genetic Riboswitch Control
* **Mechanism:** Transcriptional On/Off Switch.
* **Function:** Replication is governed by a synthetic riboswitch that responds exclusively to intracellular markers found in KRAS-mutant cells.

### 3. The Safeguard Lock: Post-Transcriptional Sequestration
* **Mechanism:** RNA "Tangling" & Foreign Fragment Integration.
* **Function:** A proprietary RNA tail modification ensures that any viral genome entering a healthy cell is immediately sequestered (tangled) and targeted for rapid enzymatic destruction. In tumor cells, this fragment acts as an adjuvant, converting "cold" tumors into "hot" immunogenic environments.

## Computational Simulation (Python/Dry Lab)
The simulation scripts included here model the following:
- **Viral Kinetics:** Differential equations modeling burst size and infection rates in heterogeneous cell populations.
- **Safety Thresholds:** Comparative analysis between standard OV constructs and the 3-Lock Architecture.
- **Microenvironment Logic:** Modeling protease-cleavage efficiency and riboswitch response times.

## Tech Stack
- **Language:** Python 3.x
- **Environment:** Miniconda / Jupyter
- **Libraries:** - `NumPy` & `SciPy` (Mathematical Modeling)
  - `Matplotlib` (Data Visualization)
  - `Biopython` (Sequence analysis placeholders)

## Current Status
 * [x] Conceptual Design & Logic Flow
 * [x] Mathematical Modeling of 3-Lock Logic
 * [x] Refinement of Stochastic Simulation Parameters
 * [ ] Provisional Patent Filing (In Progress)

Phase 3: Robustness & Sensitivity Testing
To ensure the 3-Lock Architecture remains effective across diverse patient populations, I conducted a Stochastic Sensitivity Analysis. This phase models the "real-world" performance of the virus by varying critical biological parameters—such as protease concentration and RNA decay rates—to simulate physiological noise and patient-specific variability.
Key Outcomes:
 * Safety Integrity: Validated that Lock 2 (RNA Sequestration) remains effective even in "low-defense" healthy cell environments.
 * Trigger Precision: Confirmed the riboswitch (Lock 1) maintains a high signal-to-noise ratio across a range of KRAS-mutant marker concentrations.
[Detailed Technical Data & Visualizations available in the /results folder]
## Usage
*Note: Due to pending intellectual property filings, the exact genetic sequences and core logic scripts are currently restricted. A "Lite" version of the simulation logic is provided in the `/simulations` folder for demonstration purposes.*

## Research & Development
This project is being developed as part of a transition toward high-level R&D in synthetic biology and oncology. 

**Contact:** [Suraj Suresh Jadhav]
