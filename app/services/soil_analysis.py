def analyze_soil(data: dict):
    ph = data.get("ph")
    nitrogen = data.get("nitrogen")

    if ph < 6:
        condition = "Acidic"
    elif ph > 7.5:
        condition = "Alkaline"
    else:
        condition = "Optimal"

    return {
        "soil_condition": condition,
        "recommendation": "Add organic compost"
    }
