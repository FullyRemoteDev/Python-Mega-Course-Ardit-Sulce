import cv2
import time
import glob
import os
from sending_email import send_email

pc_cam_port = 0
pc_cam_video = cv2.VideoCapture(pc_cam_port, cv2.CAP_DSHOW)
time.sleep(1)

first_frame = None
objects_list = []
count = 1
day_and_time = time.strftime("%A, %d %b %Y %H:%M:%S")


def clean_folder():
    images = glob.glob('images/*.png')
    for image in images:
        os.remove(image)


while True:
    object_in_view = 0
    check, frame = pc_cam_video.read()

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
    cv2.imshow("Processed Video Feed", dil_frame)

    # Detect the contours around the white areas - new object(s) in the scene
    contours, check2 = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Iterate over contours of all the objects in the scene
    for contour in contours:
        if cv2.contourArea(contour) < 5_000:
            continue
        # Extracting the coordinates and sizes of the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Draw a bounding box around the contour - including colour and width
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            # Object enters the scene (value changes from 0 to 1)
            object_in_view = 1
            cv2.imwrite(f'images/{count}.png', frame)
            count += 1
            all_images = glob.glob('images/*.png')
            index = int(len(all_images) / 2)
            object_image = all_images[index]

    # Store all the object intrusions (0 or 1) in the list
    objects_list.append(object_in_view)
    # Extract only the last two unique values
    objects_list = objects_list[-2:]

    # Check if object exits the scene (value changes from 1 to 0)
    if objects_list[0] == 1 and objects_list[1] == 0:
        send_email(object_image)
        clean_folder()

    # Add Day and Time overlay on the video feed
    cv2.putText(frame,
                day_and_time,
                (18, 36),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 191, 255),
                1,
                cv2.LINE_AA
                )
    # Show the original video feed
    cv2.imshow("Original Video Feed", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

pc_cam_video.release()
