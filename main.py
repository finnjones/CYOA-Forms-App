import pygame, os, time
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
playerSpriteL = [pygame.image.load(FlexyPath + "/Sprites/1.png"), pygame.image.load(FlexyPath + "/Sprites/2.png"), pygame.image.load(FlexyPath + "/Sprites/3.png"), pygame.image.load(FlexyPath + "/Sprites/4.png"), pygame.image.load(FlexyPath + "/Sprites/5.png"), pygame.image.load(FlexyPath + "/Sprites/6.png"), pygame.image.load(FlexyPath + "/Sprites/7.png"), pygame.image.load(FlexyPath + "/Sprites/8.png"), pygame.image.load(FlexyPath + "/Sprites/9.png"), pygame.image.load(FlexyPath + "/Sprites/10.png")]
playerSpriteR = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/1.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/2.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/3.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/4.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/5.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/6.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/7.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/8.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/9.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/10.png"), True, False)]
bulletSprite = []
steveSprite = pygame.image.load(FlexyPath + "/SteveJobs.png")
kd = False
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
        self.hitbox = (self.x + 17, self.y + 2, self.width, self.height)


    # def playerText(self):

    def draw(self, window, direction):
        self.direction = direction
        global lastFacing
        if self.changeSprite > 48:
            self.changeSprite = -1
        self.changeSprite += 1
        
        print(self.changeSprite)

        if direction == -1:
            lastFacing = "left"
            window.blit(playerSpriteL[self.changeSprite//5], (self.x, self.y))
        elif direction == 1:
            lastFacing = "right"
            window.blit(playerSpriteR[self.changeSprite//5], (self.x, self.y))
        
        else:
            if lastFacing == "right":
                window.blit(playerSpriteR[0], (self.x, self.y))
            if lastFacing == "left":
                window.blit(playerSpriteL[0], (self.x, self.y))
                

       

        self.hitbox = (self.x + 17, self.y + 2, self.width, self.height)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

class npc(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        self.hitbox = (self.x, self.y, self.width, self.height)


    

    def draw(self, window):
        window.blit(steveSprite, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        showText("Press 'o' To Talk", 20, (steveNPC.x - 20, steveNPC.y - 30), black)

        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    

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


def textRender(text, font , colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def showText(text, fontSize, textloc, colour):
    Font = pygame.font.Font(FlexyPath+'/Quicksand/Quicksand-VariableFont_wght.ttf', fontSize)
    finalText, textLoc = textRender(text, Font , colour)
    window.blit(finalText, textloc)

def speechF(text, attach):
    if attach == True:
        speechCloud.x = person.x + 65
        speechCloud.y = person.y - 135
    else:
        speechCloud.x = steveNPC.x + 65
        speechCloud.y = steveNPC.y - 135
    speechCloud.draw(window)
    showText(text, 20, (speechCloud.x + 50, speechCloud.y + 10), black)


def reDraw(facing):
    global kd
    window.blit(bg,(0,0))
    person.draw(window, facing)
    if kd == True:
        # npc.stevetext()
        speechF("hello, sup nerd", True)
        speechF("egg", False)



        # kd = False


    
    for b in bullets:
        if b.x < person.x + 600:
            b.draw(window)
    steveNPC.draw(window)
    pygame.display.update()


person = player(500,700,64,100)
steveNPC = npc(1000,700,77, 143)
speechCloud = speech(100,100)

bullets = {}

running = True
facing = 1
wasFacing = 1
kd = False
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
    
    if keys[pygame.K_i]:
        bullets[bullet(person.x + person.width/2, person.y + person.height/2, 6, (0,0,0), 1)] = wasFacing
    
    


    if steveNPC.x != 700:
        steveNPC.x -= 4

    if person.hitbox[0] + person.hitbox[2] > steveNPC.hitbox[0] and person.hitbox[0] < steveNPC.hitbox[0] + steveNPC.hitbox[2]:
        if person.hitbox[1] + person.hitbox[3] > steveNPC.hitbox[1] and person.hitbox[1] < steveNPC.hitbox[1] + steveNPC.hitbox[3]:
            if keys[pygame.K_o]:
                kd = True



    reDraw(facing)




pygame.quit()