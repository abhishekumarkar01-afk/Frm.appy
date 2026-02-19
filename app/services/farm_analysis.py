def analyze_farm(data: dict):
    area = data.get("area_acres")
    irrigation = data.get("irrigation")

    productivity_score = 0

    if irrigation:
        productivity_score += 50
    if area > 5:
        productivity_score += 50

    return {
        "farm_score": productivity_score,
        "recommendation": "Improve irrigation efficiency"
    }
