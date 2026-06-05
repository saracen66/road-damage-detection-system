from flask import Flask, render_template, request
from utils.image_processor import process_image
from utils.video_processor import process_video
from utils.recommendation import get_recommendation
import os
import time

app = Flask(__name__)

IMAGE_UPLOAD_FOLDER = "uploads/images"
VIDEO_UPLOAD_FOLDER = "uploads/videos"

IMAGE_OUTPUT_FOLDER = "static/results"
VIDEO_OUTPUT_FOLDER = "static/videos"

os.makedirs(IMAGE_UPLOAD_FOLDER, exist_ok=True)
os.makedirs(VIDEO_UPLOAD_FOLDER, exist_ok=True)

os.makedirs(IMAGE_OUTPUT_FOLDER, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_FOLDER, exist_ok=True)

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
}


@app.route("/", methods=["GET", "POST"])
def home():

    result_image = None
    result_video = None

    detections = None
    report = None
    recommendation = None

    if request.method == "POST":

        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            return render_template("index.html")

        extension = os.path.splitext(
            uploaded_file.filename
        )[1].lower()

        # IMAGE PIPELINE
        if extension in IMAGE_EXTENSIONS:

            image_path = os.path.join(
                IMAGE_UPLOAD_FOLDER,
                uploaded_file.filename
            )

            uploaded_file.save(image_path)

            output_filename = f"result_{int(time.time())}.jpg"

            output_path = os.path.join(
                IMAGE_OUTPUT_FOLDER,
                output_filename
            )

            result = process_image(
                image_path,
                output_path
            )

            result_image = result["image_path"]
            detections = result["detections"]
            report = result["report"]

        # VIDEO PIPELINE
        elif extension in VIDEO_EXTENSIONS:

            video_path = os.path.join(
                VIDEO_UPLOAD_FOLDER,
                uploaded_file.filename
            )

            uploaded_file.save(video_path)

            output_filename = f"result_{int(time.time())}.mp4"

            output_video = os.path.join(
                VIDEO_OUTPUT_FOLDER,
                output_filename
            )

            result = process_video(
                video_path,
                output_video
            )

            result_video = result["video_path"]
            report = result["report"]

        if report:
            recommendation = get_recommendation(report)

    return render_template(
        "index.html",
        result_image=result_image,
        result_video=result_video,
        detections=detections,
        report=report,
        recommendation=recommendation,
        damage_counts=report.get("damage_counts", {}) if report else {},
        severity_counts=report.get("severity_counts", {}) if report else {}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)