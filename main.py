#Angus Clayton 2021
#12SDD ATK3
#Tennis Hits game
#main program.

from matplotlib.pyplot import title #not sure why I added this, but don't want to remove incase it breakes anything
import pygame
import os 
import objects
import highscore
import random
#setup
size = (960,720)
screen = pygame.display.set_mode(size)

gameIcon = pygame.image.load(os.path.join("img","icon.png"))
pygame.display.set_icon(gameIcon)


pygame.display.set_caption("Tennis Hits")
pygame.init()
#clock setup
clock = pygame.time.Clock()

gameFinished = False
gameOverActive = True

#set background:
bg = pygame.image.load(os.path.join("img","background.png"))

#set backing music:
#Note: try except used; as on my windows system; (which i devloped on) the music would not play (I believe my python install has path errors) however my macOS laptop had no problem
#still wanted to have music; but didn't have time to fix my python installation on PC.
#tested macbook as off 15/6/2021
try:
    pygame.mixer.init()
    pygame.mixer.music.load('dioma.mp3') #Jnathyn - Dioma [NCS Release] #14/6/2021
    pygame.mixer.music.play(-1, 0.0)
except:
    print("ERROR: PYGAME MUSIC NOT INSTALLED CORRECTLY ON SYSTEM")
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

#specialty ball objects:
activeSpecialBalls = {"DEATH":0,"TIME":0,"BONUS":0}

hitWhenNotReady = False #changes when player hits ball when not ready; and prevents more than 1 point from being lost.

##prevV = 0 #FOR DATA ANALYSIS OF THE Z VELOCITY OF MAINBALL
NextSpawnTime = 9999999999 #The next time a ball spawns
while gameFinished == False: #main loop; change gameFinished when game is exited to True
    ##if mainBall.vz != prevV:#FOR DATA ANALYSIS OF THE Z VELOCITY OF MAINBALL
    ##    print(pygame.time.get_ticks(),mainBall.vz,NextSpawnTime)#FOR DATA ANALYSIS OF THE Z VELOCITY OF MAINBALL
    ##    prevV = mainBall.vz#FOR DATA ANALYSIS OF THE Z VELOCITY OF MAINBALL
    
    
    #=============== main event loop:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameFinished = True
            gameOverActive = False
        if event.type == pygame.MOUSEBUTTONDOWN: #when key pressed:
            if event.button == 1 and not gameStarted: #left click:
                gameStarted = titleSequence.nextImage()
                if gameStarted:
                    NextSpawnTime = 3000
                print("TitleScreen.next")

        if False: #Change to false when not debuging the specialty balls
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    deathBall = objects.deathBall()
                    activeSpecialBalls["DEATH"] = True
                    ballObjects.add(deathBall)
                if event.key == pygame.K_b:
                    bonusBall = objects.bonusBall()
                    activeSpecialBalls["BONUS"] = True
                    ballObjects.add(bonusBall)
                if event.key == pygame.K_t:
                    timeBall = objects.timeBall()
                    activeSpecialBalls["TIME"] = True
                    ballObjects.add(timeBall)
        
            

    

    #====== drawing code:
    screen.blit(bg, (0, 0)) #background
    menuObects.draw(screen)

    if gameStarted: # === code to run when game is started; and not on a start menu screen.
        ballObjects.draw(screen) #draw the main ball
        playerObjects.draw(screen) #draw the player racket.
        #======= movement of ball objects [handles physics]
        if activeSpecialBalls["DEATH"]:
            deathBall.move()
            if deathBall not in ballObjects:
                activeSpecialBalls["DEATH"] = False
        if activeSpecialBalls["BONUS"]:
            bonusBall.move()
            if bonusBall not in ballObjects:
                activeSpecialBalls["BONUS"] = False
        if activeSpecialBalls["TIME"]:
            timeBall.move()
            if timeBall not in ballObjects:
                activeSpecialBalls["TIME"] = False

        mainBall.move() #handles physics for main ball

        #====== movemnt of player object
        player.move() #handels players racket staying in position with mouse cursor.
        
        #====== Colision Detection
        #  check for collision between balls and racket:
        collisions = pygame.sprite.spritecollide(player, ballObjects, False)
        if collisions:
            if mainBall in collisions: #main ball collision handeler:
                if mainBall.ready: #ensure ball hit with correct timing; or take a point.
                    hitWhenNotReady = False
                    mainBall.impact()
                    mainBall.impactEnabled = False
                    mainBall.ready=False
                    player.points += 1
                else:
                    if not hitWhenNotReady and mainBall.vz > 0: #only takes 1 point; and only if ball heading towards player
                        hitWhenNotReady = True
                        player.points -= 1
            
            #now check active speciality ballObjects collisions
            #we require the activeSpecialBalls dictionary to stop 'undefined' errors when these balls are not currenty active/exist.
            #the code after the and statement will not run unless the first condition is true; therefore this prevents undefinded errors in the collision check.
            minZCollision = 0.2
            
            if activeSpecialBalls["DEATH"] and deathBall in collisions:
                if deathBall.z > minZCollision:
                    gameFinished = "Next time don't hit the grey ball. It instantly ends the game." #end game
                
            if activeSpecialBalls["BONUS"] and bonusBall in collisions:
                if bonusBall.z > minZCollision:
                    player.points += 5
                    bonusBall.z = 2 #causes the ball to 'die' as ball will kill its self when z > 1
                    
            if activeSpecialBalls["TIME"] and timeBall in collisions:
                if timeBall.z > minZCollision:
                    mainBall.vz *= .75 #reduce the main ball's z speed to 75% of its current value
                    timeBall.z = 2 #causes the ball to 'die' as ball will kill its self when z > 1

                
        

        #check if  game over due to mainball traveling past z=1
        if mainBall.gameOver:
            gameFinished = "You need to hit the green ball faster after it changes from red."
        
        
        #display score:
        text = str(player.points)
        LargeText = pygame.font.Font('ERASBD.ttf',90)
        TextSurf, TextRect = objects.text_object(text, LargeText,(0,0,0))
        TextRect.center = ((objects.screenWidth/2),50)
        screen.blit(TextSurf, TextRect)

        #====== random spawn of specialty balls:
        
        if NextSpawnTime < pygame.time.get_ticks():
            NextSpawnTime = pygame.time.get_ticks() + random.randint(3000,8000) #spawn every 1 to 5 seconds
            toSpawn = random.randint(1,3) #which ball to spawn (random choice)

            #DEBUG
            #print("SPAWNING:",toSpawn,"CURRENT TIME:",pygame.time.get_ticks(),"NEXT SPAWN:",NextSpawnTime)


            #MAIN
            #need to also ensure that other ball of same type does not already exist on screen
            if toSpawn == 1 and activeSpecialBalls["DEATH"] == False:
                deathBall = objects.deathBall()
                activeSpecialBalls["DEATH"] = True
                ballObjects.add(deathBall)
            if toSpawn == 2 and activeSpecialBalls["BONUS"] == False:
                bonusBall = objects.bonusBall()
                activeSpecialBalls["BONUS"] = True
                ballObjects.add(bonusBall)
            if toSpawn == 3 and activeSpecialBalls["TIME"] == False:
                timeBall = objects.timeBall()
                activeSpecialBalls["TIME"] = True
                ballObjects.add(timeBall)

        

        

            

    #update screen:
    pygame.display.flip()
    clock.tick(60) #60fps
    #print(player.points)
