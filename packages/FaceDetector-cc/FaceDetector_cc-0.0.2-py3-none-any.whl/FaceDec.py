"""
Project : Mediapipe Face Detection
Developer : Chanchal Roy
Date : 11th Dec, 2022
GitHub : https://github.com/Chexa12cc/FaceDetector-cc
"""
import cv2 as c
import time
import mediapipe as mp
import numpy as np


class FaceDetector:
    def __init__(
            self,
            cam_index: int = 0,
            cam_width: int = 640,
            cam_height: int = 360,
            min_detection_confidence=0.5,
            model_selection=0):
        """Face Detection"""
        self.cid = cam_index
        self.cw = cam_width
        self.ch =cam_height
        self.det_conf = min_detection_confidence
        self.mod_sel = model_selection
        self.mp_face = mp.solutions.face_detection
        self.RED = (0, 0, 255)
        self.YELLOW = (0, 255, 255)

    def init_cam(self) -> np.ndarray:
        """Initiate camera"""
        self.cam = c.VideoCapture(self.cid, 700)
        self.cam.set(3, self.cw)
        self.cam.set(4, self.ch)
        self.cam.set(5, 30)
        self.cam.set(6, c.VideoWriter_fourcc(*'MJPG'))
        return self.cam

    def detect_face(
            self,
            image: np.ndarray,
            draw_detection: bool = True,
            draw_key: bool = True,
            draw_bbox: bool = True) -> tuple:
        """Detect Face points"""
        self.face = self.mp_face.FaceDetection(
            min_detection_confidence=self.det_conf,
            model_selection=self.mod_sel)

        self.image_rgb = c.cvtColor(image, c.COLOR_BGR2RGB)
        self.result = self.face.process(image=self.image_rgb)

        if self.result.detections:
            for id1, fd in enumerate(self.result.detections):
                self.kp_data = fd.location_data.relative_keypoints
                self.bbox_data = fd.location_data.relative_bounding_box

                if draw_detection:
                    h, w, _ = image.shape
                    if draw_key:
                        x1, y1 = int(self.bbox_data.xmin * w), int(self.bbox_data.ymin * h)
                        x2, y2 = int((self.bbox_data.xmin + self.bbox_data.width) * w), int((self.bbox_data.ymin + self.bbox_data.height) * h)
                        c.rectangle(image, (x1, y1), (x2, y2), self.YELLOW, 2)

                    if draw_bbox:
                        for key in self.kp_data:
                            cx, cy = int(key.x * w), int(key.y * h)
                            c.circle(image, (cx, cy), 3, self.RED, -1)
        return self.kp_data, self.bbox_data


def main():
    RED = (0, 0, 255)
    YELLOW = (0, 255, 255)
    timeS, timeE = 0, 0

    obj = FaceDetector()
    cam = obj.init_cam()

    while cam.isOpened():
        success, frame = cam.read()

        if not success: continue

        face_lm, face_bbox = obj.detect_face(frame)
        print(face_lm, face_bbox, sep='\n', end='\n\n')

        timeE: float = time.time()
        fps = int(1 / (timeE - timeS))
        timeS = timeE
        c.putText(frame, str(f'FPS : {fps}'), (10, 30), 0, 1, YELLOW, 2)

        c.imshow('Face Detection : Chanchal Roy', frame)

        if c.waitKey(1) & 0xff == ord('q'): break

    cam.release()
    c.destroyAllWindows()


if __name__ == '__main__':
    main()
