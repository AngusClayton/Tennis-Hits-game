import pygame
import os
import random

screenWidth = 960
screenHeight = 720

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','playerRacket.png'))
        self.rect = self.image.get_rect()
        self.points = 0
    def move(self):
        x, y = pygame.mouse.get_pos()
        self.rect.center = (x,y)
        




class titleScreen(pygame.sprite.Sprite):
    #start screen / help menu
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #load images:
        self.images = []
        self.images.append(pygame.image.load(os.path.join('img', 'help','1.png'))) #index 0
        self.images.append(pygame.image.load(os.path.join('img', 'help','2.png'))) #index 1
        self.images.append(pygame.image.load(os.path.join('img', 'help','3.png'))) #index 2
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def nextImage(self):
        currentImage = self.images.index(self.image)
        if currentImage != 2: #when index == 2 kill title screen
            self.image = self.images[currentImage+1]
            return False
        else:
            self.kill()
            return True
    
class deathBall(pygame.sprite.Sprite): #class for the 'grey' ball that end the game upon touch.
    def changeZ(self,zValue): #changes 'size' / distance away / z value of ball.
        zposx = int(zValue*self.originalX)
        zposy = int(zValue*self.originalY)
        #apply scaling to image
        self.image = pygame.transform.smoothscale(self.origionalImage,(zposx,zposy))
        #apply scaling to hitbox
        self.rect.width = zposx
        self.rect.height = zposy

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.origionalImage = pygame.image.load(os.path.join('img', 'deathBall.png'))
        self.image = self.origionalImage
        self.rect = self.image.get_rect()
         
        #set origional size for Z axis scaling effect.
        self.originalX = self.rect.width
        self.originalY = self.rect.height

        #set direction vectors [random x/y]
        self.vx = random.randint(-5,5)/10 #velocity X
        self.vy = random.randint(-5,5)/10 #velocity Y
        self.vz = 0.005

        #set starting position
        self.x = screenWidth/2 #position x
        self.y = screenHeight/2 #position y
        self.z = 0.1
        self.rect.center = (self.x,self.y) #start at centre of window.

        #set image to scale:
        self.changeZ(self.z)
    def move(self):
        #change x y z pos 
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        self.z = self.z + self.vz
        self.rect.center = (self.x,self.y)
        self.changeZ(self.z)

        #remove the death ball from the screen if z > 1
        if self.z > 1:
            self.kill()    

class bonusBall(pygame.sprite.Sprite): #class for the 'purple' ball that give bonus points upon touch.
    def changeZ(self,zValue): #changes 'size' / distance away / z value of ball.
        zposx = int(zValue*self.originalX)
        zposy = int(zValue*self.originalY)
        #apply scaling to image
        self.image = pygame.transform.smoothscale(self.origionalImage,(zposx,zposy))
        #apply scaling to hitbox
        self.rect.width = zposx
        self.rect.height = zposy

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.origionalImage = pygame.image.load(os.path.join('img', 'pointsBall.png'))
        self.image = self.origionalImage
        self.rect = self.image.get_rect()
         
        #set origional size for Z axis scaling effect.
        self.originalX = self.rect.width
        self.originalY = self.rect.height

        #set direction vectors [random x/y]
        self.vx = random.randint(-5,5)/10 #velocity X
        self.vy = random.randint(-5,5)/10 #velocity Y
        self.vz = 0.005

        #set starting position
        self.x = screenWidth/2 #position x
        self.y = screenHeight/2 #position y
        self.z = 0.1
        self.rect.center = (self.x,self.y) #start at centre of window.

        #set image to scale:
        self.changeZ(self.z)    
    

    def move(self):
        #change x y z pos 
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        self.z = self.z + self.vz
        self.rect.center = (self.x,self.y)
        self.changeZ(self.z)

        #remove the death ball from the screen if z > 1
        if self.z > 1:
            self.kill()    

        
