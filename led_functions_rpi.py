# LED functions

# Include all necessary packages to get LEDs to work with Raspberry Pi using the rpi package (rather than the neopixels package)

import time
import random
from rpi_ws281x import Color

# Define functions
def fill(pixels, colour):
    for i in range(pixels.numPixels()):
        pixels.setPixelColor(i, colour)

def random_choices(start, end, exclude):
    choices = [x for x in range(start, end - 1) if x != exclude]
    return (random.choice(choices))

def fade_in(pixels, fade_in, fade_increments, numbers):
        lights = numbers[fade_in]
        for n in range(0, 256, fade_increments):
            for i in lights:
                pixels.setPixelColor(i, Color(n, n, n))
            pixels.show()
            time.sleep(.01)
        time.sleep(2)

def fade_out(pixels, fade_out, fade_increments, numbers):
        lights = numbers[fade_out]
        for n in range(0, 256, fade_increments):
            for i in lights:
                pixels.setPixelColor(i, Color(255 - n, 255 - n, 255 - n))
            pixels.show()
            time.sleep(.01)
        time.sleep(2)

def crossfade(pixels, fade_in, fade_out, fade_increments, duration, numbers):
    fade_in = numbers[fade_in]
    fade_out = numbers[fade_out]

    for n in range(0, 256, fade_increments):
        for i in fade_in:
            pixels.setPixelColor(i, Color(n, n, n))
        for x in fade_out:
            pixels.setPixelColor(x, Color(255-n, 255-n, 255-n))
            if 255 - n <= fade_increments:
                pixels.setPixelColor(x, Color(0, 0, 0))
        pixels.show()
        time.sleep(.02)
    time.sleep(duration)


def fade_seq(pixels, numbers):
    print("Running fade_seq")
    fill(pixels, Color(0, 0, 0))
    pixels.show()
    time.sleep(2)
    print("Running fades 2")
    
    light_1 = random_choices(0, len(numbers), 0)
    fade_in(pixels, light_1, 2, numbers)
    print(f"Fading in {light_1}")
    while True:
        light_2 = random_choices(0, len(numbers), light_1)
        duration = random.randint(3, 10)
        speed = random.randint(1, 2)
        crossfade(pixels, light_2, light_1, speed, duration, numbers)
        print(f"Fading in {light_2}, fading out {light_1}")
        light_1 = random_choices(0, len(numbers), light_2)
        print(f"Setting new light 1: {light_1}")
        duration = random.randint(3, 10)
        speed = random.randint(1, 2)
        crossfade(pixels, light_1, light_2, speed, duration, numbers)



def clock(pixels, start = 3, end = 65, fade_increments = 5, r = 255, g = 255, b = 255):
    # Function that fades in LEDs one at a time in a clockwise motion
    # pixels: 
    # start: first pixel of sequence
    # end: last pixel of sequence
    # fade_increments: the steps in which the fade up occurs
    # r, g, b: end values to set for pixel colours

    # Start pixels black
    fill(pixels, Color(0, 0, 0))

    # Clock movement
    while True:
        # Fade in end pixel
        for n in range(0, 256, fade_increments):
            pixels.setPixelColor(end, Color(n, n, n))
            pixels.show()
            time.sleep(.01)
        time.sleep(1)
            
        # Fade in first pixel
        for n in range(0, 255, fade_increments):
            colour = Color(n, n, n)
            pixels.setPixelColor(start, colour)
            pixels.show()
            time.sleep(.01)
        time.sleep(1)
            
            
        # Loop to fade in and out all pixels between start and end
        for i in range(start, end - 1):
            # print(f"Pixel {i}")
    
            for n in range(0, 256, fade_increments):
                colour_in = Color(n, n, n)
                pixels.setPixelColor(i+1, colour_in)
                # print(f"Pixel i+1 ({i+1}) colour_in: {n}")
                colour_out = Color(255 - n, 255 - n, 255 - n)
                pixels.setPixelColor(i, colour_out)
                if 255 - n <= fade_increments:
                    pixels.setPixelColor(i, Color(0, 0, 0))
                # print(f"Pixel i ({i}) colour_out: {255 - n}")
                pixels.show()
                time.sleep(.01)
            pixels.setPixelColor(i, Color(0, 0, 0))
            time.sleep(.5)
            
        # Fade out end - 1
        for n in range(0, 256, fade_increments):
            colour = Color(255 - n, 255 - n, 255 - n)
            if 255 - n <= fade_increments:
                    colour = Color(0, 0, 0)
            pixels.setPixelColor(end-1, colour)
            pixels.show()
        time.sleep(.5)
        
        # Fade out end
        for n in range(0, 256, fade_increments):
            colour = Color(255 - n, 255 - n, 255 - n)
            if 255 - n <= fade_increments:
                    colour = Color(0, 0, 0)
            pixels.setPixelColor(end, colour)
            pixels.show()
        
        time.sleep(1)

            # Fade down
#             for n in range(255, 0, -fade_increments):
#                 colour = Color(n, n, n)
#                 pixels.setPixelColor(i, colour)
#                 pixels.show()
#                 time.sleep(.01)
#             pixels.setPixelColor(i, Color(0, 0, 0))
#             pixels.show()
#             time.sleep(.1)
             


    

def fades(pixels, start, end, fade_increments):
    print('Running fades')
    try:
        fill(pixels, Color(0, 0, 0))
        pixel2 = 10
        # Fade in
        while True:
            # Fade in end pixel
            
            pixel = random_choices(start, end, pixel2)
            for n in range(0, 256, fade_increments):
                pixels.setPixelColor(pixel, Color(n, n, n))
                pixels.show()
                time.sleep(.01)
            time.sleep(1)

            pixel2 = random_choices(start, end, pixel)

            for n in range(0, 256, fade_increments):
                colour_in = Color(n, n, n)
                pixels.setPixelColor(pixel2, colour_in)
                # print(f"Pixel i+1 ({i+1}) colour_in: {n}")
                colour_out = Color(255 - n, 255 - n, 255 - n)
                pixels.setPixelColor(pixel, colour_out)
                if 255 - n <= fade_increments:
                    pixels.setPixelColor(pixel, Color(0, 0, 0))
                # print(f"Pixel i ({i}) colour_out: {255 - n}")
                pixels.show()
                time.sleep(.01)
            pixels.setPixelColor(pixel, Color(0, 0, 0))
            time.sleep(1)
        
        
    finally:
        pass
