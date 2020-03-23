#This is my project

red = 100
red2 = 50
green = 0
green2 = 100
blue = 0
blue2 = 0
readiness = 0
readiness2 = 200

pixel_brightness = (red + green + blue) / 3
pixel_brightness2 = (red2 + green2 + blue2) / 3

mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)
