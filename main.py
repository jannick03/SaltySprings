from ultralytics import YOLO
import cv2
from steckbrief import steckbrief

model = YOLO("C:\\Users\\andre\\PycharmProjects\\SaltySprings\\weights.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

steckbriefe = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read camera")
        break

    results = model(frame)
    annotated_frame = results[0].plot()
    key = cv2.waitKey(1) & 0xFF

    if key == ord('p'):
        # Get class indices from results
        class_ids = results[0].boxes.cls.cpu().numpy().astype(int)

        # Get class names from model
        class_names = [model.names[c] for c in class_ids]

        detected_items = []
        with open("predicted_classes.txt", "w") as f:
            for class_id in class_ids:
                name = model.names[class_id]
                f.write(f"{class_id} : {model.names[class_id]}\n")
                detected_items.append((class_id, name))  # Save for the class

        steckbriefe.append(steckbrief(detected_items))

    cv2.imshow("YOLOv8 Live", annotated_frame)

    if key == ord('q'):
        break



for sb in steckbriefe:
    print(sb)

cap.release()
cv2.destroyAllWindows()
