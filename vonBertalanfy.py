import numpy as np

# Parameters for the von Bertalanffy growth model
k = 0.1
L_infinity = 1.0
t0 = 0

# Time points (years)
years = np.arange(0, 41)

# Calculate the relative growth (L(t) / L_infinity)
relative_growth = (1 - np.exp(-k * (years - t0)))**3

# Normalize to make the sum 100%
relative_growth_normalized = relative_growth / np.sum(relative_growth) * 100

# Ensure the sum is exactly 100%
relative_growth_normalized = np.round(relative_growth_normalized, 2)

# Adjust the final value to make the sum exactly 100%
relative_growth_normalized[-1] += 100 - np.sum(relative_growth_normalized)

for item in relative_growth_normalized:
    print(item)
