import cv2
import os

videos_dir = "src\\videos"
file_name = ""

for file_name in os.listdir(videos_dir):
    if os.path.isfile(os.path.join(videos_dir, file_name)):
        cap = cv2.VideoCapture(os.path.join(videos_dir, file_name))
        count_frame = 0
        while True:
            _, frame = cap.read()
            count_frame += 1
            print(f"src\\videos\\themes\\{file_name}")
            print(count_frame)
            if count_frame == 109:
                name = file_name.split(".")[0]
                # print(frame)
                # print(file_name)
                # cv2.imshow('Frame', frame)
                cv2.imwrite(f"src\\videos\\themes\\{name}.jpeg",frame)
                break




