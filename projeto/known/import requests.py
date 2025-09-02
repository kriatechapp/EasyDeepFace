import cv2
import os
from deepface import DeepFace

# KNOWN_DIR = "known"
KNOWN_DIR = r"C:\Users\Renato\projeto\known"

# Carregar imagens conhecidas
known_faces = []
names = []

for file in os.listdir(KNOWN_DIR):
    if file.lower().endswith((".jpg", ".png", ".jpeg")):
        known_faces.append(os.path.join(KNOWN_DIR, file))
        names.append(os.path.splitext(file)[0])

# Abrir webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Não foi possível abrir a webcam.")

print("[INFO] Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_img = small_frame[y:y+h, x:x+w]

        nome = "Desconhecido"
        confianca = 0.0

        for i, known_path in enumerate(known_faces):
            try:
                result = DeepFace.verify(face_img, known_path, enforce_detection=False)
                if result["verified"] and result["distance"] < 0.6:
                    nome = names[i]
                    confianca = 1 - result["distance"]
                    break
            except:
                continue

        # Desenhar retângulo e nome
        cv2.rectangle(frame, (x*2, y*2), ((x+w)*2, (y+h)*2), (0,255,0), 2)
        cv2.putText(frame, f"{nome} ({confianca:.2f})", (x*2, (y+h)*2 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv2.imshow("Reconhecimento Facial", cv2.resize(frame, (frame.shape[1]*2, frame.shape[0]*2)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
