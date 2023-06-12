import pygame
import random
import algos
from clickable_text import ClickableText
from selection_sort import Sorter, SelectionSorter

def stationary_view(screen, bg_color, sorter):
    screen.fill(bg_color)
    if sorter.is_done():
        sorter.draw((0, 255, 0), sorter.array)
    else:
        sorter.draw((255, 255, 255), sorter.array)


def main():
    # variables
    width = 1280
    height = 720
    running = True
    fps = 60
    bg_color = "black"
    line_color = "white"

    pygame.init()
    pygame.display.set_caption("Sorting visualizer")
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    sorter = SelectionSorter(screen)

    while running:
        execute = False
        keys = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = True
                if event.key == pygame.MOUSEBUTTONDOWN:
                    # if clicked on button
                        # do stuff
                    pass

        if execute:

            execute = False
            sorter.sort()

        stationary_view(screen, bg_color, sorter) 
   
        pygame.display.flip()
        
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()