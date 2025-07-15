# Multi-Fidelity Surrogate Modeling for NH₃-H₂ SI Engines (MFSM-NH₃H₂)

This repository implements multi-fidelity surrogate models for predicting spark ignition (SI) engine performance using ammonia-hydrogen blends. The surrogate models fuse heterogeneous datasets (0D/1D models + high-fidelity CFD) for real-time emulation within digital twins.

---

## 🚀 Features
- 📦 Multi-fidelity Gaussian Process (Co-Kriging) surrogate models
- 🔄 Data fusion of OpenFOAM CFD and Simulink system-level data
- 📈 Interactive dashboard for KPI visualization (Plotly/Dash)
- ⚡ Real-time Python API for surrogate predictions
- 🌱 Optimization routines (NSGA-II) for NH₃-H₂ ratio targeting minimal NOx

---

## 🛠️ Tech Stack
- **Python:** scikit-learn, GPyTorch, Emukit, pandas, numpy
- **Visualization:** Plotly, Dash
- **Optimization:** pymoo (NSGA-II)
- **CFD:** OpenFOAM
- **1D Models:** MATLAB/Simulink
- **Docker:** Containerization
- **CI/CD:** GitHub Actions

---

## 📦 Setup
```bash
git clone https://github.com/yourusername/MFSM-NH3H2.git
cd MFSM-NH3H2
conda env create -f environment.yml
conda activate mfsm
