import cv2
from PIL import Image

from util import get_limits

blue = [255, 0, 0]

cap = cv2.VideoCapture(0)

# Set the desired FPS (e.g., 1000)
desired_fps = 500
frame_delay = int(1000 / desired_fps)  # Calculate frame delay in milliseconds

while True:
    ret, frame = cap.read()

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color = blue)

    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0 ,255), 5)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()