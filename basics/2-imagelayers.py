import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# keep looping
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Note OpenCV store colors in BGR format.

    frame = cv2.resize(frame, (848, 480))

    R = frame.copy()
    R[:,:,0] = 0 # Turn Blue channel to 0
    R[:,:,1] = 0 # Turn Green channel to 0
    # Now R has Red channel only

    G = frame.copy()
    G[:,:,0] = 0 # Turn Blue channel to 0
    G[:,:,2] = 0 # Turn Red channel to 0
    # Now R has Green channel only

    B = frame.copy()
    B[:,:,1] = 0 # Turn Green channel to 0
    B[:,:,2] = 0 # Turn Red channel to 0
    # Now R has Blue channel only

    # Display the resulting frame
    cv2.imshow('frame, Red Channel',R)
    cv2.imshow('frame, Green Channel',G)
    cv2.imshow('frame, Blue Channel',B)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()