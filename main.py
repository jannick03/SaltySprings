from ultralytics import YOLO
import cv2

//model = YOLO("C:\\Users\\andre\\PycharmProjects\\SaltySprings\\weights.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read camera")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    if cv2.waitKey(1) & 0xFF == ord('p'):
        # Get class indices from results
        class_ids = results[0].boxes.cls.cpu().numpy().astype(int)

        # Get class names from model
        class_names = [model.names[c] for c in class_ids]

        # Save class names to a text file (overwrites each frame)
        with open("predicted_classes.txt", "w") as f:
            for name in class_names:
                f.write(f"{name}\n")
        break

    cv2.imshow("YOLOv8 Live", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
