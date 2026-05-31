import numpy as np
import matplotlib.pyplot as plt

from src.carbonation_model import conversion

# Rate constant
k = 0.05

# Residence time range
t = np.linspace(0, 100, 200)

# Conversion
X = conversion(k, t)

# Plot
plt.figure(figsize=(8,5))

plt.plot(t, X, linewidth=2)

plt.xlabel("Residence Time (min)")
plt.ylabel("Conversion")

plt.title("Carbonation Conversion vs Residence Time")

plt.grid(True)

plt.tight_layout()

plt.savefig("plots/conversion_vs_time.png", dpi=300)

plt.show()