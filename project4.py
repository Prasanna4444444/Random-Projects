import cv2
import numpy as np

# Model paths
face_proto = "models/deploy.prototxt"
face_model = "models/res10_300x300_ssd_iter_140000.caffemodel"

gender_proto = "models/gender_deploy.prototxt"
gender_model = "models/gender_net.caffemodel"

# Load models
face_net = cv2.dnn.readNet(face_model, face_proto)
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

# Gender labels
GENDER_LIST = ['Male', 'Female']

# Mean values for gender model
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Face detection
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
                                 (104, 117, 123), swapRB=False)

    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.7:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype(int)

            face = frame[y1:y2, x1:x2]

            if face.size == 0:
                continue

            # Gender prediction
            face_blob = cv2.dnn.blobFromImage(
                face, 1.0, (227, 227),
                MODEL_MEAN_VALUES, swapRB=False
            )

            gender_net.setInput(face_blob)
            gender_preds = gender_net.forward()
            gender = GENDER_LIST[gender_preds[0].argmax()]

            # Draw results
            label = f"{gender}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Gender Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
