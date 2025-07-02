from typing import List
from components import component
from ultralytics import YOLO
import cv2
from box import box
import time
import os
from machine import machine


def is_significantly_different(set_a, set_b, tolerance):
    return len(set_a.symmetric_difference(set_b)) >= tolerance


base_path = os.path.dirname(__file__)
weights_path = os.path.join(base_path, "weights.pt")
model = YOLO(weights_path)
cap = cv2.VideoCapture(1)
rdy_new = True

if not cap.isOpened():
    print("Cannot open camera")
    exit()

boxes = [box([component(0, "Anker Typ 7"), component(1, "Buerstenhalter"), component(2, "Getriebedeckel Typ 6"),
              component(3, "Getriebehause typ 10"), component(4, "Getriebehause typ 6"),
              component(5, "Getriebehause typ 9"), component(6, "Magnet Lang"), component(7, "Poltopf-Lang"),
              component(8, "spange")]),
         box([component(6, "Magnet Lang"), component(7, "Poltopf-Lang"), component(8, "spange")])]
machines = [machine(0, "Spritzguss Maschine", "Herstellung der Gehäuse für das Motorgetriebe", "offline"),
            machine(1, "Kupferwickelmaschine", "Wicklung der Kupferdrähte für den Rotor", "offline", )]


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

    if is_significantly_different(current_classes, seen_classes, tolerance=1) & rdy_new:
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
            rdy_new = False
        else:
            rdy_new = True

    seen_classes = current_classes

    cv2.imshow("YOLOv8 Live", annotated_frame)

    if key == ord('q'):
        break

for box in boxes:
    print(box)


cap.release()
cv2.destroyAllWindows()
