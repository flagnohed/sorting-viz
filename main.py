import pygame
import random
import algos

pygame.init()
pygame.display.set_caption("Sorting visualizer")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
fps = 60
bg_color = "black"
line_color = "white"

arr = [i for i in range(1, 200)]

# sorting methods available
methods = {
        "mergesort": algos.mergesort, 
        "bubblesort": algos.bubblesort,
        "insertionsort": algos.insertionsort,
        "selectionsort": algos.selectionsort
        }

chosen_method = "selectionsort"

def run_sort(method_key):
    methods[method_key](arr, screen)

random.shuffle(arr)

while running:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if keys[pygame.K_SPACE]:
        execute = True

    if execute:
        run_sort(chosen_method)
        # algos.mergesort(arr, screen)
    else:
        screen.fill(bg_color)
        algos.draw_lines(arr, screen, line_color)
        

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()