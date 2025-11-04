## Particle in a 1D Box — Quantum Mechanics Simulation

# Author: Md. Mahiuddin Zilani
Topic: Quantum mechanics 

---
# Overview:
This project simulates a particle in a one-dimensional infinite potential well (particle in a box).\
It calculates wavefunctions and probability densities for different quantum numbers n. The results are plotted in two separate graphs for clear visualization.

## Features:

Interactive user input for box length L and maximum quantum number n_max\
Calculates wavefunctions using NumPy arrays\
Plots wavefunctions and probability densities in separate graphs\
Prints energy levels (dimensionless units by default)\
Can optionally calculate energies in SI units if physical constants are provided\

---
## Files:

particle_in_box.py — Main Python script\
particle_in_box.png - Created graph\

## Usage:

Save the script as particle_in_box.py\
Run the script using Python 3\
Enter the requested inputs: box length, highest quantum number, and number of spatial points\
Two graphs will appear: one for wavefunctions and one for probability densities\
Energy levels are printed in the console\

---

# Example Input:

Enter box length L: 100\
Enter highest quantum number to plot: 3\
Enter number of spatial points: 1000\
Print energies using physical constants? n\

---

# Output:

Top graph: psi_1(x), psi_2(x), psi_3(x)\
Bottom graph: |psi_1(x)|^2, |psi_2(x)|^2, |psi_3(x)|^2\
Energy levels in dimensionless units\

