import pygame
import pygame_ai as PAI
import ctypes
import random

sysWidth=ctypes.windll.user32.GetSystemMetrics(0)
sysHeight=ctypes.windll.user32.GetSystemMetrics(1)
startWidth=sysWidth/2
startHeight=sysHeight/2
sysChange=sysWidth/100
dragonDim=int(sysHeight/8)
reaperDim=int(2*dragonDim)
reaperAttackWidth=int(1.6*reaperDim)
reaperAttackHeight=int(1.3*reaperDim)
fireHeight=int(dragonDim/3)
#boundaryE=int(1.05*sysWidth)
boundaryE=int(1*sysWidth)
#boundaryW=int(0.12*sysWidth)
boundaryW=int(0*sysWidth)
#boundaryN=int(0.12*sysHeight)
boundaryN=int(0*sysHeight)
boundaryS=1*sysHeight
APPROACH_RADIUS=0.138*sysHeight
class bossPlosion(PAI.gameobject.GameObject):
    def __init__(self):
        super().__init__()
        self.done = 0
        self.delayer = 0
        self.index = 0
        self.position = boss.position
        self.images=BPimages
        self.image = self.images[0]
        self.rect.x = self.position.x
        self.rect.y = self.position.y
    def explode(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        elif self.delayer<40:
            self.index=3
        elif self.delayer<50:
            self.index=4
        elif self.delayer<60:
            self.index=5
        elif self.delayer<70:
            self.index=6
        elif self.delayer<80:
            self.index=7
        else:
            self.done=1
        self.delayer+=2
class Explosion(PAI.gameobject.GameObject):
    def __init__(self,x,y):
        super().__init__()
        self.done=0
        self.delayer=0
        self.index=0
        self.position=pygame.math.Vector2(x,y)
        self.images=Eimages
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/16.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/17.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/18.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/19.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/20.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/21.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/22.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/23.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/24.gif"), (dragonDim, dragonDim)))
        # self.images.append(pygame.transform.scale(pygame.image.load("img/explosion/25.gif"), (dragonDim, dragonDim)))
        self.image = self.images[0]
        self.rect.x = self.position.x
        self.rect.y = self.position.y
    def explode(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        elif self.delayer<40:
            self.index=3
        elif self.delayer<50:
            self.index=4
        elif self.delayer<60:
            self.index=5
        elif self.delayer<70:
            self.index=6
        elif self.delayer<80:
            self.index=7
        elif self.delayer<90:
            self.index=8
        elif self.delayer<100:
            self.index=9
        elif self.delayer<110:
            self.index=10
        elif self.delayer<120:
            self.index=11
        elif self.delayer<130:
            self.index=12
        elif self.delayer<140:
            self.index=13
        elif self.delayer < 150:
            self.index = 14
        # elif self.delayer < 160:
        #     self.index = 15
        # elif self.delayer < 170:
        #     self.index = 16
        # elif self.delayer < 180:
        #     self.index = 17
        # elif self.delayer < 190:
        #     self.index = 18
        # elif self.delayer < 200:
        #     self.index = 19
        # elif self.delayer < 210:
        #     self.index = 20
        # elif self.delayer < 220:
        #     self.index = 21
        # elif self.delayer < 230:
        #     self.index = 22
        # elif self.delayer < 240:
        #     self.index = 23
        # elif self.delayer < 250:
        #     self.index = 24
        else:
            self.done=1
        self.delayer+=5


class Orb(PAI.gameobject.GameObject):
    def __init__(self,type):
        super().__init__()
        self.type=type
        self.consumed=0
        self.visible=1
        self.timeout=0
        self.index = 0
        self.delayer = 0
        self.images=[]
        if type==0:
            self.images=Oimages0
        elif type==1:
            self.images=Oimages1
        elif type==2:
            self.images=Oimages2
        self.position = pygame.math.Vector2(random.randint(boundaryW, int(boundaryE-0.4*dragonDim)), random.randint(boundaryN, int(boundaryS-0.4*dragonDim)))
        while myDragon.position.x + 2 * dragonDim > self.position.x and myDragon.position.x < self.position.x + 2 * dragonDim and myDragon.position.y + 2 * dragonDim > self.position.y and myDragon.position.y < self.position.y + 2 * dragonDim:
            self.position = pygame.math.Vector2(random.randint(boundaryW, int(boundaryE-0.4*dragonDim)),random.randint(boundaryN, int(boundaryS-0.4*dragonDim)))
        self.image = self.images
        self.rect.x = self.position.x
        self.rect.y = self.position.y
    def spin(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        elif self.delayer<40:
            self.index=3
        else:
            self.delayer=0
        self.delayer+=4

class Reaper(PAI.gameobject.GameObject):
    def __init__(self):
        super().__init__()
        self.position=pygame.math.Vector2(0.4*boundaryE+boundaryW,boundaryN+0.5*dragonDim)
        self.initialPos=self.position
        self.acc=pygame.math.Vector2(0,0)
        self.velocity=pygame.math.Vector2(0,0)
        self.life=50
        self.triggered=0
        self.defeated=0
        self.images=[]
        self.images.append(imagesI)
        self.images.append(imagesA)
        self.mode=0
        self.index = 0
        self.delayer = 0
        self.attackTimer=0
        self.image = self.images[0][0]
        self.rect.x = self.position.x
        self.rect.y = self.position.y
    def adjustPos(self):
        global BOSS_SPEED, BOSS_ATTACK
        if not self.mode:
            if self.position==self.initialPos:
                self.velocity=pygame.math.Vector2(0,0)
                self.acc=pygame.math.Vector2(0,0)
            else:
                self.acc = self.seekWithApproach(self.initialPos)
        else:
            self.acc = self.seek(myDragon.position)
        self.velocity += self.acc
        if self.velocity.length() > BOSS_ATTACK:
            self.velocity.scale_to_length(BOSS_ATTACK)
        self.position += self.velocity
        if self.position.x > boundaryE:
            self.position.x = boundaryW
        if self.position.x < boundaryW:
            self.position.x = boundaryE
        if self.position.y > boundaryS:
            self.position.y = boundaryN
        if self.position.y < boundaryN:
            self.position.y = boundaryS
        self.rect.x = self.position.x
        self.rect.y = self.position.y
    def flap(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        elif self.delayer<40:
            self.index=3
        elif self.delayer<50:
            self.index=4
        elif self.delayer<60:
            self.index=5
        elif self.delayer<70:
            self.index=6
        elif self.delayer<80:
            self.index=7
        elif self.delayer<90:
            self.index=8
        elif self.delayer<100:
            self.index=9
        elif self.delayer<110:
            self.index=10
        elif self.delayer<120:
            self.index=11
        elif self.delayer<130:
            self.index=12
        elif self.delayer<140:
            self.index=13
        else:
            self.delayer=0
            self.mode=0
        self.delayer+=10

    def seek(self, target):
        global BOSS_ATTACK, BOSS_SPEED
        desired = (target - self.position).normalize() * BOSS_ATTACK
        steering = (desired - self.velocity)
        if steering.length() > BOSS_SPEED:
            steering.scale_to_length(BOSS_SPEED)
        return steering
    def seekWithApproach(self,target):
        desired= (target-self.position)
        dist=desired.length()
        desired.normalize_ip()
        if dist<APPROACH_RADIUS:
            desired*=dist/APPROACH_RADIUS*BOSS_ATTACK
        else:
            desired*=BOSS_ATTACK
        steering=(desired-self.velocity)
        if steering.length()>BOSS_SPEED:
            steering.scale_to_length(BOSS_SPEED)
        return steering
    def update(self):
        if self.attackTimer<400:
            self.mode=0
        elif self.attackTimer<700:
            self.mode=1
        else:
            self.attackTimer=0
        self.attackTimer+=1
        '''if myDragon.position.x>self.position.x-dragonDim and myDragon.position.x<self.position.x+reaperDim+dragonDim and myDragon.position.y<self.position.y+reaperDim:
            self.mode=1
            self.position.x=0.4*boundaryE+boundaryW-reaperAttackWidth'''



class dFire(PAI.gameobject.GameObject):
    def __init__(self,d,x,y):
        super().__init__()
        self.direc=d
        self.Destroyed=0
        if self.direc==0:
            self.images=FIR
            self.x=x+dragonDim
            self.y=y+0.25*dragonDim
        elif self.direc==1:
            self.images=FIL
            self.x=x-dragonDim
            self.y=y+0.25*dragonDim
        elif self.direc==2:
            self.images=FIU
            self.x=x+0.25*dragonDim
            self.y=y-dragonDim
        else:
            self.images=FID
            self.x=x+0.25*dragonDim
            self.y=y+dragonDim
        self.image = self.images
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
def fireDragonShot():
    myDragonShots.append(dFire(myDragon.orien,lead_x,lead_y))
def fireSuperShot():
    for i in range(20):
        if i%2==0:
            myDragonShots.append(dFire(0,boundaryW-dragonDim,boundaryN+(i/20)*boundaryS))
        else:
            myDragonShots.append(dFire(1,boundaryE,boundaryN+(i/20)*boundaryS))
def moveDragonShots():
    for shot in myDragonShots:
        shot.rect.topleft=(shot.x,shot.y)
        if shot.direc==0:
            shot.x+=30
        elif shot.direc==1:
            shot.x-=30
        elif shot.direc==2:
            shot.y-=30
        else:
            shot.y+=30
class Dragon(PAI.gameobject.GameObject):
    def __init__(self):
        super().__init__()
        self.life=3
        self.shielded=0
        self.images=[]
        self.orien=0
        self.dmgBoost=0
        self.visible=1
        self.dmgBoostCount=0
        imagesR=[]
        imagesR.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonright1.png"),(dragonDim,dragonDim)))
        imagesR.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonright2.png"),(dragonDim,dragonDim)))
        imagesR.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonright3.png"),(dragonDim,dragonDim)))
        self.images.append(imagesR)
        imagesL = []
        imagesL.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonleft1.png"), (dragonDim, dragonDim)))
        imagesL.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonleft2.png"), (dragonDim, dragonDim)))
        imagesL.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonleft3.png"), (dragonDim, dragonDim)))
        self.images.append(imagesL)
        imagesU = []
        imagesU.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonup1.png"), (dragonDim, dragonDim)))
        imagesU.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonup2.png"), (dragonDim, dragonDim)))
        imagesU.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragonup3.png"), (dragonDim, dragonDim)))
        self.images.append(imagesU)
        imagesD = []
        imagesD.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragondown1.png"), (dragonDim, dragonDim)))
        imagesD.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragondown2.png"), (dragonDim, dragonDim)))
        imagesD.append(pygame.transform.scale(pygame.image.load("img/dragon_std/dragondown3.png"), (dragonDim, dragonDim)))
        self.images.append(imagesD)
        self.index=0
        self.delayer=0

    def flap(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        else:
            self.delayer=0
        self.delayer+=2
class Eye(PAI.gameobject.GameObject):
    def __init__(self):
        super().__init__()
        self.Destroyed=0
        self.seekingDragon=SEEKING
        self.images = []
        self.position=pygame.math.Vector2(random.randint(boundaryW,boundaryE),random.randint(boundaryN,boundaryS))
        while myDragon.position.x + 2 * dragonDim > self.position.x and myDragon.position.x < self.position.x + 2 * dragonDim and myDragon.position.y + 2 * dragonDim > self.position.y and myDragon.position.y < self.position.y + 2 * dragonDim :
            self.position = pygame.math.Vector2(random.randint(boundaryW, boundaryE), random.randint(boundaryN, boundaryS))
        self.wanderTarget=pygame.math.Vector2(random.randint(boundaryW,boundaryE),random.randint(boundaryN,boundaryS))
        if self.wanderTarget.x>self.position.x:
            self.orien=0
        else:
            self.orien=1
        self.lastWanderTarget=0
        #self.position=(500,500)
        self.velocity=pygame.math.Vector2(5,0).rotate(random.uniform(0,360))
        self.acc=(0,0)
        self.images.append(EyeimagesR)
        self.images.append(EyeimagesL)
        self.index = 0
        self.delayer = 0
        self.image = self.images[0][0]
        self.rect.x=self.position.x
        self.rect.y=self.position.y

    def update(self):
        global SEEK_SPEED,SEEK_ATTACK
        if self.seekingDragon:
            self.acc=self.seek(myDragon.position)
        else:
            self.acc=self.wander()
        self.velocity+=self.acc
        #self.followDragon()
        if self.velocity.length()>SEEK_ATTACK:
            self.velocity.scale_to_length(SEEK_ATTACK)
        self.position+=self.velocity
        if self.position.x>boundaryE:
            self.position.x=boundaryW
        if self.position.x<boundaryW:
            self.position.x=boundaryE
        if self.position.y>boundaryS:
            self.position.y=boundaryN
        if self.position.y<boundaryN:
            self.position.y=boundaryS
        self.rect.x=self.position.x
        self.rect.y=self.position.y
    def followDragon(self):
        dpos=myDragon.position
        self.acc=(dpos-self.position).normalize() *0.5
    def seek(self,target):
        global SEEK_ATTACK,SEEK_SPEED
        if (target-self.position).length()==0:
            target+=(target.x+1,target.y)
        desired= (target-self.position).normalize() * SEEK_ATTACK
        steering=(desired-self.velocity)
        if steering.length()>SEEK_SPEED:
            steering.scale_to_length(SEEK_SPEED)
        if target.x > self.position.x:
            self.orien = 0
        else:
            self.orien = 1
        return steering
    def seekWithApproach(self,target):
        desired= (target-self.position)
        dist=desired.length()
        desired.normalize_ip()
        if dist<APPROACH_RADIUS:
            desired*=dist/APPROACH_RADIUS*5
        else:
            desired*=5
        steering=(desired-self.velocity)
        if steering.length()>0.1:
            steering.scale_to_length(0.1)
        if target.x > self.position.x:
            self.orien = 0
        else:
            self.orien = 1
        return steering
    def wander(self):
        now=pygame.time.get_ticks()
        if now - self.lastWanderTarget>500:
            self.lastWanderTarget=now
            self.wanderTarget = pygame.math.Vector2(random.randint(boundaryW, boundaryE), random.randint(boundaryN, boundaryS))
            if self.wanderTarget.x > self.position.x:
                self.orien = 0
            else:
                self.orien = 1
        return self.seekWithApproach(self.wanderTarget)
    def flap(self):
        if self.delayer<10:
            self.index=0
        elif self.delayer<20:
            self.index=1
        elif self.delayer<30:
            self.index=2
        else:
            self.delayer=0
        self.delayer+=1
def toggleSeeking():
    global SEEKING
    SEEKING=not SEEKING
    for e in enemies:
        e.seekingDragon = SEEKING
def shotEyeCollision(shot,eye):
    #if shot.rect.colliderect(eye.rect):
    global gameScore,DIFFICULTY
    if shot.direc==0 or shot.direc==1:
        if shot.x+dragonDim>eye.position.x and shot.x<eye.position.x+dragonDim and shot.y>eye.position.y and shot.y<eye.position.y+dragonDim:
            #shot.Destroyed=1
            eye.Destroyed=1
            exps.append(Explosion(eye.position.x,eye.position.y))
            gameScore += DIFFICULTY*100
    elif shot.direc==2 or shot.direc==3:
        if shot.x+fireHeight>eye.position.x and shot.x<eye.position.x+dragonDim and shot.y+dragonDim>eye.position.y and shot.y<eye.position.y:
            #shot.Destroyed=1
            eye.Destroyed=1
            exps.append(Explosion(eye.position.x,eye.position.y))
            gameScore+=DIFFICULTY*100
def shotBossCollision(shot):
    global gameScore
    if shot.Destroyed or not boss.triggered or boss.defeated:
        return
    if shot.direc == 0 or shot.direc == 1:
        if shot.x + dragonDim > boss.position.x and shot.x < boss.position.x + reaperDim and shot.y > boss.position.y and shot.y < boss.position.y +reaperDim:
            shot.Destroyed=1
            boss.life-=1
            gameScore += 1000
    elif shot.direc == 2 or shot.direc == 3:
        if shot.x + fireHeight > boss.position.x and shot.x < boss.position.x + reaperDim and shot.y + dragonDim > boss.position.y and shot.y < boss.position.y+reaperDim:
            shot.Destroyed=1
            boss.life-=1
            gameScore += 1000
def dragonEyeCollision():
    for eeye in enemies:
        if myDragon.position.x + 0.7 * dragonDim > eeye.position.x and myDragon.position.x < eeye.position.x + 0.7 * dragonDim and myDragon.position.y + 0.7 * dragonDim > eeye.position.y and myDragon.position.y < eeye.position.y + 0.7 * dragonDim and not eeye.Destroyed:
            if myDragon.shielded:
                eeye.Destroyed = 1
                exps.append(Explosion(eeye.position.x, eeye.position.y))
                return
            if myDragon.dmgBoost:
                return
            myDragon.dmgBoost=1
            eeye.Destroyed = 1
            exps.append(Explosion(eeye.position.x,eeye.position.y))
            if myDragon.life == 3:
                myDragon.life = 2
            elif myDragon.life == 2:
                myDragon.life = 1
            elif myDragon.life == 1:
                myDragon.life = 0
            elif myDragon.life>3:
                myDragon.life-=1
def dragonBossCollision():
        if myDragon.position.x +dragonDim > boss.position.x and myDragon.position.x < boss.position.x + reaperDim and myDragon.position.y + dragonDim > boss.position.y and myDragon.position.y < boss.position.y + reaperDim and not myDragon.shielded and not myDragon.dmgBoost:
            myDragon.dmgBoost=1
            if myDragon.life == 3:
                myDragon.life = 2
            elif myDragon.life == 2:
                myDragon.life = 1
            elif myDragon.life == 1:
                myDragon.life = 0
            elif myDragon.life>3:
                myDragon.life-=1
def dragonOrbCollision():
    global shieldcounter
    for o in orbs:
        if myDragon.position.x+dragonDim>o.position.x and o.position.x>myDragon.position.x and o.position.y>myDragon.position.y and o.position.y<myDragon.position.y+dragonDim and not o.consumed:
            o.consumed=1
            if o.type==0:
                print("SHIELD")
                if(myDragon.shielded):
                    shieldcounter=0
                else:
                    myDragon.shielded=1
            elif o.type==1:
                myDragon.life+=1
            elif o.type==2:
                fireSuperShot()
def removeBeyondBounds():
    for shot in myDragonShots:
        if shot.x>1.1*boundaryE or shot.x<0 or shot.y>1.1*boundaryS or shot.y<0:
            shot.Destroyed=1
def generateEnemy():
    enemies.append(Eye())

def generateOrb():
    orbs.append(Orb(random.randint(0,2)))
def updateScore():
    global gameScore
    print(str(gameScore))
def triggerBoss():
    boss.triggered=1
    toggleSeeking()
def timeOutOrbs():
    for o in orbs:
        if not o.consumed:
            if o.timeout<200:
                o.timeout+=1
            elif o.timeout<300:
                if o.timeout%2==0:
                    o.visible=1
                else:
                    o.visible=0
                o.timeout += 1
            else:
                o.consumed=1
def DamageBoostCheck():
    if myDragon.dmgBoost:
        if myDragon.dmgBoostCount<120:
            myDragon.dmgBoostCount+=1
            if myDragon.dmgBoostCount%2==0:
                myDragon.visible=1
            else:
                myDragon.visible=0
        else:
            myDragon.visible=1
            myDragon.dmgBoost=0
            myDragon.dmgBoostCount=0
def endgame():
    bp.explode()
    for e in enemies:
        if not e.Destroyed:
            e.Destroyed=1
            exps.append(Explosion(e.position.x,e.position.y))
pygame.init()
global gameScore
global SEEKING
global DIFFICULTY,SEEK_SPEED,SEEK_ATTACK,BOSS_ATTACK,BOSS_SPEED,shieldcounter
gameScore=0
SEEKING=0
DIFFICULTY=1
SEEK_SPEED=0.1
SEEK_ATTACK=5
BOSS_ATTACK=30
BOSS_SPEED=0.5
dimensions=sysWidth,sysHeight
white=(255,255,255)
CURRECT_SPAWN_DELAY=120
gameDisplay =pygame.display.set_mode((sysWidth,sysHeight),pygame.FULLSCREEN)
pygame.display.set_caption("Draconic_Dystopia_v1.0")
font=pygame.font.Font('font/ringbearer.ttf',24)
fontLarge=pygame.font.Font('font/ringbearer.ttf',32)
fontStart=pygame.font.Font('font/ringbearer.ttf',42)
#pygame.display.update()
#LOADING IMAGES

BPimages = []
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/1.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/2.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/3.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/4.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/5.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/6.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/7.gif"), (reaperAttackWidth, reaperAttackHeight)))
BPimages.append(pygame.transform.scale(pygame.image.load("img/explosion/boss/8.gif"), (reaperAttackWidth, reaperAttackHeight)))

Eimages=[]
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/1.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/2.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/3.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/4.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/5.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/6.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/7.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/8.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/9.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/10.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/11.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/12.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/13.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/14.gif"), (dragonDim, dragonDim)))
Eimages.append(pygame.transform.scale(pygame.image.load("img/explosion/15.gif"), (dragonDim, dragonDim)))
Oimages0=[]
Oimages0.append(pygame.transform.scale(pygame.image.load("img/orb/green/1.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages0.append(pygame.transform.scale(pygame.image.load("img/orb/green/2.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages0.append(pygame.transform.scale(pygame.image.load("img/orb/green/3.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages0.append(pygame.transform.scale(pygame.image.load("img/orb/green/4.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages1=[]
Oimages1.append(pygame.transform.scale(pygame.image.load("img/orb/red/1.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages1.append(pygame.transform.scale(pygame.image.load("img/orb/red/2.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages1.append(pygame.transform.scale(pygame.image.load("img/orb/red/3.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages1.append(pygame.transform.scale(pygame.image.load("img/orb/red/4.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages2=[]
Oimages2.append(pygame.transform.scale(pygame.image.load("img/orb/fire/1.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages2.append(pygame.transform.scale(pygame.image.load("img/orb/fire/2.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages2.append(pygame.transform.scale(pygame.image.load("img/orb/fire/3.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))
Oimages2.append(pygame.transform.scale(pygame.image.load("img/orb/fire/4.png"),(int(0.4 * dragonDim), int(0.4 * dragonDim))))


imagesI=[]
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/1.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/2.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/3.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/4.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/5.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/6.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/7.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/8.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/9.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/10.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/11.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/12.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/13.gif"), (reaperDim, reaperDim)))
imagesI.append(pygame.transform.scale(pygame.image.load("img/boss/idle/14.gif"), (reaperDim, reaperDim)))

imagesA = []
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/1.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/2.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/3.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/4.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/5.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/6.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/7.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/8.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/9.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/10.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/11.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/12.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/13.gif"), (reaperAttackWidth, reaperAttackHeight)))
imagesA.append(pygame.transform.scale(pygame.image.load("img/boss/attack/14.gif"), (reaperAttackWidth, reaperAttackHeight)))

FIR=pygame.transform.scale(pygame.image.load("img/projectile/fireRight.png"),(dragonDim,fireHeight))
FIL=pygame.transform.scale(pygame.image.load("img/projectile/fireLeft.png"), (dragonDim, fireHeight))
FIU=pygame.transform.scale(pygame.image.load("img/projectile/fireUp.png"), (fireHeight,dragonDim))
FID=pygame.transform.scale(pygame.image.load("img/projectile/fireDown.png"), (fireHeight,dragonDim))

EyeimagesR = []
EyeimagesR.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeright1.png"), (dragonDim, dragonDim)))
EyeimagesR.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeright2.png"), (dragonDim, dragonDim)))
EyeimagesR.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeright3.png"), (dragonDim, dragonDim)))
EyeimagesL = []
EyeimagesL.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeleft1.png"), (dragonDim, dragonDim)))
EyeimagesL.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeleft2.png"), (dragonDim, dragonDim)))
EyeimagesL.append(pygame.transform.scale(pygame.image.load("img/eye_std/eyeleft3.png"), (dragonDim, dragonDim)))

#LOADING IMAGES
#START SCREEN
startScreen=1
startText=fontStart.render("Draconic Dystopia",True,white,None)
startTextRect=startText.get_rect()
startTextRect.center=((boundaryE-boundaryW)/2+boundaryW,boundaryS/2+boundaryN)
startSubText=fontLarge.render("Press any key to start",True,white,None)
startSubTextRect=startSubText.get_rect()
startSubTextRect.center=((boundaryE-boundaryW)/2+boundaryW,(boundaryS+dragonDim)/2+boundaryN)
#START SCREEN
#PAUSE SCREEN
pauseText=fontStart.render("PAUSED",True,white,None)
pauseTextRect=pauseText.get_rect()
pauseTextRect.center=(boundaryE/2+boundaryW/2,boundaryS/2+boundaryN)
pauseSubText=fontLarge.render("Press ESC to exit, or any other key to continue",True,white,None)
pauseSubTextRect=pauseSubText.get_rect()
pauseSubTextRect.center=(boundaryE/2+boundaryW/2,(boundaryS+dragonDim)/2+boundaryN)
#PAUSE SCREEN
#ENDGAME SCREEN
gameOverText=fontStart.render("GAME OVER",True,white,None)
gameOverTextRect=gameOverText.get_rect()
gameOverTextRect.center=(boundaryE/2+boundaryW/2,boundaryS/2+boundaryN)
gameOverSubText=fontLarge.render("You scored:"+str(gameScore)+"\nPress ESC to exit, or any other key to try again",True,white,None)
gameOverSubTextRect=gameOverSubText.get_rect()
gameOverSubTextRect.center=(boundaryE/2+boundaryW/2,(boundaryS+dragonDim)/2+boundaryN)

endGameText=fontStart.render("CONGRATULATIONS",True,white,None)
endGameTextRect=endGameText.get_rect()
endGameTextRect.center=(boundaryE/2+boundaryW/2,boundaryS/2+boundaryN)
endGameSubText=fontLarge.render("You scored:"+str(gameScore)+"\nPress ESC to exit, or any other key to play again",True,white,None)
endGameSubTextRect=endGameSubText.get_rect()
endGameSubTextRect.center=(boundaryE/2+boundaryW/2,(boundaryS+dragonDim)/2+boundaryN)
#ENDGAME SCREEN
myDragon = Dragon()
myDragonShots=[]
boss=Reaper()
bp=bossPlosion()
enemies=[]
orbs=[]
exps=[]
enemies.append(Eye())
bg=pygame.transform.scale(pygame.image.load("img/bg/night1.gif"),(sysWidth,sysHeight))
shield=pygame.transform.scale(pygame.image.load("img/shield/red.png"),(dragonDim,dragonDim))
heart=pygame.transform.scale(pygame.image.load("img/heart/heart.png"),(int(0.3*dragonDim),int(0.3*dragonDim)))
text=font.render(str(gameScore),True,white,None)
textLvl=fontLarge.render("Level 1",True,white,None)
healthtext=font.render(str(myDragon.life),True,white,None)
textRect=text.get_rect()
textRect.center =(boundaryW+dragonDim/2,boundaryN+dragonDim/2)
textRectLvl=textLvl.get_rect()
textRectLvl.center =((boundaryE-boundaryW)/2+boundaryW,boundaryN+dragonDim/2)
HtextRect=healthtext.get_rect()
HtextRect.center =(int(0.9 * boundaryE), int(boundaryN + dragonDim / 1.5))
gameExit=False
gameOver=False
lead_x=startWidth
lead_y=startHeight
lead_x_change=0
enemyDelay=0
orbDelay=0
shieldcounter=0
paused=0
lead_y_change=0
pygame.mouse.set_visible(False)
clock=pygame.time.Clock()
while not gameExit:
    while not gameOver:
        if not paused:
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    #print("Quittin")
                    gameOver=True
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if startScreen and (event.key==pygame.K_ESCAPE or event.key==pygame.K_TAB or event.key==308):
                        dontPause=1
                    else:
                        dontPause=0
                    startScreen=0
                    if event.key ==pygame.K_ESCAPE or event.key==pygame.K_TAB or event.key==308:
                        if not dontPause:
                            paused=1
                    if event.key == pygame.K_LEFT:
                        lead_x_change=-1*sysChange
                        myDragon.orien=1
                    if event.key == pygame.K_RIGHT:
                        lead_x_change=sysChange
                        myDragon.orien=0
                    if event.key == pygame.K_UP:
                        lead_y_change=-1*sysChange
                        myDragon.orien=2
                    if event.key == pygame.K_DOWN:
                        lead_y_change=sysChange
                        myDragon.orien=3
                    if event.key == pygame.K_SPACE:
                        fireDragonShot()
                    if event.key == pygame.K_F2:
                        print("SEEKING TOGGLED MANUALLY")
                        toggleSeeking()
                    if event.key == pygame.K_F1:
                        print("GOD MODE ACTIVATED")
                        myDragon.life=10000
                    if event.key == pygame.K_F3:
                        print("BOSS MODE TRIGGERED MANUALLY")
                        textLvl = font.render("DEVH4XX", True, white, None)
                        gameScore=696969
                        triggerBoss()
                    if event.key == pygame.K_F4:
                        fireSuperShot()
                if event.type==pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        lead_x_change=0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_y_change=-0
        if startScreen:
            gameDisplay.blit(bg,(boundaryW,boundaryN))
            gameDisplay.blit(startText,startTextRect)
            gameDisplay.blit(startSubText,startSubTextRect)
        elif paused:
            #gameDisplay.blit()
            gameDisplay.blit(pauseText,pauseTextRect)
            gameDisplay.blit(pauseSubText,pauseSubTextRect)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
                    gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameOver=True
                        gameExit = True
                    else:
                        if event.key==pygame.K_TAB or event.key==308:
                            paused=1
                        else:
                            paused=0
        else:
            if lead_x>boundaryE-dragonDim+boundaryW:
            #if lead_x>boundaryE:
                lead_x-=sysChange
            if lead_y>boundaryS-dragonDim+boundaryN:
            #if lead_y>boundaryS
                lead_y-=sysChange
            if lead_x<boundaryW:
                lead_x+=sysChange
            if lead_y<boundaryN:
                lead_y+=sysChange
            if lead_y_change!=0 and lead_x_change !=0:
                if lead_x_change>0:
                    myDragon.orien=0
                else:
                    myDragon.orien=1
                lead_x+=lead_x_change/2
                lead_y+=lead_y_change/2
            else:
                lead_x+=lead_x_change
                lead_y+=lead_y_change



            gameDisplay.blit(bg,(boundaryW,boundaryN))
            myDragon.position=pygame.math.Vector2(lead_x,lead_y)
            for eyee in enemies:
                if not eyee.Destroyed:
                    gameDisplay.blit(eyee.images[eyee.orien][eyee.index],eyee.position)
                    eyee.flap()
                    eyee.update()
            for o in orbs:
                if not o.consumed and o.visible:
                    gameDisplay.blit(o.images[o.index],o.position)
                    o.spin()
            for e in exps:
                if not e.done:
                    gameDisplay.blit(e.images[e.index],e.position)
                    e.explode()
            #pygame.draw.rect(gameDisplay,(0,0,0),[lead_x,lead_y,sysChange,sysChange])
            # TESTING---------------------
            if boss.triggered and not boss.defeated:
                gameDisplay.blit(boss.images[boss.mode][boss.index], boss.position)
                boss.flap()
                boss.update()
                boss.adjustPos()
                dragonBossCollision()
                #pygame.draw.rect(gameDisplay,(255,0,0),(boundaryW+1.5*dragonDim,boundaryS+0.4*dragonDim,(boss.life/50)*(sysWidth-(3*dragonDim)),dragonDim/2))
                pygame.draw.rect(gameDisplay,(255,0,0),(boundaryW+1.5*dragonDim,boundaryS-0.6*dragonDim,(boss.life/50)*(sysWidth-(3*dragonDim)),dragonDim/2))
                #pygame.draw.rect(gameDisplay,(0,0,0),((boundaryW+1.5*dragonDim)+(boss.life/50)*(sysWidth-(3*dragonDim)),boundaryS+0.4*dragonDim,(sysWidth-(3*dragonDim))-(boss.life/50)*(sysWidth-(3*dragonDim)),dragonDim/2))
                pygame.draw.rect(gameDisplay,(0,0,0),((boundaryW+1.5*dragonDim)+(boss.life/50)*(sysWidth-(3*dragonDim)),boundaryS-0.6*dragonDim,(sysWidth-(3*dragonDim))-(boss.life/50)*(sysWidth-(3*dragonDim)),dragonDim/2))
            # TESTING---------------------
            if myDragon.visible:
                gameDisplay.blit(myDragon.images[myDragon.orien][myDragon.index],[lead_x,lead_y])
            if myDragon.shielded:
                gameDisplay.blit(shield,[lead_x,lead_y])
            if myDragon.life>=1:
                gameDisplay.blit(heart,(int(0.85*(boundaryE-boundaryW)+boundaryW),boundaryN+dragonDim/2))
                if myDragon.life==2 or myDragon.life==3:
                    gameDisplay.blit(heart,(int(0.9 * (boundaryE-boundaryW)+boundaryW), boundaryN + dragonDim / 2))
                    if myDragon.life==3:
                        gameDisplay.blit(heart,(int(0.95 * (boundaryE-boundaryW)+boundaryW), boundaryN + dragonDim / 2))
                else:
                    if myDragon.life!=1:
                        healthtext = font.render(str(myDragon.life), True, white, None)
                        gameDisplay.blit(healthtext, HtextRect)
            #if myDragon.life>=3:
                #gameDisplay.blit(pygame.transform.scale(pygame.image.load("img/heart/heart.png"),(int(0.3*dragonDim),int(0.3*dragonDim))),(int(0.95*boundaryE),boundaryN+dragonDim/2))
            #if myDragon.life>=2:
                #gameDisplay.blit(pygame.transform.scale(pygame.image.load("img/heart/heart.png"),(int(0.3*dragonDim),int(0.3*dragonDim))),(int(0.9*boundaryE),boundaryN+dragonDim/2))
            #if myDragon.life>=1:
                #gameDisplay.blit(pygame.transform.scale(pygame.image.load("img/heart/heart.png"),(int(0.3*dragonDim),int(0.3*dragonDim))),(int(0.85*boundaryE),boundaryN+dragonDim/2))
            else:
                gameOver=True
            for eye in enemies:
                for sh in myDragonShots:
                    if not eye.Destroyed:
                        shotEyeCollision(sh,eye)
            for shot in myDragonShots:
                if not shot.Destroyed:
                    shotBossCollision(shot)
                    gameDisplay.blit(shot.images,[shot.x,shot.y])
            myDragon.flap()
            moveDragonShots()
            dragonEyeCollision()
            dragonOrbCollision()
            if boss.defeated and not bp.done:
                bp.position=boss.position
                gameDisplay.blit(bp.images[bp.index],bp.position)
                endgame()
            '''for eeye in enemies:
                if myDragon.position.x+0.7*dragonDim>eeye.position.x and myDragon.position.x<eeye.position.x+0.7*dragonDim and myDragon.position.y+0.7*dragonDim>eeye.position.y and myDragon.position.y<eeye.position.y+0.7*dragonDim and not eeye.Destroyed:
                    eeye.Destroyed=1
                    if myDragon.life==3 and not Waiting:
                        myDragon.life=2
                        Waiting=1
                    elif myDragon.life==2 and not Waiting:
                        myDragon.life=1
                        Waiting=1
                    elif myDragon.life==1 and not Waiting:
                        myDragon.life==0
                        Waiting=1
                    else:
                        Waiting+=1
            if Waiting>0 and Waiting<=60:
                Waiting+=1
            else:
                Waiting=0'''
            if enemyDelay<CURRECT_SPAWN_DELAY:
                enemyDelay+=1
            else:
                if not boss.defeated:
                    generateEnemy()
                enemyDelay=0
            if orbDelay<400:
                orbDelay+=1
            else:
                if not boss.defeated:
                    generateOrb()
                orbDelay=0
            if myDragon.shielded:
                if shieldcounter<200:
                    shieldcounter+=1
                else:
                    myDragon.shielded=0
                    shieldcounter=0
            removeBeyondBounds()
            DamageBoostCheck()
            timeOutOrbs()
            if boss.life<1:
                print("BOSS KILLED!")
                boss.defeated=1
                #gameExit=True
            if gameScore>=1000 and gameScore<3000:
                textLvl = font.render("Level 2", True, white, None)
                DIFFICULTY=2
                SEEK_ATTACK=10
                SEEK_SPEED=0.15
                CURRECT_SPAWN_DELAY=90
            elif gameScore>=3000 and gameScore<6000:
                textLvl = font.render("Level 3", True, white, None)
                DIFFICULTY=3
                SEEK_ATTACK=15
                SEEK_SPEED=0.2
                CURRECT_SPAWN_DELAY=60
            elif gameScore>=6000 and gameScore<10000:
                textLvl = font.render("Level 4", True, white, None)
                DIFFICULTY=4
                SEEK_ATTACK=20
                SEEK_SPEED=0.25
                CURRECT_SPAWN_DELAY=30
            elif gameScore>=10000 and not boss.triggered:
                textLvl = font.render("Boss Fight", True, white, None)
                DIFFICULTY=5
                SEEK_ATTACK=10
                SEEK_SPEED=0.15
                CURRECT_SPAWN_DELAY=90
                triggerBoss()
            if bp.done:
                gameOver=True
            #updateScore()
            text = font.render(str(gameScore), True, white, None)
            gameDisplay.blit(text,textRect)
            gameDisplay.blit(textLvl, textRectLvl)
            #pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            else:
                print(event.key)
                if event.key == pygame.K_KP_ENTER or event.key==13:
                    gameScore = 0
                    SEEKING = 0
                    DIFFICULTY = 1
                    SEEK_SPEED = 0.1
                    SEEK_ATTACK = 5
                    CURRECT_SPAWN_DELAY = 120
                    myDragon = Dragon()
                    myDragonShots = []
                    boss = Reaper()
                    bp = bossPlosion()
                    enemies = []
                    orbs = []
                    exps = []
                    enemies.append(Eye())
                    lead_x = startWidth
                    lead_y = startHeight
                    lead_x_change = 0
                    enemyDelay = 0
                    orbDelay = 0
                    shieldcounter = 0
                    paused = 0
                    lead_y_change = 0
                    textLvl = fontLarge.render("Level 1", True, white, None)
                    gameOver=False
    if gameExit:
        break
    if boss.defeated:
        gameDisplay.blit(bg, (boundaryW, boundaryN))
        endGameSubText = fontLarge.render("You scored:" + str(gameScore) + " - Press ESC to exit, or ENTER to play again", True, white, None)
        gameDisplay.blit(endGameText,endGameTextRect)
        gameDisplay.blit(endGameSubText,endGameSubTextRect)
    else:
        gameDisplay.blit(bg, (boundaryW, boundaryN))
        gameOverSubText = fontLarge.render("You scored:" + str(gameScore) + " - Press ESC to exit, or ENTER to try again", True, white, None)
        gameDisplay.blit(gameOverText,gameOverTextRect)
        gameDisplay.blit(gameOverSubText,gameOverSubTextRect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()