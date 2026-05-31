import numpy as np

def conversion(k, t):
    """
    First-order carbonation conversion model

    Parameters
    ----------
    k : rate constant
    t : residence time

    Returns
    -------
    X : conversion
    """
    return 1 - np.exp(-k * t)


def co2_captured(flow_rate, X):
    """
    Calculate captured CO₂

    Parameters
    ----------
    flow_rate : CO₂ flow rate
    X : conversion

    Returns
    -------
    Captured CO₂
    """
    return flow_rate * X