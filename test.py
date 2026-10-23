import cv2

print("Robodog project Started!")

camera = cv2.VideoCapture(0)
lower = (35, 80, 50)
upper = (85, 255, 255)
close_area = 50000
while True:
    success, frame = camera.read()
    if not success:
     print("image not found") 
     break 
    frame_width = frame.shape[1]
    left_limit = frame_width//3
    right_limit = 2 * frame_width//3

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    cv2.imshow("mask", mask)
    
    contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
    command = "SEARCHING"
    if contours:
     largest = max(contours, key=cv2.contourArea)
     x, y, w, h = cv2.boundingRect(largest)
     center_x = x+w//2 
     center_y = y+h//2
     ball_area = w * h
     
     if ball_area > close_area:
       command = "STOP"
     else:
      if center_x < left_limit:
       command = "TURN LEFT"
      elif center_x >  right_limit:
       command = "TURN RIGHT"
      else:
       command = "GO STRAIGHT"  

     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
     cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

     if command == "STOP":
       text_color = (0, 0, 255)
     else:
       text_color = (0, 255, 0)

     cv2.putText(
        frame,
        command,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        text_color,
        2
     )

     
    cv2.imshow("RoboDog Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
     print("stopped")
     break

camera.release()
cv2.destroyAllWindows()