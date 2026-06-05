from collections import Counter


def generate_report(detections):

    damage_counter = Counter()

    severity_counter = Counter()

    highest_priority = 999

    highest_priority_damage = None

    for detection in detections:

        damage_counter[detection["class"]] += 1

        severity_counter[detection["severity"]] += 1

        if detection["priority"] < highest_priority:

            highest_priority = detection["priority"]

            highest_priority_damage = detection["class"]

    total_detections = len(detections)

    most_common_damage = None

    if damage_counter:
        most_common_damage = damage_counter.most_common(1)[0][0]

    report = {
        "total_detections": total_detections,
        "damage_counts": dict(damage_counter),
        "severity_counts": dict(severity_counter),
        "most_common_damage": most_common_damage,
        "highest_priority": highest_priority,
        "highest_priority_damage": highest_priority_damage
    }

    return report