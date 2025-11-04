
"""
Particle in a 1D Box - Separate Graphs
Author: Md. Mahiuddin Zilani
"""

import numpy as np
import matplotlib.pyplot as plt

L = float(input("Enter box length L: "))
n_max = int(input("Enter highest quantum number to plot: "))
points = 1000

x = np.linspace(0, L, points)


def wavefunction(n, x, L):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def probability_density(psi):
    return psi**2


fig, axs = plt.subplots(2, 1, figsize=(10, 10))


for n in range(1, n_max + 1):
    psi = wavefunction(n, x, L)
    axs[0].plot(x, psi, label=f'ψ{n}(x)')
axs[0].set_title("Wavefunctions ψₙ(x)")
axs[0].set_xlabel("Position x")
axs[0].set_ylabel("ψₙ(x)")
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.5)


for n in range(1, n_max + 1):
    psi = wavefunction(n, x, L)
    prob = probability_density(psi)
    axs[1].plot(x, prob, label=f'|ψ{n}(x)|²')
axs[1].set_title("Probability Densities |ψₙ(x)|²")
axs[1].set_xlabel("Position x")
axs[1].set_ylabel("Probability Density")
axs[1].legend()
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
