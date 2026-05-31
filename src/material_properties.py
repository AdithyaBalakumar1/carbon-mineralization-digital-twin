MATERIALS = {
    "Fly Ash": {
        "CaO": 0.15
    },

    "Steel Slag": {
        "CaO": 0.40
    },

    "Red Mud": {
        "CaO": 0.08
    }
}


def max_co2_capacity(material_name, mass_kg):

    cao_fraction = MATERIALS[material_name]["CaO"]

    cao_mass = mass_kg * cao_fraction

    MW_CaO = 56
    MW_CO2 = 44

    return cao_mass * MW_CO2 / MW_CaO