import pygame, os, time
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
brown = (139,69,19)
red = (255, 0, 0)

FlexyPath = os.path.dirname(os.path.abspath(__file__))


window = pygame.display.set_mode((1620 , 1000))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

speechBubble = pygame.image.load(FlexyPath + "/Images/Bubble.png")
actionImgL = [pygame.image.load(FlexyPath + "/Images/ActionImages/apple.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/money.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/money.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/repair.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/hand.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/slide.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/return.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/no.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/no.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/no.png")]
actionImgL2 = [pygame.image.load(FlexyPath + "/Images/ActionImages/torrent.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/ADB.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/matrix.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/steal.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/sell.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/ddos.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/matrix.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/connect.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/matrix.png"), pygame.image.load(FlexyPath + "/Images/ActionImages/plagerise.png")]
actionImg = []
actionImg2 = []
for i in actionImgL:
    i = pygame.transform.scale(i, (100, 100))
    actionImg.append(i)
for i in actionImgL2:
    i = pygame.transform.scale(i, (100, 100))
    actionImg2.append(i)

playerSpriteL = [pygame.image.load(FlexyPath + "/Sprites/1.png"), pygame.image.load(FlexyPath + "/Sprites/2.png"), pygame.image.load(FlexyPath + "/Sprites/3.png"), pygame.image.load(FlexyPath + "/Sprites/4.png"), pygame.image.load(FlexyPath + "/Sprites/5.png"), pygame.image.load(FlexyPath + "/Sprites/6.png"), pygame.image.load(FlexyPath + "/Sprites/7.png"), pygame.image.load(FlexyPath + "/Sprites/8.png"), pygame.image.load(FlexyPath + "/Sprites/9.png"), pygame.image.load(FlexyPath + "/Sprites/10.png")]
playerSpriteR = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/1.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/2.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/3.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/4.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/5.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/6.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/7.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/8.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/9.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/10.png"), True, False)]
bulletSprite = []
zombieSprite = pygame.image.load(FlexyPath + "/Sprites/Zombie.png")
steveSprite = pygame.image.load(FlexyPath + "/Sprites/SteveJobs.png")
pygame.mixer.music.load(FlexyPath +'/gameSong.wav')
pygame.mixer.music.play(-1)

kd = False
bg = pygame.image.load(FlexyPath + "/Images/wallpaper.png")
bg = pygame.transform.scale(bg, (1920, 1080))
lastFacing = "right"
f=open(FlexyPath + "/data.txt", "r")
contents = f.read()
f.close()
contents = contents.split()
level = int(contents[0])
ethicsScore = int(contents[1])
bulletColl = False

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


    def draw(self, window, direction):
        self.direction = direction
        global lastFacing
        if self.changeSprite > 48:
            self.changeSprite = -1
        self.changeSprite += 1
        

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

def actionQuestions():
    global ethicsScore
    global level
    global kd
    global bulletColl
    actionImgHit = [100, 100, 100, 100]
    actionImgHit2 = [1500, 100, 100, 100]
    try:
        window.blit(actionImg[level - 1], (100,100))
        window.blit(actionImg2[level - 1], (1500,100))
    except:
        print("GameOver")
    if person.hitbox[0] + person.hitbox[2] > actionImgHit[0] and person.hitbox[0] < actionImgHit[0] + actionImgHit[2]:   
        if person.hitbox[1] + person.hitbox[3] > actionImgHit[1] and person.hitbox[1] < actionImgHit[1] + actionImgHit[3]:
            ethicsScore += 10
            level += 1
            kd = False
            bulletColl = False
            person.x = 100
            person.y = 810
            person.jumpTimer = person.jumpTime

            save()

    if person.hitbox[0] + person.hitbox[2] > actionImgHit2[0] and person.hitbox[0] < actionImgHit2[0] + actionImgHit2[2]:   
        if person.hitbox[1] + person.hitbox[3] > actionImgHit2[1] and person.hitbox[1] < actionImgHit2[1] + actionImgHit2[3]:
            ethicsScore -= 10
            level += 1
            kd = False
            bulletColl = False
            person.x = 100
            person.y = 810
            person.jumpTimer = person.jumpTime

            save()

def zombie(x,y):
    window.blit(zombieSprite, (x,y))

def speechF(text, text2,text3, text4, attach):
    if attach == True:
        speechCloud.x = person.x + 65
        speechCloud.y = person.y - 135
    else:
        speechCloud.x = steveNPC.x + 65
        speechCloud.y = steveNPC.y - 135
    speechCloud.draw(window)
    showText(text, 20, (speechCloud.x + 50, speechCloud.y + 15), black)
    showText(text2, 20, (speechCloud.x + 50, speechCloud.y + 30), black)
    showText(text3, 20, (speechCloud.x + 50, speechCloud.y + 45), black)
    showText(text4, 20, (speechCloud.x + 50, speechCloud.y + 60), black)
