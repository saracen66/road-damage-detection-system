# AI-Based Road Damage Detection System

An AI-powered road damage detection platform developed for the AI Competition by **Team Anvil**. The system uses a custom-trained YOLO model to detect road damages from images and videos, estimate severity, assign maintenance priority, and generate actionable maintenance recommendations.

---

## Features

- Road damage detection using YOLO
- Supports both images and videos
- Severity analysis (Low, Medium, High)
- Priority assignment (P1, P2, P3)
- AI-powered maintenance recommendations
- Interactive dashboard UI
- Damage distribution visualization
- Severity analysis charts
- Summary reporting

---

## Project Structure

```text
road-damage-detection-system/
│
├── models/
│   └── best.pt
│
├── static/
│   ├── results/
│   └── videos/
│
├── templates/
│   └── index.html
│
├── uploads/
│   ├── images/
│   └── videos/
│
├── utils/
│   ├── detector.py
│   ├── image_processor.py
│   ├── video_processor.py
│   ├── severity.py
│   ├── priority.py
│   ├── report.py
│   └── recommendation.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the project, install:

### Python

Download and install Python 3.11 or newer:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

### Git

Download and install Git:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

---

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/saracen66/road-damage-detection-system.git
```

Move into the project directory:

```bash
cd road-damage-detection-system
```

---

### Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Mac/Linux:

```bash
python3 -m venv venv
```

---

### Step 3: Activate Virtual Environment

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

```powershell
.\venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

After activation you should see:

```text
(venv)
```

at the beginning of your terminal line.

---

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This may take several minutes because PyTorch and Ultralytics are large packages.

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Using the System

### Image Detection

1. Click **Choose File**
2. Select an image
3. Click **Analyze File**
4. View:
   - Detected damages
   - Severity levels
   - Priority assignments
   - AI recommendations
   - Summary report

---

### Video Detection

1. Click **Choose File**
2. Select a video
3. Click **Analyze File**
4. Wait for processing
5. View:
   - Annotated video output
   - Damage statistics
   - Severity analysis
   - Maintenance recommendations

---

## Supported File Formats

### Images

- JPG
- JPEG
- PNG
- BMP
- WEBP

### Videos

- MP4
- AVI
- MOV
- MKV

---

## Output

### Image Analysis

The system generates:

- Processed image with bounding boxes
- Detection table
- Severity assessment
- Priority assignment
- Summary report

---

### Video Analysis

The system generates:

- Processed video with annotations
- Detection statistics
- Severity analysis
- Maintenance recommendation
- Summary report

---

## Common Issues

### Flask Not Found

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install -r requirements.txt
```

or activate the virtual environment first.

---

### Virtual Environment Not Found

Error:

```text
.\venv\Scripts\Activate.ps1 : The term is not recognized
```

Solution:

Create the virtual environment:

```bash
python -m venv venv
```

Then activate it again.

---

### Model File Missing

Error:

```text
FileNotFoundError: best.pt
```

Solution:

Ensure:

```text
models/best.pt
```

exists.

---

## Technology Stack

- Python
- Flask
- YOLO (Ultralytics)
- OpenCV
- NumPy
- Pandas
- Chart.js
- Bootstrap 5

---

## Team

**Team Anvil**

AI Competition Project

Developed for automated road damage detection, maintenance prioritization, and intelligent infrastructure monitoring.

---
