import cv2
import numpy as np

frame = cv2.imread('sudoku.png')
edges = cv2.Canny(frame,100,200)

minLineLength=50
maxLineGap=50
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)

blankImage = np.zeros(frame.shape)

for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(blankImage,(x1,y1),(x2,y2),(0,255,0),2)



cv2.imshow("original", frame)
cv2.imshow("lines", blankImage)
cv2.waitKey(-1)
