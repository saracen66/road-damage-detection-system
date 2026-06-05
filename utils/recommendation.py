def get_recommendation(report):
    if report["total_detections"] == 0:
        return "No road damage detected. The road segment appears to be in good condition."

    damage = report["highest_priority_damage"]

    priority = report["highest_priority"]

    if damage == "pothole":

        if priority == 1:
            return "Immediate pothole repair recommended."

        elif priority == 2:
            return "Schedule pothole maintenance."

        return "Monitor pothole growth during routine inspections."

    elif damage == "alligator_crack":

        if priority == 1:
            return "Full pavement rehabilitation is recommended."

        elif priority == 2:
            return "Perform crack sealing and patching."

        return "Monitor crack progression."

    elif damage == "longitudinal_crack":

        if priority == 1:
            return "Seal crack immediately to prevent water intrusion."

        elif priority == 2:
            return "Schedule crack sealing maintenance."

        return "Periodic monitoring recommended."

    elif damage == "patching":

        if priority == 1:
            return "Reconstruct failed patch area."

        elif priority == 2:
            return "Repair damaged patch section."

        return "Monitor patch performance."

    return "Routine inspection recommended."