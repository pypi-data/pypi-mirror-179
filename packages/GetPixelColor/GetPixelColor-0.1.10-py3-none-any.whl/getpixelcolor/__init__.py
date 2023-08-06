# python module for getting the color of a pixel on screen

# import the necessary modules
from io import BytesIO
import os
import platform
if (platform == "darwin"):
    from pasteboard import TIFF, Pasteboard
from PIL import Image
from sys import platform
import pyautogui

# define the function
# the function takes 2 arguments, the x and y coordinates of the pixel
# returns a tuple of the RGBA values of the pixel
def pixel(x, y):
    if (platform == "darwin"):
        os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',1,1 -c')
        im = Pasteboard().get_contents(TIFF)
        im = Image.open(BytesIO(im))
        return (im.getpixel((0,0)))
    elif (platform == "win32" or platform == "linux" or platform == "linux2"):
        # save the screenshot to /tmp
        im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, 1, 1))
        return (im.getpixel((0,0)))
    else:
        return ("Error: Unsupported operating system.")


