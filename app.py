import streamlit as st
import tempfile
import pandas as pd
from PIL import Image
from ultralytics import YOLO

# Page Setup
st.set_page_config(page_title="Pothole Detection AI", page_icon="🚗", layout="wide")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.title("🚗 Automated Road Pothole Detection Dashboard")

# Sidebar Controls
st.sidebar.header("Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.25, 0.05)
option = st.sidebar.radio("Input Type", ("Image", "Video"))

# --- IMAGE MODE ---
if option == "Image":
    uploaded_file = st.file_uploader("Upload Road Image", type=["jpg", "jpeg", "png", "webp"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Detect Potholes"):
            results = model.predict(source=img, conf=conf_threshold)
            res_plotted = results[0].plot()
            pothole_count = len(results[0].boxes)
            
            st.image(res_plotted, caption="Detections", channels="BGR", use_container_width=True)
            st.success(f"Found {pothole_count} pothole(s)!")

# --- VIDEO MODE ---
elif option == "Video":
    uploaded_video = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        tfile.write(uploaded_video.read())
        
        st.video(tfile.name)
        
        if st.button("Run Video Tracking"):
            st.info("Processing video frame-by-frame in real time...")
            
            st_frame = st.empty()
            telemetry_records = []
            
            # Memory-safe generator streaming
            results_generator = model.track(
                source=tfile.name,
                conf=conf_threshold,
                stream=True,
                save=True,
                imgsz=640
            )
            
            for frame_idx, r in enumerate(results_generator):
                annotated_frame = r.plot()
                st_frame.image(annotated_frame, channels="BGR", use_container_width=True)
                
                # Simple telemetry collection
                if r.boxes is not None and len(r.boxes) > 0:
                    for box in r.boxes:
                        coords = box.xyxy[0].tolist()
                        conf = float(box.conf[0])
                        track_id = int(box.id[0]) if box.id is not None else None
                        
                        telemetry_records.append({
                            "Frame_ID": frame_idx + 1,
                            "Track_ID": track_id,
                            "Confidence": round(conf, 3),
                            "BBox_X1": int(coords[0]),
                            "BBox_Y1": int(coords[1]),
                            "BBox_X2": int(coords[2]),
                            "BBox_Y2": int(coords[3])
                        })
                        
            st.success("Video tracking completed successfully!")
            
            # Simple CSV Download
            if len(telemetry_records) > 0:
                df = pd.DataFrame(telemetry_records)
                st.subheader("Pothole Detections Log")
                st.dataframe(df, use_container_width=True)
                
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Detection Log (CSV)",
                    data=csv,
                    file_name="pothole_detections.csv",
                    mime="text/csv"
                )