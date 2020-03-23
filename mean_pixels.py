#This is my project

import statistics

def calculate_pixel_brightness(x, y, z):
    """
    Calculates the brightnss of a pixel from its r,g,b values
    :param x: the red value of pixel
    :param y: the green value of pixel
    :param z: the blue value of pixel
    :return: the brightness of the pixel
    """
    return statistics.mean([x, y, z])

pixels = [
    {'red': 100, 'green': 0, 'blue': 0},
    {'red2': 50, 'green2': 100, 'blue2': 0},
]
pixel_brightness = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]
mean_brightness = statistics.mean(pixel_brightness)
print(mean_brightness)
