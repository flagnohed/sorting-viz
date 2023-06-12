import pygame


class ClickableText: 
    def __init__(self, text, action, screen, x, y):
        self.width = 80
        self.height = 20
        self.text = text
        self.action = action
        self.x = x
        self.y = y
        self.screen = screen
        self.font = pygame.font.SysFont('Corbel',35)
    
    def draw(self):
        text_object = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_object, (self.x, self.y))
