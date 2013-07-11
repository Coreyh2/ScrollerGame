
# Source File Name: LineRunner.py
# Author's Name: Corey Haggan 
# Last Modified By: Corey Haggan 
# Date Last Modified: July 10, 2013 
# Program Desciption: Create a Game.
# Version History: Added a instructions menu added, scrolling background
import pygame, random
pygame.init()
screen = pygame.display.set_mode((640, 480))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
        self.image = pygame.Surface((60, 60))
        self.image = pygame.image.load("stickman.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndHit = pygame.mixer.Sound("stickman_sound.ogg")
            

        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (550, mousey)
        if mousey > 350:
            self.rect.center = (550, 350)


        
class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = random.randrange(3, 11)
        self.reset()

        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randrange(20, 400)
        
class healthBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("health-icon.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 8
        self.reset()

        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.left > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.left = -4000
        self.rect.centery = random.randrange(0, 400)
        
        
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screen.get_width(), 100))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 0
        self.reset()

        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.left = 0
        #self.rect.centery = random.randrange(0, screen.get_width())
        self.rect.centery = 450

class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space_background.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.left += self.dx
        if self.rect.left > 0:
            self.reset() 
    
    def reset(self):
        self.rect.right = screen.get_width()
        self.image  
        
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.healthpoints = 5
        self.score = 0
        
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Health: %d, score: %d" % (self.healthpoints, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
    
        
def game():
    
    pygame.mixer.music.load("Stickman_background.ogg")

    pygame.display.set_caption("Line Runner dodge the obstacles")
    
    background = pygame.Surface(screen.get_size())

    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    stickman = Player()
    obstacles = Box()
    obstacles1 = Box()
    obstacles2 = Box()
    health = healthBox()
    floor = Floor()
    space = Space()
    score = Score()
    

    
    pygame.mixer.music.play(-1, 0.0)
   
    playerSprites = pygame.sprite.OrderedUpdates(space, floor, stickman)
    obstacleSprites = pygame.sprite.Group(obstacles, obstacles1, obstacles2)
    healthSprites = pygame.sprite.Group(health)
    scoreSprite = pygame.sprite.Group(score)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
                

       
        
        
        if stickman.rect.colliderect(health.rect) and clock.tick() > 2:
            score.healthpoints += 1
        if clock.get_rawtime() > 1:
            score.score += 1 
            
        if score.healthpoints <= 0:
            return score.score
        if stickman.rect.colliderect(health.rect):
            health.reset()
            score.healthpoints += 1


        #check collisions
        hitObstacle = pygame.sprite.spritecollide(stickman, obstacleSprites, False)
        if hitObstacle:
            score.healthpoints -= 1
            stickman.sndHit.play()
            if score.healthpoints <= 0:
                print("You Lose")
                keepGoing = False
            for theObstacle in hitObstacle:
                theObstacle.reset()
                
       
        hitHealth = pygame.sprite.spritecollide(stickman, healthSprites, False)
        if hitHealth:
            scoreboard.healthpoints += 1
            for theHealth in hitHealth:
                theHealth.reset()
        # to refresh the frames, and stop them from dragging.
        playerSprites.clear(screen, background)
        obstacleSprites.clear(screen, background)
        healthSprites.clear(screen, background)
        scoreSprite.clear(screen, background)
        
        playerSprites.update()
        obstacleSprites.update()
        healthSprites.update()
        scoreSprite.update()
        
        playerSprites.draw(screen)
        obstacleSprites.draw(screen)
        healthSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
        
        #show mouse cursor
    pygame.mouse.set_visible(True) 
    return score.score

def instructions(score):
    stickman = Player()
    space = Space()
    
    
    background = pygame.Surface(screen.get_size())

    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    allSprites = pygame.sprite.OrderedUpdates(space, stickman)
    insFont = pygame.font.SysFont(None, 50)


    instructions = (
    "Space Line Runner.   Last score: %d" % score,
    "Instructions:  You Have to navaigate threw,",
    "the cold depths of space",
    "",
    "dodge the asteriods,",
    "and make it to the end",    
    "where you will be teleported home",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
    return donePlaying


def endScreen(score):
    stickman = Player()
    space = Space()
    
    
    background = pygame.Surface(screen.get_size())

    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    allSprites = pygame.sprite.OrderedUpdates(space, stickman)
    insFont = pygame.font.SysFont(None, 50)


    instructions = (
    "Space Line Runner.   Last score: %d" % score,
    "Hope you enjoyed this game", 
    "",
    "",
    "just click anywhere on the screen,",
    "if you would like to Play Again,",
    "",
    "Otherwise Press the ESC key,",
    "or the red X box to quit"


    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 0, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
    return donePlaying

    
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
            donePlaying = endScreen(score)

if __name__ == "__main__":
    main()
            
