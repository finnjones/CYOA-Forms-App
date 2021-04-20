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

speechBubble = pygame.image.load(FlexyPath + "/Bubble.png")
playerSprite = pygame.image.load(FlexyPath + "/Player.png")
playerSpriteL = [pygame.image.load(FlexyPath + "/Sprites/1.png"), pygame.image.load(FlexyPath + "/Sprites/2.png"), pygame.image.load(FlexyPath + "/Sprites/3.png"), pygame.image.load(FlexyPath + "/Sprites/4.png"), pygame.image.load(FlexyPath + "/Sprites/5.png"), pygame.image.load(FlexyPath + "/Sprites/6.png"), pygame.image.load(FlexyPath + "/Sprites/7.png"), pygame.image.load(FlexyPath + "/Sprites/8.png")]
playerSpriteR = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/1.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/2.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/3.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/4.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/5.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/6.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/7.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/8.png"), True, False), ]
bulletSprite = []

bg = pygame.image.load(FlexyPath + "/wallpaper.png")
lastFacing = "right"
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

    def draw(self, window, direction):
        self.direction = direction
        global lastFacing
        self.changeSprite += 1

        if direction == -1:
            lastFacing = "left"
            window.blit(playerSpriteL[self.changeSprite//4], (self.x, self.y))
        elif direction == 1:
            lastFacing = "right"
            window.blit(playerSpriteR[self.changeSprite//4], (self.x, self.y))
        
        else:
            if lastFacing == "right":
                window.blit(playerSpriteR[1], (self.x, self.y))
            if lastFacing == "left":
                window.blit(playerSpriteL[1], (self.x, self.y))

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

    def draw(self,window):
        pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)

class speech(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self,window):
        window.blit(speechBubble, (self.x, self.y))


# class words(object):
#     def __init__(self, text, fontSize, textloc, colour):
#         self.text = text
#         self.fontSize = fontSize
#         self.textloc = textloc
#         self.colour = colour
#         self.Font = pygame.font.Font(FlexyPath+'/Quicksand-VariableFont_wght.ttf', fontSize)
#         self.finalText, self.textLoc = textRender(self.text, self.Font , self.colour)
#         window.blit(self.finalText, self.textloc)
def textRender(text, font , colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def showText(text, fontSize, textloc, colour):
    Font = pygame.font.Font(FlexyPath+'/Quicksand/Quicksand-VariableFont_wght.ttf', fontSize)
    finalText, textLoc = textRender(text, Font , colour)
    window.blit(finalText, textloc)

def reDraw(facing):
    window.blit(bg,(0,0))
    person.draw(window, facing)
    speechCloud.x = person.x + 65
    speechCloud.y = person.y - 135

    speechCloud.draw(window)
    showText("hello", 20, (speechCloud.x+ 50, speechCloud.y + 10), black)

    for b in bullets:
        if b.x < person.x + 600:
            b.draw(window)
    
    pygame.display.update()


person = player(500,700,64,64)
speechCloud = speech(100,100)

bullets = {}

running = True
facing = 1
wasFacing = 1

while running:
    clock.tick(100)
    
    for b in list(bullets):
        if b.x < 1920 and b.x > -10:
            
            b.x += b.vel * bullets[b]
        else:
            del bullets[b]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

            
    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_a]:
        facing = -1
        wasFacing = -1

        person.x -= person.speed
    elif keys[pygame.K_d]:
        facing = 1
        wasFacing = 1

        person.x += person.speed
    else:
        facing = 0
    
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
        bullets[bullet(person.x + person.width/2, person.y + person.height/2, 6, (0,0,0), 1)] = wasFacing
        # print(bullets)



    reDraw(facing)




pygame.quit()