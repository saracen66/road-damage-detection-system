from ultralytics import YOLO
import cv2

MODEL_PATH = "models/best.pt"

model = YOLO(MODEL_PATH)


def detect_image(image_path, output_path):

    results = model.predict(
        source=image_path,
        conf=0.25,
        save=False
    )

    annotated_frame = results[0].plot()

    cv2.imwrite(output_path, annotated_frame)

    detections = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        confidence = float(box.conf[0])

        class_name = model.names[class_id]

        x1, y1, x2, y2 = box.xyxy[0]

        width = x2 - x1
        height = y2 - y1

        bbox_area = float(width * height)

        detections.append({
        "class": class_name,
        "confidence": round(confidence, 3),
        "bbox_area": round(bbox_area, 2)
    })

    return detections