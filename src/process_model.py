def co2_captured(flow_rate, conversion):
    """
    CO₂ captured (kg/hr)
    """
    return flow_rate * conversion


def carbonate_production(co2_captured):
    """
    Estimate CaCO3 production

    Molecular weight ratio:
    CaCO3 / CO2 = 100 / 44
    """

    return co2_captured * (100 / 44)


def capture_efficiency(conversion):
    """
    Capture efficiency (%)
    """

    return conversion * 100