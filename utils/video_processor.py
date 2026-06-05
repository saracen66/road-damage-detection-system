import cv2
import os
import subprocess
from ultralytics import YOLO

from utils.severity import calculate_severity
from utils.priority import calculate_priority
from utils.report import generate_report

MODEL_PATH = "models/best.pt"

model = YOLO(MODEL_PATH)


def process_video(input_video, output_video):

    temp_video = output_video.replace(".mp4", "_temp.mp4")

    cap = cv2.VideoCapture(input_video)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        temp_video,
        fourcc,
        fps,
        (width, height)
    )

    all_detections = []

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model.predict(
            frame,
            conf=0.25,
            verbose=False
        )

        for box in results[0].boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            class_name = model.names[class_id]

            x1, y1, x2, y2 = box.xyxy[0]

            width_box = x2 - x1
            height_box = y2 - y1

            bbox_area = float(width_box * height_box)

            detection = {
                "class": class_name,
                "confidence": round(confidence, 3),
                "bbox_area": round(bbox_area, 2)
            }

            detection["severity"] = calculate_severity(
                detection
            )

            detection["priority"] = calculate_priority(
                detection,
                detection["severity"]
            )

            all_detections.append(
                detection
            )

        annotated_frame = results[0].plot()

        writer.write(
            annotated_frame
        )

    cap.release()
    writer.release()

    # Convert to browser-compatible H.264 MP4
    ffmpeg_command = [
        "ffmpeg",
        "-y",
        "-i",
        temp_video,
        "-vcodec",
        "libx264",
        "-acodec",
        "aac",
        output_video
    ]

    subprocess.run(
        ffmpeg_command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if os.path.exists(temp_video):
        os.remove(temp_video)

    report = generate_report(
        all_detections
    )

    return {
        "video_path": output_video,
        "report": report
    }