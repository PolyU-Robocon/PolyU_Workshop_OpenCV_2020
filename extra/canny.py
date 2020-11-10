import numpy as np
import cv2

# https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
import imutils

cap = cv2.VideoCapture(0)

# keep looping
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

    #canny_edges = cv2.Canny(gray_blur, 10, 70)


    auto_canny = imutils.auto_canny(gray_blur)

    #ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)

    ret, mask = cv2.threshold(auto_canny, 70, 255, cv2.THRESH_BINARY_INV)

    

    # Display the resulting frame
    cv2.imshow('frame',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
