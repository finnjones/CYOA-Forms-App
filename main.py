import pygame, os
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

FlexyPath = os.path.dirname(os.path.abspath(__file__))


window = pygame.display.set_mode((1920 , 1080))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

playerSprite = pygame.image.load(FlexyPath + "/Player.png")
bg = pygame.image.load(FlexyPath + "/wallpaper.png")

class player(object):
    
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 7
        self.jumpTime = 30
        self.jumpTimer = 30
        self.jump = False

    def draw(self, window):
        window.blit(playerSprite, (self.x, self.y))


def reDraw():
    window.blit(bg,(0,0))
    person.draw(window)
    
    pygame.display.update()

person = player(500,700,64,64)
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

            
    if keys[pygame.K_ESCAPE]:
        running = False

    elif keys[pygame.K_a]:
        person.x -= person.speed

    elif keys[pygame.K_d]:
        person.x += person.speed
    
    if keys[pygame.K_SPACE]:
        person.jump = True

    if person.jump == True:
        if person.jumpTimer >= -(person.jumpTime):
            person.jumpTimer -= 1
        if person.jumpTimer <= person.jumpTime or person.jumpTimer >= person.jumpTime:
            person.y -= (person.jumpTimer ** 1)
        # elif person.jumpTimer < 0 and person.jumpTimer >= -(person.jumpTime):
        #     person.y -= (person.jumpTimer ** 1)
        else:
            person.jump = False
            person.jumpTimer = person.jumpTime
        

        
    

    reDraw()




pygame.quit()




