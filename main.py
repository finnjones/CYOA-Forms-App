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
playerSpriteL = [pygame.image.load(FlexyPath + "/Sprites/1.png"), pygame.image.load(FlexyPath + "/Sprites/2.png"), pygame.image.load(FlexyPath + "/Sprites/3.png"), pygame.image.load(FlexyPath + "/Sprites/4.png"), pygame.image.load(FlexyPath + "/Sprites/5.png"), pygame.image.load(FlexyPath + "/Sprites/6.png"), pygame.image.load(FlexyPath + "/Sprites/7.png"), pygame.image.load(FlexyPath + "/Sprites/8.png")]
playerSpriteR = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/1.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/2.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/3.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/4.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/5.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/6.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/7.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/8.png"), True, False), ]
# for i in playerSpriteL:
#     print
# playerSpriteR
bulletSprite = []

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
        self.changeSprite = 0
        self.direction = "left"

    def draw(self, window, direction):
        self.changeSprite += 1
        print(self.changeSprite)
        if direction == "left":
            window.blit(playerSpriteL[self.changeSprite//4], (self.x, self.y))
        else:
            window.blit(playerSpriteR[self.changeSprite//4], (self.x, self.y))

        if self.changeSprite > 26:
            self.changeSprite = -1

class bullet(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self,win):
        pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)


def reDraw(facing):
    window.blit(bg,(0,0))
    person.draw(window, facing)
    for b in bullets:
        if b.x < person.x + 600:
            b.draw(window)
    

    
    pygame.display.update()

person = player(500,700,64,64)

bullets = []

running = True
facing = ""
while running:
    clock.tick(100)

    for b in bullets:
        if b.x < 1920 and b.x > -10:
            b.x += b.vel


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

            
    if keys[pygame.K_ESCAPE]:
        running = False

    elif keys[pygame.K_a]:
        facing = "left"
        person.x -= person.speed

    elif keys[pygame.K_d]:
        facing = "right"
        person.x += person.speed
    
    if keys[pygame.K_w]:
        person.jump = True

    if person.jump == True:
        if person.jumpTimer >= -(person.jumpTime):
            person.jumpTimer -= 1.5
        if person.jumpTimer > -(person.jumpTime):
            person.y -= person.jumpTimer

        else:
            person.jump = False
            person.jumpTimer = person.jumpTime
    
    if keys[pygame.K_p]:
        bullets.append(bullet(person.x + person.width/2, person.y + person.height/2, 6, (0,0,0), 1))


    reDraw(facing)




pygame.quit()




