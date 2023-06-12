import pygame
import random


class Sorter(object):
    def __init__(self, screen):
        self.screen = screen
        self.array_accesses = self.comparisons = self.delay = self.num_elems = 0

    def reg_comparison(self, list_of_indexes):
        self.comparisons += 1
        self.draw((0, 0, 255), list_of_indexes)

    def reg_array_access(self, list_of_indexes):
        self.array_accesses += 1
        self.draw((255, 0, 0), list_of_indexes)

    def is_done(self):
        """ used when figure should turn green when done sorting """
        return all(self.array[i] <= self.array[i+1] 
                   for i in range(len(self.array) - 1))
    
    def show_stats(self):
        font = pygame.font.Font('freesansbold.ttf', 14)
        array_access_text = font.render(f"Array accesses: {self.array_accesses}", False, (255, 255, 255))
        comparisons_text = font.render(f"Comparisons: {self.comparisons} ", False, (255, 255, 255))
        delay_text = font.render(f"Delay: {self.delay} ms", False, (255, 255, 255))  
        num_elems_text = font.render(f"Number of elements: {self.num_elems}", False, (255, 255, 255))                
       
        self.screen.blit(array_access_text, (10, 10))
        self.screen.blit(comparisons_text, (10, 30))
        self.screen.blit(delay_text, (10, 50))
        self.screen.blit(num_elems_text, (10, 70))



# den här kan man färglägga sorterade staplar
# genom att färga de 'i' som har itererats!
class SelectionSorter(Sorter):
    def __init__(self, screen):
        super(SelectionSorter, self).__init__(screen)
        self.delay = 0
        self.num_elems = 100
        self.array = [i for i in range(1, self.num_elems + 1)]
        
        random.shuffle(self.array)
        
    def sort(self):
        for i in range(self.num_elems):
            small = i  # assume ith element is smallest

            for j in range(i + 1, self.num_elems):  # rest of array
                if self.array[small] > self.array[j]:
                    small = j  # found new smallest element
                self.reg_comparison([small, j])
                self.reg_array_access([small, j])

            self.array[i], self.array[small] = self.array[small], self.array[i]
            self.reg_array_access([i, small])
        
        # draw everything in green or something here
        # print([i-1 for i in self.array])
        self.draw((0, 255, 0), list_of_indexes=[i-1 for i in self.array])

    def draw(self, standout_color, list_of_indexes):
        # vill alltid ha 100 i mellanrum på sidorna
        # så arrayen får ta upp x: [100, 1180]
        y_bottom = 700
        x_start = 140
        rect_w = 10
        x_end = 1140  # here array ends (right edge of last element)
        self.screen.fill((0, 0, 0))
        
        for i in range(self.num_elems):
            color = (255, 255, 255)
            x_pos = x_start + 10 * i
            y_top = y_bottom - 5 * self.array[i]
            if i in list_of_indexes:
                color = standout_color
           
            pygame.draw.rect(self.screen, color, 
                             pygame.Rect(x_pos, y_top, 
                                         rect_w, 5 * self.array[i]), 1, 1)
            
        self.show_stats()

        pygame.display.update()