stopMove = ""
collide = False
def platforms(x,y,width,height):
    global collide
    pygame.draw.rect(window,brown,(x,y,width,height))
    pygame.draw.rect(window,green,(x,y,width,height / 3))
    hitbox = (x, y, width, height)
    if person.hitbox[0] + person.hitbox[2] > hitbox[0] and person.hitbox[0] < hitbox[0] + hitbox[2]:
        if person.hitbox[1] + person.height >= hitbox[1] and person.hitbox[1] + person.height < hitbox[1] + hitbox[3] / 2 and person.jump == False:
            person.y = hitbox[1] - person.height

        elif person.jump == False:
            if person.hitbox[1] + person.hitbox[3] - hitbox[1] > 10:
                if person.y != hitbox[1] - person.height:
                    person.y -= 20

        if person.hitbox[1] + person.hitbox[3] > hitbox[1] and person.hitbox[1] < hitbox[1] + hitbox[3]:
            person.jump = False
            person.jumpTimer = person.jumpTime
            
            collide = True

def save():
    global level
    global ethicsScore
    f = open(FlexyPath + '/data.txt','w')
    f.write(str(level)+ " " + str(ethicsScore))

def reDraw(facing):
    global kd
    global bulletColl

    window.blit(bg,(0,0))
    if bulletColl == False:
        zombie(600,620)

    platforms(1200,700,100,50)
    platforms(1500,400,100,50)
    platforms(600,700,100,50)
    platforms(200,400,100,50)
    platforms(0,950,1920,50)
    actionQuestions()
    showText("Ethics Score: " + str(ethicsScore), 50, (700, 100), black)
    if kd == True:
        if level == 1:
            speechF("Hello","","","",  True)
            speechF("You want to","watch a movie do","you pirate it or","rent on Apple TV?", False)
        elif level == 2:
            speechF("I don't like","the ads on","youtube","",  True)
            speechF("Use an ad","blocker or pay","for premium","", False)
        elif level == 3:
            speechF("I really like","the look of","the new game","cyberpunk 2077",  True)
            speechF("Would you like","to buy the","full version or","crack the game", False)
        elif level == 4:
            speechF("Dam I just","dropped and smashed","my new phone","",  True)
            speechF("Would you like","to steal your","mates screen or","buy a new one", False)
        elif level == 5:
            speechF("Hey I found","this cool usb","it has a bunch","of paid software",  True)
            speechF("Would you like","to hand in","the usb or","sell it on ebay", False)
        elif level == 6:
            speechF("I am angry","at someone for","bad mouthing me","",  True)
            speechF("Would you like","to ddos their","computer or","let it slide", False)
        elif level == 7:
            speechF("Someone dropped","their credit card","on the ground","",  True)
            speechF("Do you use","brute force attack","to find their","pin or return", False)
        elif level == 8:
            speechF("The neighbours","wifi makes it","to my house","",  True)
            speechF("Would you like","to connect to","their internet","", False)
        elif level == 9:
            speechF("The mcdonalds wifi","is completely","unprotected","",  True)
            speechF("Would you like","to perform a","man in the","middle attack", False)
        elif level == 10:
            speechF("Mr Shen has","given me an","assignment","",  True)
            speechF("Would you like","to copy and","the whole thing","", False)
    elif level > 10:
        showText("Game Over", 70, (700, 500), black)
        

        

    for b in bullets:
        if b.x < person.x + 600:
            b.draw(window)
    person.draw(window, facing)
    steveNPC.draw(window)
    pygame.display.flip()

    pygame.display.update()


person = player(100,810,100,130)
steveNPC = npc(1930,810,77, 143)
speechCloud = speech(100,100)

bullets = {}
inair = False
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
        if level > 10:
            level = 1
            ethicsScore = 0
        save()
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
        if collide == True:
            person.jump = True

    if person.jump == True and inair == False:
        if person.jumpTimer > -(person.jumpTime):
            person.jumpTimer -= 1.5
            person.y -= person.jumpTimer
        else:
            person.jump = False
    
    if keys[pygame.K_i]:
        bullets[bullet(person.x + person.width/2, person.y + person.height/2.8, 6, (0,0,0), 1)] = wasFacing

    if steveNPC.x > 1000:
        steveNPC.x -= 4

    if person.hitbox[0] + person.hitbox[2] > steveNPC.hitbox[0] and person.hitbox[0] < steveNPC.hitbox[0] + steveNPC.hitbox[2]:
        
        if person.hitbox[1] + person.hitbox[3] > steveNPC.hitbox[1] and person.hitbox[1] < steveNPC.hitbox[1] + steveNPC.hitbox[3]:
            if keys[pygame.K_o]:
                kd = True

    if person.hitbox[0] + person.hitbox[2] > 620 and person.hitbox[0] < 620 + 113:
        
        if person.hitbox[1] + person.hitbox[3] > 600 and person.hitbox[1] < 600 + 83 and bulletColl == False:
            person.x = 100
            person.y = 810
            person.jumpTimer = person.jumpTime
    
    for b in list(bullets):
        if 620 + 113 > b.x and 620 < b.x:   
            if 600 + 83 > b.y and 600 < b.y:
                bulletColl = True

    if collide == False and person.jump == False:
        if person.jumpTimer > 0:
            person.jumpTimer = 0


        if person.jumpTimer > -40:
            person.jumpTimer -= 1.5
        
        person.y -= person.jumpTimer
        
    else:
        collide = False
    reDraw(facing)

    if person.y > 1000:
        person.x = 100
        person.y = 810
        person.jumpTimer = person.jumpTime


    

pygame.quit()