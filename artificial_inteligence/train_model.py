from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
model.train(data='C:/Users/rafae/OneDrive/Área de Trabalho/patromonial-system/data.yaml', epochs=100)
model.val()  # It'll automatically evaluate the data you trained.