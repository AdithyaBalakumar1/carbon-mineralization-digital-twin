from src.process_optimizer import (
    optimize_residence_time
)

from src.material_properties import (
    max_co2_capacity
)

capacity = max_co2_capacity(
    "Fly Ash",
    1000
)

best_time, best_score = (
    optimize_residence_time(
        k=0.05,
        co2_feed=1000,
        capacity=capacity,
        emissions=100
    )
)

print(
    f"Optimal Residence Time: "
    f"{best_time:.1f} min"
)

print(
    f"Best Carbon Negativity Score: "
    f"{best_score:.2f}"
)