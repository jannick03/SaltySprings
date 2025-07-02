from typing import List
from components import component
from ultralytics import YOLO
import cv2
from box import box
import time
import os

base_path = os.path.dirname(__file__)
weights_path = os.path.join(base_path, "weights.pt")
model = YOLO(weights_path)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

boxes = []

seen_classes = set()
photo_counter = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read camera")
        break

    results = model(frame)
    annotated_frame = results[0].plot()
    key = cv2.waitKey(1) & 0xFF
    current_classes = set(results[0].boxes.cls.cpu().numpy().astype(int))
    new_classes = current_classes - seen_classes

    if new_classes:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"photo_{timestamp}_{photo_counter}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[+] Neues Objekt erkannt, Foto gespeichert als {filename}")
        photo_counter += 1

        class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
        class_names = [model.names[c] for c in class_ids]

        components: List['components'] = []
        for class_id in class_ids:
            name = model.names[class_id]
            components.append(component(class_id, name))  # Save for the class

        if len(components) != 0:
            boxes.append(box(components))

    seen_classes = current_classes

    cv2.imshow("YOLOv8 Live", annotated_frame)

    if key == ord('q'):
        break

for box in boxes:
    print(box)

cap.release()
cv2.destroyAllWindows()
