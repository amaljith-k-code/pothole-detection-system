\# 🚗 Pothole Detection and Road Monitoring System



A computer vision application for detecting and tracking potholes in road images and videos using a trained YOLO model.



The application provides a Streamlit dashboard where users can upload road images or videos, configure the detection confidence threshold, visualize pothole detections, and export detection telemetry as a CSV file.



\## Features



\* 🖼️ Pothole detection from road images

\* 🎥 Pothole detection and tracking in videos

\* 🎯 Configurable confidence threshold

\* 📦 Bounding-box visualization

\* 🆔 Tracking IDs for detected potholes

\* 📊 Detection telemetry using Pandas

\* 📥 CSV export of detection results

\* 🌐 Streamlit-based web interface



\## Technologies Used



\* Python

\* YOLO — Ultralytics

\* Streamlit

\* Pandas

\* Pillow

\* PyTorch

\* OpenCV / video processing through Ultralytics



\## How It Works



\### Image Mode



1\. The user uploads a road image.

2\. The trained YOLO model processes the image.

3\. Potholes are detected based on the selected confidence threshold.

4\. Bounding boxes are drawn around detected potholes.

5\. The application displays the detection results and pothole count.



\### Video Mode



1\. The user uploads a road video.

2\. The video is temporarily stored for processing.

3\. YOLO tracking processes the video frame by frame.

4\. Detected potholes are assigned tracking IDs when available.

5\. Detection information is collected for each frame.

6\. Annotated frames are displayed in the Streamlit interface.

7\. Detection telemetry can be downloaded as a CSV file.



\## Detection Telemetry



For video detections, the application records:



\* Frame ID

\* Track ID

\* Confidence score

\* Bounding-box X1 coordinate

\* Bounding-box Y1 coordinate

\* Bounding-box X2 coordinate

\* Bounding-box Y2 coordinate



Example:



| Frame ID | Track ID | Confidence |  X1 |  Y1 |  X2 |  Y2 |

| -------- | -------- | ---------: | --: | --: | --: | --: |

| 1        | 1        |       0.87 | 120 | 200 | 310 | 350 |

| 2        | 1        |       0.84 | 125 | 202 | 315 | 352 |



\## Project Structure



```text

pothole-detection-system/

│

├── app.py

├── best.pt

├── .gitignore

├── .streamlit/

│   └── config.toml

└── README.md

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/amaljith-k-code/pothole-detection-system.git

cd pothole-detection-system

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

venv\\Scripts\\activate

```



Install the required packages:



```bash

pip install streamlit ultralytics pandas pillow

```



\## Run the Application



Start the Streamlit application:



```bash

python -m streamlit run app.py

```



The application will open in your browser.



\## Model



The application uses `best.pt`, a trained YOLO model developed for pothole detection.



The model is loaded by the application using:



```python

model = YOLO("best.pt")

```



\## 🚀 Feature Upgrades



The current version focuses on pothole detection, tracking, and telemetry. The system can be extended into a more practical road-condition monitoring platform with the following features:



\### 📍 GPS-Based Pothole Location



Integrate GPS data from a smartphone or GPS device and associate each detected pothole with its real-world coordinates.



\### 🗺️ Interactive Pothole Map



Display detected potholes on a map so road-maintenance teams can quickly identify affected road sections.



\### ⚠️ Pothole Severity Estimation



Estimate pothole severity using visual characteristics such as bounding-box size and additional image-based features.



\### 📄 Automated Road Inspection Report



Generate a report containing detected potholes, locations, timestamps, confidence scores, severity, and supporting images.



\### 📊 Road Condition Analytics



Analyze collected detection data to identify pothole frequency and problematic road sections.



\### 🎥 Evidence Clips



Automatically extract short video clips around detected potholes so maintenance teams can review the detection.



\### 📱 Mobile/GPS Integration



Use a smartphone mounted on a vehicle to capture road video and GPS data simultaneously, creating a more complete road-inspection workflow.



\## Author



\*\*Amaljith K\*\*



Computer Science Graduate | Data Science \& Machine Learning



