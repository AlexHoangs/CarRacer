from logging.handlers import RotatingFileHandler
import pygame

# image scaling function
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

# function to rotate image based on angle
def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle) # rotate around top left hand corner
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center) # 
    win.blit(rotated_image, new_rect.topleft)

# half of text width - half of screen width u get top left hand position
def blit_text_center(win, font, text):
    render = font.render(text, 0.5, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, win.get_height()/2 - render.get_height()/2))