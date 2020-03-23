#This is my project


def calculate_pixel_brightness(x,y,z):
    brightness = (x + y + z) / 3
    return brightness


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel_brightness = calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue'])

pixel2 = {'red2': 50, 'green2': 100, 'blue2': 0}
pixel_brightness2 = calculate_pixel_brightness(pixel2['red2'], pixel2['green2'], pixel2['blue2'])

mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)
