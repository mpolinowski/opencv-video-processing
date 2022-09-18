import cv2

filename = 'security_cam'
video = cv2.VideoCapture('videos/'+filename+'.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
# print(width, height, frames, fps)

# get frame at a specific timestamp
# timestamp = '00:00:04.00'
timestamp = input('Enter timestamp in hh:mm:ss format: ')
hours, minutes, seconds = [float(i) for i in timestamp.split(':')]
# print(hours, minutes, seconds)

# get number of frames up to timestamp
trigger_frame = hours * 3600 * fps + minutes * 60 * fps + seconds * fps
# print(frames, trigger_frame)

# # get the first frame and see if successful
# success, frame = video.read()
# # initiate count
# count = 1
# # keep extracting frames as long as success is True
#     cv2.imwrite(f'images/{count}.jpg', frame)
#     success, frame = video.read()
#     count += 1


# Go to frame selected by timestamp
video.set(1, trigger_frame)
success, frame = video.read()

# save the frame into an image file
if success:
    cv2.imwrite(f'images/{filename}_{hours}-{minutes}-{seconds}.jpg', frame)