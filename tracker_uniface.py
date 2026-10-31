from uniface import RetinaFace
import cv2
import eyes
from utils import num_to_range

eye_window = eyes.eyeWindow()
eye_window.__init__()

cap = cv2.VideoCapture(0)

center_to_nose_offset = -50

detector = RetinaFace()

if not cap.isOpened():
    print("Error establishing connection")

eye_pos = [0, 0]
while cap.isOpened():
    ret, frame = cap.read()
    frame_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    if not (type(frame) == list or type(frame) == tuple) and frame.any():
        face_locations = detector.detect(frame)
        if len(face_locations) != 0:
            # print(face_locations[0].bbox[0])
            top_left_bb_point = (int(face_locations[0].bbox[0]), int(face_locations[0].bbox[1]))
            bottom_right_bb_point =  (int(face_locations[0].bbox[2]), int(face_locations[0].bbox[3]))
            eyes_center = (int((top_left_bb_point[0] + bottom_right_bb_point[0])/2), int((top_left_bb_point[1] + bottom_right_bb_point[1])/2 + center_to_nose_offset))

            eye_pos[0] = num_to_range(eyes_center[0], 0, frame_w, 30, -30) # type: ignore
            # print(num_to_range(eyes_center[0], 0, frame_w, 15, -15)) # type: ignore)
            eye_pos[1] = num_to_range(eyes_center[1], 0, frame_h, 13, -13) + 2 # type: ignore
            # print("(" + str(eye_pos[0]) + ", " + str(eye_pos[1]) + ")")
            eye_window.move_eyes(eye_pos)
            # Comment/uncomment the next four lines to enable/disable debug camera feed.    
            # cv2.rectangle(frame, top_left_bb_point, bottom_right_bb_point, (0, 255, 0), 8) # type: ignore
            # cv2.circle(frame, eyes_center, 10, (0, 255, 0), 5) # type: ignore
            # if ret:
            #     cv2.imshow('Displaying image frames from a webcam', frame)

        # If the Esc key is pressed, terminate the while loop
    if cv2.waitKey(25) == 27:
        break

    eye_window.update()