# Python program to create a robot.
   
# importing cv2 
import cv2 
import numpy as np
height=512
width=512
image = np.zeros((height,width,3), np.uint8)
    
# Window name in which image is displayed
window_name = 'Image'
  
    
#-----Body-------------

# represents the top left corner of rectangle 
start_point = (200, 200) 
  
# represents the bottom right corner of rectangle 
end_point = (350, 350) 
  
# Blue color in BGR 
color = (255, 255, 0) 
  
# Line thickness of 2 px 
thickness = 2
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 
 
#-------Head-----------

# represents the top left corner of rectangle 
start_point = (230, 100) 
  
# represents the bottom right corner of rectangle 
end_point = (320, 200) 
  
# Blue color in BGR 
color = (0, 255, 255) 
  
# Line thickness of 2 px 
thickness = -1
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 
 
#-------Left leg-----------

# represents the top left corner of rectangle 
start_point = (200, 350) 
  
# represents the bottom right corner of rectangle 
end_point = (230, 500) 
  
# Blue color in BGR 
color = (255, 0, 255) 
  
# Line thickness of 2 px 
thickness = -1
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 
    
#-------right leg-----------

# represents the top left corner of rectangle 
start_point = (320, 350) 
  
# represents the bottom right corner of rectangle 
end_point = (350, 500) 
  
# Blue color in BGR 
color = (255, 0, 255) 
  
# Line thickness of 2 px 
thickness = -1
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 

#-------Left hand-----------

# represents the top left corner of rectangle 
start_point = (100, 215) 
  
# represents the bottom right corner of rectangle 
end_point = (200, 240) 
  
# Blue color in BGR 
color = (93, 200, 195) 
  
# Line thickness of 2 px 
thickness = -1
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 

#-------right hand-----------

# represents the top left corner of rectangle 
start_point = (350, 215) 
  
# represents the bottom right corner of rectangle 
end_point = (450, 240) 
  
# Blue color in BGR 
color = (93, 200, 195) 
  
# Line thickness of 2 px 
thickness = -1
  
# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 



#-------Right eye-----------    
    
# Center coordinates
center_coordinates = (260, 130)
 
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
center_coordinates = (290, 130)
 
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
    
# Displaying the image 
cv2.imshow(window_name, image)

cv2.imwrite('output_robot.png', image) 
