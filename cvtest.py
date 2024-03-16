import cv2

# Replace 0 with the correct index if you have multiple cameras
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
ret, frame = cap.read()

# Check if the frame was captured
if ret:
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)  # Wait for a key press to exit
    cv2.destroyAllWindows()
else:
    print("Failed to capture frame")

cap.release()
