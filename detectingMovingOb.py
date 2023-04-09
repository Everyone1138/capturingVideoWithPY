import cv2, time

first_frame=None


video=cv2.VideoCapture(0)



while True:
  
    check, frame = video.read()

    # print(check)
    # print(frame)


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # this does the color
    gray=cv2.GaussianBlur(gray,(21,21),0)
    # time.sleep(3)
    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_delta=cv2.threshold(delta_frame, 30, 255,cv2.THRESH_BINARY)[1]

    # thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # for x, y, w, h in faces:
    #     img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Capturing",gray)
    cv2.imshow("Delta Frame",thresh_delta)
    # cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Dilate",delta_frame)



    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)
    print()
    print()


    if key==ord('q'):
        break


video.release()
cv2.destroyAllWindows
