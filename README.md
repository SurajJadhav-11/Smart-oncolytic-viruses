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

###The Environmental Lock (Hardware-Level Activation)
   * Mechanism: Protease-responsive surface modification.
   * Function: Utilizes a tumor-specific linker that ensures viral activation is restricted to the acidic, enzyme-rich tumor microenvironment, protecting the payload during systemic circulation.
 * The Transcriptional Lock (Software-Level Control)
   * Mechanism: Synthetic Riboswitch Logic.
   * Function: Viral replication is governed by a high-precision genetic switch that triggers exclusively in the presence of intracellular markers specific to KRAS-mutant profiles.
 * The Biocontainment Lock (Post-Transcriptional Safeguard)
   * Mechanism: Proprietary Intracellular Sequestration Logic.
   * Function: A novel safeguard designed to neutralize viral genetic material within non-target cells. In healthy tissue, this mechanism facilitates rapid enzymatic clearance; within the tumor environment, it is engineered to enhance the local immunogenic response, effectively "turning the tumor hot.

## Computational Simulation (Python/Dry Lab)
The simulation scripts included here model the following:
- **Viral Kinetics:** Differential equations modeling burst size and infection rates in heterogeneous cell populations.
- **Safety Thresholds:** Comparative analysis between standard OV constructs and the 3-Lock Architecture.
- **Microenvironment Logic:** Modeling protease-cleavage efficiency and riboswitch response times.

## Tech Stack & Environment
* **Language:** Python 3.10+
* **Libraries:**
    * **NumPy (v1.24+):** For high-performance array manipulation and kinetics modeling.
    * **Matplotlib (v3.7+):** For generating publication-quality simulation visualizations.
    * **SciPy (v1.10+):** For solving the differential equations governing viral decay.


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