#========= Game Finished! 
#determine if new high score:
endScreen = objects.endScreen()
menuObects.add(endScreen)
newHighScore = False
if highscore.retrieveHighScore()["score"] < player.points: 
    #print(player.points,highscore.retrieveHighScore()["score"])
    endScreen.newHighScore() #need new high score end screen
    newHighScore = True


nickname = str("edit name") #high score nickname

# mouse position
mouseX = 9999999999
mouseY = 9999999999
textInputColor = (0,0,0)

#=== constant varibles:
currentHighScore = highscore.retrieveHighScore()
scorePositionGameOver = (None,None)
#set score position game over:
if newHighScore:
    
    scorePositionGameOver = (615,275)
else:
    scorePositionGameOver = (465,218)


fontA = pygame.font.Font('ERASBD.ttf',69)
helpFont = pygame.font.Font('ERASBD.ttf',25)


while gameOverActive:
    #===== show background and refresh screen + other basic pygame runtime stuff
    screen.blit(bg, (0, 0))#background
    menuObects.draw(screen)

    #==== display Score
    
    TextSurf, TextRect = objects.text_object(str(player.points), fontA,(0,0,0))
    TextRect.midleft = scorePositionGameOver
    screen.blit(TextSurf, TextRect)

    #=== display help tip
    TextSurf, TextRect = objects.text_object("Hint: " + str(gameFinished), helpFont,(0,0,0))
    TextRect.midleft = (20,700)
    screen.blit(TextSurf, TextRect)

    
    
    #=========New high score screen code:
    if newHighScore:
        #print("NEW HIGIH SCORE")

        #==== display nickname input field 
        
        TextSurf, TextRect = objects.text_object(nickname, fontA,textInputColor)
        TextRect.midleft = (350,357)
        screen.blit(TextSurf, TextRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverActive = False
            #get mouse pos
            if event.type == pygame.MOUSEMOTION:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                #print(mouseX,mouseY)

            #determine if mouse cursor over txt field [Values (336,391) to (903,319)]
            if (336<mouseX<903) and (319<mouseY<391): #if mouse cursor over text field
                #change color of text to #FFFFFF to show user that field is active
                textInputColor = (255,255,255)
                #change nickname text
                if (event.type == pygame.TEXTINPUT) and len(nickname) < 9:
                    nickname += event.text
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_BACKSPACE):
                    nickname = nickname[:-1]
            else:
                textInputColor = (0,0,0)
            
            #see if mouse on save and button:
            if (482 < mouseX < 942) and (564<mouseY<679):
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    gameOverActive = False

    else: #regular game over screen

        # === interactrve element (exit button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverActive = False
            #get mouse pos
            if event.type == pygame.MOUSEMOTION:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                #print(mouseX,mouseY)

            #see if mouse on exit button:
            if (647 < mouseX < 942) and (564<mouseY<679):
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    gameOverActive = False  

        # === highscore display:
        TextSurf, TextRect = objects.text_object(str(currentHighScore["score"]), fontA,(0,0,0))
        TextRect.midleft = (465,365)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = objects.text_object(str(currentHighScore["player"]), fontA,(0,0,0))
        TextRect.midleft = (465,445)
        screen.blit(TextSurf, TextRect)
            



    #=== update display
    pygame.display.flip()
    clock.tick(60)

#== save score:
if newHighScore:
    highscore.newScore(nickname,player.points)
    highscore.save()
print(gameFinished,player.points)
pygame.quit()