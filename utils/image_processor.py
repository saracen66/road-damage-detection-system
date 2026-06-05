from utils.detector import detect_image
from utils.severity import calculate_severity
from utils.priority import calculate_priority
from utils.report import generate_report


def process_image(image_path, output_path):

    detections = detect_image(
        image_path,
        output_path
    )

    for detection in detections:

        detection["severity"] = calculate_severity(
            detection
        )

        detection["priority"] = calculate_priority(
            detection,
            detection["severity"]
        )

    report = generate_report(
        detections
    )

    return {
        "image_path": output_path,
        "detections": detections,
        "report": report
    }