import cv2
import os

face_cascade = cv2.CascadeClassifier('cascades/adaboost_frontal_face_detector.xml')
RTSP_URL = 'rtsp://admin:instar@192.168.2.120/livestream/12'

# use tcp instead of udp if stream is unstable
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
# start the stream and verify
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("ERROR :: Cannot open RTSP stream")
    exit(-1)



####### detect from videostream ##########
########### and grab snapshots ###########
##########################################

# # start reading frames
# success, frame = cap.read()
# count = 0

# while success:
#     # resize frame and convert to grayscale
#     resize = cv2.resize(frame, (1280, 720))
#     gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

#     # use cascade to detect frontal faces on grayscale frame
#     faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.4, minNeighbors=4)

#     # use returned coordinates to draw bounding box on colour frame
#     for (x, y, w, h) in faces:
#         cv2.rectangle(resize, (x, y), (x+w, y+h), (198,211,30), thickness=3)
#         cv2.imwrite(f'images/face_detection_{count}.jpg', resize)
    
#     # output.write(resize)
#     count += 1
#     success, frame = cap.read()



####### detect from videostream ##########
############ and record video ############
##########################################


# prepare empty video file
output = cv2.VideoWriter('videos/face_detection.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, (1280, 720))


# start reading frames
success, frame = cap.read()
count = 0

while success:
    # resize frame and convert to grayscale
    resize = cv2.resize(frame, (1280, 720))
    gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    # use cascade to detect frontal faces on grayscale frame
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.4, minNeighbors=4)

    # use returned coordinates to draw bounding box on colour frame
    for (x, y, w, h) in faces:
        cv2.rectangle(resize, (x, y), (x+w, y+h), (198,211,30), thickness=3)
        output.write(resize)
    
    count += 1
    success, frame = cap.read()

output.release()