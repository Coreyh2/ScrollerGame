# Source File Name: LineRunner.py
# Author's Name: Corey Haggan 
# Last Modified By: Corey Haggan 
# Date Last Modified: July 11, 2013 
# Program Desciption: Create a Game.
# Version History: Added a new box class to create diffrent obstacle speeds and sizes
import pygame, random
pygame.init()
screen = pygame.display.set_mode((640, 480))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load("stickman.gif")
        #self.image = self.image.convert()
        self.image = pygame.Surface((30, 30))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()


    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (550, mousey)


        
class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 8
        self.reset()

        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randrange(0, screen.get_width())

class Box1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 6
        self.reset()

        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, screen.get_width())
        
        
        
        
        
        
def main():

    pygame.display.set_caption("Line Runner dodge the obstacles")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    stickman = Player()
    obstacles = Box()
    obstacles1 = Box1()
    
    
    allSprites = pygame.sprite.Group(stickman, obstacles, obstacles1, )
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
