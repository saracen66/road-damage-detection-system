def calculate_severity(detection):

    damage_type = detection["class"]
    area = detection["bbox_area"]
    confidence = detection["confidence"]

    damage_weights = {
        "pothole": 1.5,
        "alligator_crack": 1.3,
        "transverse_crack": 1.1,
        "longitudinal_crack": 1.0,
        "patching": 0.8
    }

    weight = damage_weights.get(damage_type, 1.0)

    severity_score = (
        (area / 10000)
        * weight
        * confidence
    )

    if severity_score < 2:
        return "Low"

    elif severity_score < 5:
        return "Medium"

    else:
        return "High"