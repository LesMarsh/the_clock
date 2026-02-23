#!/usr/bin/env python3

# The clock LED pipeline
import threading
import signal
import sys
# import board
# import neopixel
import time
from rpi_ws281x import PixelStrip, Color

from led_functions_rpi import fill, random_choices, fade_in, fade_out, crossfade, fade_seq, clock, fades


# Assign strips to variables
pixels1 = PixelStrip(65, 18, dma = 10) # Use pixels 3 to 65
pixels2 = PixelStrip(66, 21, dma = 10)

# Initialise GPIO
pixels1.begin()
pixels2.begin()

# Define groups of pixels for fade functions
numbers = [
    [1, 2, 3, 4, 5]
    , [6, 7, 8, 9, 10]
    , [11, 12, 13, 14, 15]
    , [16, 17, 18, 19, 20]
    , [21, 22, 23, 24, 25]
    , [26, 27, 28, 29, 30]
    , [31, 32, 33, 34, 35]
    , [36, 37, 38, 39, 40]
    , [41, 42, 43, 44, 45]
    , [46, 47, 48, 49, 50]
    , [51, 52, 53, 54, 55]
]

# Clean-up functions

# Reset pixels to black
def cleanup():
    fill(pixels1, Color(0, 0, 0))
    fill(pixels2, Color(0, 0, 0))
    pixels1.show()
    pixels2.show()
    time.sleep(2)
#     for p in [pixels1, pixels2]:
#         for i in range(p.numPixels()):
#             p.setPixelColor(i, Color(0, 0, 0))
        
# Handle Ctrl+C
# def exit_handler(sig, frame):
#     cleanup()
#     sys.exit(0)
#     
# signal.signal(signal.SIGINT, exit_handler)
# signal.signal(signal.SIGTERM, exit_handler)

print("Made it 1")
# clock(pixels2, 1, 59, 2)
try:
    # Create threads
    t1 = threading.Thread(target = clock, args = (pixels1, 3, 55, 5, 255, 255, 255))
    print("Made it 2")
    t2 = threading.Thread(target = fade_seq, args = (pixels2, numbers))
    print("Made it 3")
    
    # Start threads
    t1.start()
    t2.start()
    print("Made it 4")
    
    # Join threads
    t1.join()
    t2.join()
    print("Made it 5")
    
finally:
    cleanup()

