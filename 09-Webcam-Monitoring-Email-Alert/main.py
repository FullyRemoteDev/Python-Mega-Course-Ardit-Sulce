import cv2
import time

pc_cam_port = 0
pc_cam = cv2.VideoCapture(pc_cam_port, cv2.CAP_DSHOW)
time.sleep(1)

first_frame = None

while True:
    check, frame = pc_cam.read()

    # Convert Frame to Grayscale - to reduce data size
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur - to further reduce data size
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # For first comparison assign processed frame as first frame
    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    # Compare first frame with current processed frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # Set threshold levels for detection of new object from environment
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    # Using dilate to remove noise
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Show the processed video feed
    cv2.imshow('My Video', dil_frame)

    # Detect the contours around the white areas - new object(s) in the scene
    contours, check2 = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Iterate over contours of all the objects in the scene
    for contour in contours:
        if cv2.contourArea(contour) < 10_000:
            continue
        # Extracting the coordinates and sizes of the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Draw a bounding box around the contour - including colour and width
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

pc_cam.release()
