import cv2
import os

face_cascade = cv2.CascadeClassifier('cascades/adaboost_frontal_face_detector.xml')
RTSP_URL = 'rtsp://admin:instar@192.168.2.120/livestream/12'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp' # Use tcp instead of udp if stream is unstable

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 15

video_codec = cv2.VideoWriter_fourcc(*'DIVX')
# video_output = cv2.VideoWriter('videos/captured_video.avi', video_codec, fps, (frame_width, frame_height))
video_output = cv2.VideoWriter('videos/captured_video.avi', video_codec, 15, (1280, 720))

while True:
    success, frame = cap.read()

    if success:
        # resize frame and convert to grayscale
        resize = cv2.resize(frame, (1280, 720))
        gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

        # use cascade to detect frontal faces on grayscale frame
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.4, minNeighbors=4)

        # use returned coordinates to draw bounding box on colour frame
        for (x, y, w, h) in faces:
            cv2.rectangle(resize, (x, y), (x+w, y+h), (198,211,30), thickness=3)

        cv2.imshow("Video Recording", resize)
        video_output.write(resize)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            video_output.release()
            cv2.destroyAllWindows()
            print('INFO :: Video was saved.')
            break

    else:
        cap.release()
        video_output.release()
        cv2.destroyAllWindows()
        print('ERROR :: Video recording aborted!')
        break
