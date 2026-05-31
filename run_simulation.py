import numpy as np
import matplotlib.pyplot as plt

from src.carbonation_model import conversion

from src.process_model import (
    co2_captured,
    carbonate_production,
    capture_efficiency
)

from src.material_properties import max_co2_capacity

from src.sustainability_metrics import (
    carbon_negativity_index,
    carbon_negativity_score
)

# ==========================================
# INPUT PARAMETERS
# ==========================================

co2_feed = 1000          # kg/hr
fly_ash_mass = 1000      # kg
process_emissions = 100  # kg CO2/hr

k = 0.05                # reaction rate constant

# ==========================================
# SIMULATION DOMAIN
# ==========================================

t = np.linspace(0, 100, 200)

# ==========================================
# REACTION MODEL
# ==========================================

X = conversion(k, t)

# ==========================================
# MATERIAL CONSTRAINT
# ==========================================

capacity = max_co2_capacity(fly_ash_mass)

# ==========================================
# CO2 CAPTURE
# ==========================================

captured_raw = co2_captured(co2_feed, X)

captured = np.minimum(captured_raw, capacity)

# ==========================================
# PERFORMANCE METRICS
# ==========================================

carbonate = carbonate_production(captured)

efficiency = capture_efficiency(X)

cni = carbon_negativity_index(
    captured,
    process_emissions
)

score = carbon_negativity_score(
    captured[-1],
    process_emissions
)

# ==========================================
# PLOT 1
# Conversion vs Time
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(t, X, linewidth=2)

plt.xlabel("Residence Time (min)")
plt.ylabel("Conversion")

plt.title("Carbonation Conversion vs Residence Time")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "plots/conversion_vs_time.png",
    dpi=300
)

# ==========================================
# PLOT 2
# CO2 Capture
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    t,
    captured,
    linewidth=2
)

plt.xlabel("Residence Time (min)")
plt.ylabel("CO₂ Captured (kg/hr)")

plt.title("CO₂ Capture Performance")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "plots/co2_capture.png",
    dpi=300
)

# ==========================================
# PLOT 3
# Carbon Negativity
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    t,
    cni,
    linewidth=2
)

plt.xlabel("Residence Time (min)")
plt.ylabel("Carbon Negativity Index (kg CO₂/hr)")

plt.title("Carbon Negativity Performance")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "plots/carbon_negativity.png",
    dpi=300
)

plt.show()

# ==========================================
# OUTPUT
# ==========================================

print("\n===== DIGITAL TWIN OUTPUT =====")

print(f"Final Conversion: {X[-1]:.3f}")

print(f"Capture Efficiency: {efficiency[-1]:.1f}%")

print(f"Fly Ash Capacity: {capacity:.1f} kg CO₂")

print(f"CO₂ Captured: {captured[-1]:.1f} kg/hr")

print(f"CaCO₃ Produced: {carbonate[-1]:.1f} kg/hr")

print(
    f"Carbon Negativity Index: "
    f"{cni[-1]:.1f} kg CO₂/hr"
)

print(
    f"Carbon Negativity Score: "
    f"{score:.2f}"
)