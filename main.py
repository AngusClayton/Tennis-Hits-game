from matplotlib.pyplot import title
import pygame
import os 
import objects
from specialFunctions import *
#setup
size = (960,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tennis Hits")
pygame.init()
#clock setup
clock = pygame.time.Clock()

gameFinished = False
#set background
bg = pygame.image.load(os.path.join("img","background.png"))

#menu object list:
menuObects = pygame.sprite.Group()

#start title screen sequence:
titleSequence = objects.titleScreen()
menuObects.add(titleSequence)
gameStarted = False #True when title/help sequence over.

#tennis ball (main ball) object (red/green Ball):
ballObjects = pygame.sprite.Group()
mainBall = objects.ballMain()
ballObjects.add(mainBall)

#player (racket) object:
playerObjects = pygame.sprite.Group()
player = objects.player()
playerObjects.add(player)

hitWhenNotReady = False #changes when player hits ball when not ready; and prevents more than 1 point from being lost.

while gameFinished == False: #main loop; change gameFinished when game is exited to True
    #main event loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameFinished = True
        if event.type == pygame.MOUSEBUTTONDOWN: #when key pressed:
            if event.button == 1 and not gameStarted: #left click:
                gameStarted = titleSequence.nextImage()
                print("TitleScreen.next")
            

    #game logic:

    #drawing code:
    screen.blit(bg, (0, 0)) #background
    menuObects.draw(screen)

    if gameStarted:
        ballObjects.draw(screen) #draw the main ball
        playerObjects.draw(screen) #draw the player racket.
        mainBall.move()#handles ball's movment vectors
        player.move()#handels players racket staying in position with mouse cursor.
        
        #check for collision between main ball and racket:
        collisions = pygame.sprite.spritecollide(player, ballObjects, False)
        if collisions:
            if mainBall in collisions:
                if mainBall.ready:
                    hitWhenNotReady = False
                    mainBall.impact()
                    mainBall.impactEnabled = False
                    mainBall.ready=False
                    player.points += 1
                else:
                    if not hitWhenNotReady and mainBall.vz > 0: #only takes 1 point; and only if ball heading towards player
                        hitWhenNotReady = True
                        player.points -= 1

        #check if  game over
        if mainBall.gameOver:
            gameFinished = "BALL_PAST_PLAYER"
        
        
        #display score:
        text = str(player.points)# + "pts"
        LargeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = objects.text_object(text, LargeText)
        TextRect.center = ((objects.screenWidth/2),50)
        screen.blit(TextSurf, TextRect)


        

        

            

    #update screen:
    pygame.display.flip()
    clock.tick(60) #60fps
    #print(player.points)
print(gameFinished,player.points)
pygame.quit()
