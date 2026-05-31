import numpy as np

def conversion(k, t):
    return 1 - np.exp(-k * t)


def optimize_residence_time(
    k,
    co2_feed,
    capacity,
    emissions
):

    times = np.linspace(1, 200, 500)

    best_score = -1
    best_time = None

    for t in times:

        X = conversion(k, t)

        captured = min(
            co2_feed * X,
            capacity
        )

        score = captured / emissions

        if score > best_score:

            best_score = score
            best_time = t

    return best_time, best_score