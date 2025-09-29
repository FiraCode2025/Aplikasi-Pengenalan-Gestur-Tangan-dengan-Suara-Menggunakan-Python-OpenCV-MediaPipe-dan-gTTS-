import cv2
import mediapipe as mp
from gtts import gTTS
from playsound import playsound
import os

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

gesture_messages = {
    "ONE": "Halo!",
    "TWO": "Perkenalkan, saya Fira",
    "FIVE": "Terimakasih",
    "FIST": "Salam kenal"
}

last_gesture = None
TEMP_FILE = "output.mp3"   # simpan suara sementara

def detect_gesture(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    landmarks = hand_landmarks.landmark

    fingers = []
    for tip in finger_tips:
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y)

    thumb = landmarks[thumb_tip].x < landmarks[thumb_tip - 2].x

    if fingers == [True, False, False, False]:
        return "ONE"
    elif fingers == [True, True, False, False]:
        return "TWO"
    elif all(fingers) and thumb:
        return "FIVE"
    elif not any(fingers) and not thumb:
        return "FIST"
    else:
        return None

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture = None
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks)

    if gesture and gesture in gesture_messages:
        text = gesture_messages[gesture]

        cv2.putText(frame, text, (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3, cv2.LINE_AA)

        if gesture != last_gesture:
            # Simpan ke file mp3 lalu putar
            tts = gTTS(text=text, lang="id")
            tts.save(TEMP_FILE)
            playsound(TEMP_FILE)
            os.remove(TEMP_FILE)  # hapus setelah diputar

            last_gesture = gesture

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC untuk keluar
        break

cap.release()
cv2.destroyAllWindows()
