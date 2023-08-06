
# FaceDetector-cc Module

Simple python package to simply use mediapipe face detection.


## Author Details

#### Name : [Chanchal Roy](https://github.com/Chexa12cc)
#### Email : [croy7667@gmail.com](https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSKjDXfbgxPqzlHGlKdhgKgDfbxZMfwLWHzBDlSCTsRdSrZxkGcgLHSwmlbGpKmVPcLfKxWQ)


## GitHub Project Details

#### Project : [HandDetector-cc](https://github.com/Chexa12cc/FaceDetector-cc)


## Installation

Install FaceDetector-cc with pip

```bash
  pip install FaceDetector-cc
```


## Usage

```python
import FaceDec
import time

RED = (0, 0, 255)
YELLOW = (0, 255, 255)
timeS, timeE = 0, 0

obj = FaceDec.FaceDetector()
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
```