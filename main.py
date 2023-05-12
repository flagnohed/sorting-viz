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
sort_method = "insertionsort"

# test arrays
arr = [i for i in range(1, 200)]
# arr = [5, 1, 2, 4, 3]
# arr = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

# sorting methods
methods = {"mergesort": algos.mergesort, 
           "bubblesort": algos.bubblesort,
           "insertionsort": algos.insertionsort}

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
        run_sort(sort_method)
        # algos.mergesort(arr, screen)
    else:
        screen.fill(bg_color)
        algos.draw_lines(arr, screen, line_color)
        

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()