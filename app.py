import pygame
import game_config as gc

from pygame import display, event, image, transform
from animal import Animal
from time import sleep

def find_index(x, y):
    '''
    This function assign the index for each square image in the game.
    '''
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDES + col
    return index

pygame.init()

#Loading up the screen and the images for the game
display.set_caption('Cat Memory Matching Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
matched = transform.scale(image.load('other_assets/matched.png'), (gc.SCREEN_SIZE, gc.SCREEN_SIZE))

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

while running:
    '''
    This while loop let the keyboard and the mouse interact with the game.
    '''
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]


    screen.fill((255, 255, 255))

    total_skipped = 0

    for _, tile in enumerate(tiles):
        '''
        This loop displays the image when the player click on the tile.
        '''
        image_i = tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped +=1

    display.flip()

    if len(current_images) == 2:
        '''
        This conditional statement check whether two current displayed image are identical.
        If yes, match them and let them disappear.
        '''
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.5)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.5)
            current_images = []

    if total_skipped == len(tiles):
        running = False

    display.flip()

print('Goodbye!')