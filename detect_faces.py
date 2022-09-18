import cv2

########### detect from image ############
##########################################
##########################################
# # load image file & frontal face cascade
# image = cv2.imread('images/faces.jpg', 1)
# face_cascade = cv2.CascadeClassifier('cascades/adaboost_frontal_face_detector.xml')

# # use cascade to detect frontal faces
# faces = face_cascade.detectMultiScale(image, 1.4, 4)
# # print(faces)

# # use returned coordinates to draw a frame
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (30,211,198), 3)

# # save edited image to file
# cv2.imwrite('images/faces_detected.jpg', image)



########### detect from video ############
####### and draw boxes in video ##########
##########################################
# # load video file & frontal face cascade
# video = cv2.VideoCapture('videos/faces_01.mp4')
# face_cascade = cv2.CascadeClassifier('cascades/adaboost_frontal_face_detector.xml')

# # read first frame of the video
# success, frame = video.read()

# # get frame dimensions and fps of input video
# height = frame.shape[0]
# width = frame.shape[1]
# fps = int(video.get(cv2.CAP_PROP_FPS))

# # prepare empty video file
# # output = cv2.VideoWriter('videos/output.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
# # input file was too large - i will resize it to 720p (see below)
# output = cv2.VideoWriter('videos/output.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (1280, 720))

# while success:
#     resize = cv2.resize(frame, (1280, 720))
#     # use cascade to detect frontal faces
#     faces = face_cascade.detectMultiScale(resize, 1.4, 4)

#     # use returned coordinates to draw a frame
#     for (x, y, w, h) in faces:
#         cv2.rectangle(resize, (x, y), (x+w, y+h), (198,211,30), 3)

#     # write frame to empty output
#     output.write(resize)

#     # read next frame to start the loop
#     success, frame = video.read()

# # generate video when you reached end of file
# output.release()



########### detect from video ############
########### and grab snapshots ###########
##########################################
# load video file & frontal face cascade
video = cv2.VideoCapture('videos/faces_01.mp4')
face_cascade = cv2.CascadeClassifier('cascades/adaboost_frontal_face_detector.xml')

# read first frame of the video
success, frame = video.read()
count = 1

while success:
    # convert image to grayscale and resize
    resize = cv2.resize(frame, (1280, 720))
    gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    # use cascade to detect frontal faces on grayscale frame
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.4, minNeighbors=4)

    # use returned coordinates to draw bounding box on colour frame
    for (x, y, w, h) in faces:
        cv2.rectangle(resize, (x, y), (x+w, y+h), (198,211,30), thickness=3)
        cv2.imwrite(f'images/face_detection_{count}.jpg', resize)
        count += 1

    # read next frame to start the loop
    success, frame = video.read()