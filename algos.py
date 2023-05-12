import pygame

def draw_lines(arr, screen, color):
    """ draws the lines to visualize the sorting """
    y_start = 600
    screen.fill("black")
    for i in range (len(arr)):
        x_pos = 100 + 5 * i
        y_end = 600 - 3 * arr[i]
        
        pygame.draw.line(screen, color, (x_pos, y_start), (x_pos, y_end))
    pygame.display.update()


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))


def bubblesort(arr, screen):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                draw_lines(arr, screen, "white")
                
    draw_lines(arr, screen, (0, 255, 0))


def mergesort(arr, screen):
# todo: now, it only visualizes the current sublist, want to
# show the whole array all the time.
# could send in start index for current sublist together with the 
# "parent array" because then for example:
# start_index = 5, then draw 0->4 from parent array, 
# start_index->start_index+len(current_sub_array), and then the rest 
    if len(arr) > 1: 
        mid_idx = len(arr) // 2
        left_sub, right_sub = arr[:mid_idx], arr[mid_idx:]
        mergesort(left_sub, screen)
        mergesort(right_sub, screen)

        i = j = k = 0
        while len(left_sub) > i and len(right_sub) > j:
            if left_sub[i] <= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            draw_lines(arr, screen, "white")
            k += 1
        # comes here if len(left_sub) > len(right_sub)
        while len(left_sub) > i:
            arr[k] = left_sub[i]
            draw_lines(arr, screen, "white")
            i += 1
            k += 1
        
        # comes here if len(right_sub) > len(left_sub)
        while len(right_sub) > j:
            arr[k] = right_sub[j]
            draw_lines(arr, screen, "white")
            j += 1
            k += 1
            

def quicksort(arr):
    pass

def heapsort(arr):
    pass

def selectionsort(arr):
    pass

def insertionsort(arr, screen):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            draw_lines(arr, screen, "white")
            j -= 1
        arr[j + 1] = temp
        draw_lines(arr, screen, "white")


# testing
# test_array = [2, 4, 1, 7, 3, 6, 5]
# print("bubblesort:  ", bubblesort(test_array))
# print("bogosort:    ", bogosort(test_array))
# print("mergesort:   ", mergesort(test_array))

# merge
# in: [2, 4, 1, 3]
# left: [2, 4], right: [1, 3]


