#This is my project

import statistics

def calculate_pixel_brightness(x,y,z):
    return statistics.mean([x, y, z])

pixels = [
    {'red': 100, 'green': 0, 'blue': 0},
    {'red2': 50, 'green2': 100, 'blue2': 0},
]
pixel_brightness = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels
mean_brightness = statistics.mean(pixel_brightness)
print(mean_brightness)