class timeBall(pygame.sprite.Sprite): #class for the 'yellow' ball that SLOW the game upon touch.
    def changeZ(self,zValue): #changes 'size' / distance away / z value of ball.
        zposx = int(zValue*self.originalX)
        zposy = int(zValue*self.originalY)
        #apply scaling to image
        self.image = pygame.transform.smoothscale(self.origionalImage,(zposx,zposy))
        #apply scaling to hitbox
        self.rect.width = zposx
        self.rect.height = zposy

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.origionalImage = pygame.image.load(os.path.join('img', 'timeBall.png'))
        self.image = self.origionalImage
        self.rect = self.image.get_rect()
         
        #set origional size for Z axis scaling effect.
        self.originalX = self.rect.width
        self.originalY = self.rect.height

        #set direction vectors [random x/y]
        self.vx = random.randint(-5,5)/10 #velocity X
        self.vy = random.randint(-5,5)/10 #velocity Y
        self.vz = 0.005

        #set starting position
        self.x = screenWidth/2 #position x
        self.y = screenHeight/2 #position y
        self.z = 0.1
        self.rect.center = (self.x,self.y) #start at centre of window.

        #set image to scale:
        self.changeZ(self.z)    
    

    def move(self):
        #change x y z pos 
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        self.z = self.z + self.vz
        self.rect.center = (self.x,self.y)
        self.changeZ(self.z)

        #remove the death ball from the screen if z > 1
        if self.z > 1:
            self.kill()  



class ballMain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(os.path.join('img', 'notReadyBall.png'))) #index 0 not ready
        self.images.append(pygame.image.load(os.path.join('img', 'readyBall.png'))) #index 1 ready
        self.image = self.images[0]
        self.rect = self.image.get_rect()
         
        #set origional size for Z axis scaling effect.
        self.originalX = self.rect.width
        self.originalY = self.rect.height

        #set direction vectors
        self.vx = 1 #velocity X
        self.vy = .5 #velocity Y
        self.vz = 0.005
        self.x = screenWidth/2 #position x
        self.y = screenHeight/2 #position y
        self.z = 0.1
        self.rect.center = (self.x,self.y) #start at centre of window.
        #set ready state (if collision when ball not ready take a point)
        self.ready = False

        #Set game over (As if the ball moves too far in the Z axis (>1) the player has missed.)
        self.gameOver = False

        #set wait will z back flag; used to stop the racket from triggering the impact function repetadly; instead waits for ball to go back to z<0.5 before reenabling the impact function
        self.impactEnabled = True
    def changeZ(self,zValue): #changes 'size' / distance away / z value of ball.
        zposx = int(zValue*self.originalX)
        zposy = int(zValue*self.originalY)
        if self.ready: #needed as color of ball changes images which changes scaling.
            self.image = pygame.transform.smoothscale(self.images[1],(zposx,zposy))
        else:
            self.image = pygame.transform.smoothscale(self.images[0],(zposx,zposy))
        
        self.rect.width = zposx
        self.rect.height = zposy

        #determine if ready:
        if zValue > 0.7 and self.vz > 0:#don't want to make ball ready when on its way back.
            self.ready = True
        if zValue > 1:
            self.gameOver = True
            print("GAME OVER")

        if zValue < 0.1:
            self.bounce() #as has it the computer, bounce back.
        



    def move(self):
        #change x y pos but keep within boundaries by bouncing off edges
        border = 40
        if not (border < self.x < screenWidth -border):
           self.vx = -self.vx
            
        if not (border < self.y < screenHeight -border):
            self.vy = -self.vy

        self.y = self.y + self.vy
        self.x = self.x + self.vx
        
        #Z boundaries are kept between 0 and 1 within other functions; so just need to change z position according to velocity.
        self.z = self.z + self.vz
        self.rect.center = (self.x,self.y)
        self.changeZ(self.z)

    def bounce(self):
        debug = False #causes this function to print usefull varibles to console
        r =  30 # r/10 = max magnitude of x or y velocity
        #determine new velocity for x and y directions; 
        #must not make the ball go off the screen; so if ball on left bottom go to right top and vice versa.
        if debug: print(self.x,self.y)
        if self.x < screenWidth/2: #on left side of screen
            self.vx = random.randint(0,r)/10
            if debug: print("x+")
        else:
            if debug: print("x-")
            self.vx = random.randint(-r,0)/10


        if self.y > screenHeight/2: #on top side of screen
            if debug: print("y+")
            self.vy = random.randint(0,r)/10
        else:
            if debug: print("y-")
            self.vy = random.randint(-r,0)/10
        
        #calcualte Z velocity (previous * 1.05%)
        self.vy = random.randint(-r,r)/10
        self.vz = -self.vz*1.05 #reverse Z axis direction and increase speed   
    
    def impact(self):
        if self.vz >= 0:
            self.bounce()

# ======== TEXT OBJECT
def text_object(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()
