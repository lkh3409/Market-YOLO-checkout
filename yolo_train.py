from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(data='./item.yaml',epochs=150,batch=32,imgsz=640,patience=10)




