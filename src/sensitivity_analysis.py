import numpy as np

def sensitivity(base_value, new_value):
    """
    Percentage sensitivity
    """

    return ((new_value - base_value) / base_value) * 100
import numpy as np
import matplotlib.pyplot as plt

cao = np.linspace(0.05,0.30,100)

capture_capacity = cao * 1000 * 44 / 56

plt.figure(figsize=(8,5))

plt.plot(cao*100,capture_capacity)

plt.xlabel("CaO Content (%)")
plt.ylabel("Theoretical CO₂ Capacity (kg)")

plt.title("Effect of Fly Ash Composition")

plt.grid(True)

plt.tight_layout()

plt.savefig("plots/cao_sensitivity.png",dpi=300)

plt.show()