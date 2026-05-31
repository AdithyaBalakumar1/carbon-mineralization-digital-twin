def carbon_negativity_index(co2_captured, process_emissions):
    """
    Carbon Negativity Index (kg CO₂/hr)
    """

    return co2_captured - process_emissions
def carbon_negativity_score(captured, emitted):

    return captured / emitted