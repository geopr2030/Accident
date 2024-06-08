from detect import AccidentDetection
import cv2
import numpy as np

model = AccidentDetection()
font = cv2.FONT_HERSHEY_COMPLEX


def capture():
    video = cv2.VideoCapture('car2.mp4')
    while True:
        ret, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (256, 256))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if pred == "Accident" and prob[0][0] >= 0.97:
            prob = round(prob[0][0] * 100, 2)
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred + " = " + str(prob),
                        (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            return
        cv2.imshow('Video', frame)


if __name__ == "__main__":
    capture()
