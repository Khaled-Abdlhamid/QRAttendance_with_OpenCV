import numpy as np
import cv2
from pyzbar.pyzbar import decode
from util import get_id

id_list = get_id()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    qr_info = decode(frame)

    for i in qr_info:
        left = i.rect.left
        top = i.rect.top
        width = i.rect.width
        height = i.rect.height
        polygon = i.polygon
        data = i.data

        frame = cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 255, 0), 5)
        frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)
        if int(data.decode()) in id_list:
            frame = cv2.putText(frame, 'Access Granted', (left, top - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        else:
            frame = cv2.putText(frame, 'Access Denied', (left, top - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)


    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()