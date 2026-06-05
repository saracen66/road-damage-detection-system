def calculate_priority(detection, severity):

    damage_type = detection["class"]

    if damage_type == "pothole":

        if severity == "High":
            return 1

        elif severity == "Medium":
            return 2

        return 3

    elif damage_type == "alligator_crack":

        if severity == "High":
            return 1

        return 2

    elif damage_type == "transverse_crack":

        return 2

    elif damage_type == "longitudinal_crack":

        return 3

    elif damage_type == "patching":

        return 4

    return 5