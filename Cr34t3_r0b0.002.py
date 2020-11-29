#!/usr/bin/python
# Python program to create a robot.
   
# importing cv2 
import cv2 
import numpy as np
height=512
width=512

    
#Function to create robot
def robo_craft(image, x, y):
  
    #-----Body-------------

    # represents the top left corner of rectangle 
    start_point = (x +200, y +200) 

    # represents the bottom right corner of rectangle 
    end_point = (x +350, y +350) 

    # Blue color in BGR 
    color = (95, 215, 125) 

    # Line thickness of 2 px 
    thickness = -999

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 

    #-------Head-----------

    # represents the top left corner of rectangle 
    start_point = (x +230, y +100) 

    # represents the bottom right corner of rectangle 
    end_point = (x +320, y +200) 

    # Blue color in BGR 
    color = (95, 255, 105) 

    # Line thickness of 2 px 
    thickness = -121

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 

    #-------Left leg-----------

    # represents the top left corner of rectangle 
    start_point = (x +200, y +350) 

    # represents the bottom right corner of rectangle 
    end_point = (x +230, y +500) 

    # Blue color in BGR 
    color = (98, 208, 203) 

    # Line thickness of 2 px 
    thickness = -1

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 

    #-------right leg-----------

    # represents the top left corner of rectangle 
    start_point = (x +320, y +350) 

    # represents the bottom right corner of rectangle 
    end_point = (x +350, y +500) 

    # Blue color in BGR 
    color = (98, 208, 203) 

    # Line thickness of 2 px 
    thickness = -1

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 

    #-------Left hand-----------

    # represents the top left corner of rectangle 
    start_point = (x +100, y +215) 

    # represents the bottom right corner of rectangle 
    end_point = (x +200, y +240) 

    # Blue color in BGR 
    color = (93, 200, 195) 

    # Line thickness of 2 px 
    thickness = -1

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 

    #-------right hand-----------

    # represents the top left corner of rectangle 
    start_point = (x +350, y +215) 

    # represents the bottom right corner of rectangle 
    end_point = (x +450, y +240) 

    # Blue color in BGR 
    color = (93, 200, 195) 

    # Line thickness of 2 px 
    thickness = -1

    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 



    #-------Right eye-----------    

    # Center coordinates
    center_coordinates = (x +260, y +130)

    # Radius of circle
    radius = 10

    # Red color in BGR
    color = (0, 0, 0)

    # Line thickness of -1 px
    thickness = -1

    # Using cv2.circle() method
    # Draw a circle of red color of thickness -1 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    #-------Left eye---------

    # Center coordinates
    center_coordinates = (x +290, y +130)

    # Radius of circle
    radius = 10

    # Red color in BGR
    color = (0, 0, 0)

    # Line thickness of -1 px
    thickness = -1

    # Using cv2.circle() method
    # Draw a circle of red color of thickness -1 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    #------------------  
     
    return image

# initialize video writer
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
video_filename = 'output.avi'
out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

for x in range (-40, 40, 1):
    y=x
    print(x,y)
    im = np.zeros((height,width,3), np.uint8)
    image = robo_craft(image=im, x =x, y =y)
    #cv2.imwrite('output_robot_x=' + str(x) + '_y=' + str(y) + '.png', image)
    out.write(image)

# close out the video writer
out.release()    
    