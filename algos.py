import pygame

def draw_lines(arr, screen, color):
    """ draws the lines to visualize the sorting """
    y_start = 700
    x_start = 100
    screen.fill("black")
    for i in range (len(arr)):
        x_pos = x_start + 5 * i
        y_end = y_start - 3 * arr[i]
        
        pygame.draw.line(screen, color, (x_pos, y_start), (x_pos, y_end))
    pygame.display.update()


def is_sorted(arr):
    """ used when figure should turn green when done sorting """
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

def selectionsort(arr, screen):
    for i in range(len(arr)):
        pygame.time.delay(50)  # slow it down to make it watchable
        min_elem_idx = i  # index of smallest element in unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_elem_idx] > arr[j]:
                min_elem_idx = j  # found new smallest element
        arr[i], arr[min_elem_idx] = arr[min_elem_idx], arr[i]
        draw_lines(arr, screen, "white")


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
