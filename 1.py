# import cv2

# capture = cv2.VideoCapture('/home/iiitd/Purbasha/Measurement_Study_Whole_Folder/RAW_0.5_segmented_Videos/AINormal/mp4/AITr1cam8.mp4')

# while True:
#     isTrue, frame = capture.read()

#     # If the frame was not read correctly, break the loop
#     if not isTrue:
#         break

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv2.destroyAllWindows()






import cv2

group_size = 10

capture = cv2.VideoCapture('/home/iiitd/Purbasha/Measurement_Study_Whole_Folder/RAW_0.5_segmented_Videos/AINormal/mp4/AITr1cam8.mp4')

frames = []
groups = []

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        if frames:
            groups.append(frames)
        break

    frames.append(frame)

    if len(frames) == group_size:
        groups.append(frames)
        frames = []

capture.release()


for i, group in enumerate(groups):
    print(f"Processing group {i+1}")

    for j, frame in enumerate(group):
        cv2.imshow(f'Group {i+1} - Frame {j + 1}', frame)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break

    cv2.waitKey(0)

    # cv2.destroyAllWindows()

# cv2.destroyAllWindows()    




