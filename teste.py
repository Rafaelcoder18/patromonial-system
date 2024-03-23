from ultralytics import YOLO

model = YOLO("runs/detect/train17/weights/best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
results = model.predict(source="https://www.youtube.com/watch?v=BtMmymOxdjc", show=True) # Display preds. Accepts all YOLO predict arguments

