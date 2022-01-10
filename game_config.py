import os

'''
This file includes the game configuration so other programmers can modify the numbers if they want
'''

IMAGE_SIZE = 128
SCREEN_SIZE = 768
NUM_TILES_SIDES = 6
NUM_TILES_TOTAL = 36
MARGIN = 4

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

assert len(ASSET_FILES) == 18

