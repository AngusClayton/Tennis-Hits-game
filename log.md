# GitHub repository link:

https://github.com/Happypig123123/Tennis-Hits-game

# Stack overflow account link:

https://stackoverflow.com/users/11463378/angusclayto



# Useful website on adding text to pygame


## Game Idea 1 [4hrs]

# 16/5/2021

Developing game ideas; currently thinking of 'endless' scroller game. 

Decided on a game where player has to dodge objects, some objects are useful and player should collide with.

player dodges objects by 'flipping gravity'



At this stage game needs:

- Title Screen
- Collision detection
  - which should reduce health of player by enemy.damage amount.
  - enemy then should despawn
  - sound effect?



## Game Idea 2 [4hrs] 30/5/2021
Decided that the gravity flip game was too basic; so have decided to make a tennis game.
There will be four balls:

The *main ball* the player must hit every time; if it goes past the player (i.e. z position is > 1) then the game ends.

![Main Ball](img/readyBall.png)![Main Ball](img/notReadyBall.png)

The *main ball* must be hit at the right time (when the ball is green, not when the ball is red).
    When ball green and hit; player is awarded 1 point
    When ball red and hit; player does not get point for hitting ball. 
        This feature is to stop the player from holding mouse over ball; making the game harder as there is the timing component.
        It is not intended to make the player loose the game from lack of points.

The *purple ball* gives the player 5 points when hit; compared to the main balls single point (but you must still hit the main ball)

![Main Ball](img/pointsBall.png)

The *yellow ball* slows down time (in practise by decreasing the Z velocity by a positive scalar < 1). This effect is never reversed, and reliez on the z velocity being multiplied when impacted by the players and the computers racket.

![Main Ball](img/timeBall.png)

The *grey ball* end the game when the user touches it; it is sort of a 'bomb' ball.

![Main Ball](img/deathBall.png)

### Features added as of 30/5/2021:
Completed rough game design (story board).
Completed the game graphics.
Implemented the main ball code, player racket and help/start sequence.

## 31/5/2021 [2hrs]

Implemented the specialty balls.

The purple and grey balls are quite self explanatory in documentation above.

The time ball works by reducing the Z velocity of the ball to 75% of its original value.  This allows the player to have more time to get the timing on the main ball correct.

### 3D effect

The game relies on a pseudo 3D effect, changing the size of objects as the become closer/further away. This following website helped:

https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame



### Game difficulty / Timing 

![Dificulty Over Time time Bomb](documentationImagery/Dificulty Over Time [Time Bomb].png)

In the **above graph** you can see the the time bomb slows down the rate Z velocity. Unlike in the **graph below** where no time bombs were used, and the game becomes 'impossible' after 40,000ms. 

***NOTE: Negative values represent when the ball is heading away from player (negative velocity);  The magnitude is what is important*** 

![Dificulty Over Time noTime Bomb](documentationImagery/DifficultNoTimeBomb.png)

These graphs were developed utilizing this piece of code; placed around the `while gameFinished == False:` line of code.

```python
prevV = 0 #FOR DATA ANALYSIS OF THE Z VELOCITY OF MAINBALL
while gameFinished == False: #main loop; change gameFinished when game is exited to True
    if mainBall.vz != prevV: #only output change in velocity. Don't need those extra data points; as just forms straight lines.
        print(pygame.time.get_ticks(),mainBall.vz)
        prevV = mainBall.vz
```

For testing purposes; the balls were initially triggered by key presses; but are now triggered at random;

#### Testing Code:

```python
        if True: #Change to false when not debuging the specialty balls
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
```

####  Final Game Code:

```python
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
```

## Added point score

https://pythonprogramming.net/displaying-text-pygame-screen/

This website helped with adding text to the screen, as well as tutorials. 

## To Do [As of 31/5/21]

- Add end screen
- Add high score database
- Finalise documentation
- Improve help screen looks
- Add 'tooltips' when user dies; telling them why and what they can do to improve

# 11/6/2021 [2.5 hrs]

## Font choice:

**ERAS DEMI ITC** for static text as of 11/6/2021; pygame dynamic text is all <u>Free and open sans</u>



## Adding High Score Functionality:

Used a json file to score high scores:

https://www.programiz.com/python-programming/json *helpful article on json use in python.*

Created a highscore.py file; containing easy to use functions to interface with high score db file.



## Game over screen

Added game over screen, has two 'screens'; one for when you get beat high score, and one when you don't:

#### Game Over New high score:

***Note: the dark blue box is a text input field.***



![New high score](img/NewHighScore.png)

 

#### Game Over Regular

![Regular Game Over](img/GameOver.png)

## To Do: As of 11/6/21

- Finish Game over screen.
  - Make the exit button exit; and save button save high score
- Finalise documentation
- Improve help screen looks
- Add 'tooltips' when user dies; telling them why and what they can do to improve

# 12/5/2021 [4Hrs]

#### Added help message.

Help message appears when the user 'dies'; informing them how to do better next-time.

#### Finalized game over screen.

Exit buttons work; high score information displaying correctly.

Made pygame text fonts **ERASBD.ttf** to match static text.

#### Change in Active Specialty balls. [From Sam's user feedback.]

From user feedback; found that if you leave racket in middle; it will hit the specialty balls before user had time to register they were there. Now made it so that specialty ball z has to be greater than 10%.

#### Data Dictionary Complete

The data dictionary was completed. As there are many variables; I wrote some code to automate the process.

The first part below creates a 'script' to test all the data types.

```python
program = """ STRING CONTAINING ALL CODE! """
varibles = {}
program = program.split("\n") #Split into array of liens
for i in program: #loop throough lines
    i = i.strip()
    if (" = " in i) and i[0] != '#':
        
        x = i.split(" = ")
        if x[0] not in varibles:
            varibles.update({x[0]:x[1]})

for i in varibles:
    print("try:")
    print("    print('"+i+"',type("+i+"))")
    print("except:")
    print("    print('error",i,"')")

        
```

It produces output such as:

```python3
try:
    print('size',":",type(size))
except:
    print('error size ')
try:
    print('screen',":",type(screen))
except:
    print('error screen ')
try:
    print('gameIcon',":",type(gameIcon))
except:
    print('error gameIcon ')
```

This output is then ran at the bottom of the main.py program, outputting the datatype for each variable. Now I only have to add the description for 45+ variables instead of name and type manually.



The data dictionary is **complete** for all python files (main.py, objects.py, highscore.py)

#### Story Board.

The story board was finalized as some modifications need for the creation of the last 'screen' options *game over screens.*

It showcases the flow between different screens in the application, from main menu sequence, to gameplay, to game over.

## To do 12/06/2021

- Add Gannt chart excel document to the documentation word document.
- Add GitHub commits to log book!
- Ensure files are organised. 
- Do some final user testing.
- Write maintenance and future considerations plan.
- Evaluate success with design specifications
- write about use of IDE

# 13/6/2021 [20min]

Completed future considerations and maintenance plan.

Finished Evaluation.

Added user testing from Sam. ***Still need more user feedback from others.***

## Addressing User feedback

The problems with hit box size have been addressed, the `changeZ()`function was not changing the death balls hitbox or `rect`, causing size of hitbox to be different from visual size.

The balls no-longer end the game if they spawn under the users racket; as the size of the ball must satisfy `z>20%` for collisions to be enabled. 

I am planning to make the points indicator change colour to show that a bonus / time ball has been activated. 

Also am planning to add music.

Not planning to add pause menu at this stage due to time constraints, however have included this in future considerations.

# 15/5/2021 [20min]

Tried to add music, but pygame errors. Asked question on stack overflow.

https://stackoverflow.com/questions/67982927/cannot-play-music-pygame-win-10

#### Question:

Hi when trying to play music in pygame; my win10 machine gives this error:
here is code snippet:
```
    pygame.mixer.music.load('dioma.mp3') #Jnathyn - Dioma [NCS Release] #14/6/2021
    pygame.mixer.music.play(-1, 0.0)
```
here is error snippet:
```
Traceback (most recent call last):
  File ".\main.py", line 33, in <module>
    pygame.mixer.music.load('dioma.mp3') #Jnathyn - Dioma [NCS Release] #14/6/2021
pygame.error: Failed loading libmpg123-0.dll: The specified module could not be found.
```
Thanks. Have tried installing .ddl manually into sys32

----

## Made text input more obvious
In response to user feedback, made text input box more obvious; and acts like a typical text input box. 
## Implementation of points colour
In response to user feedback,
makes it obvious that the game has registered a point loss or gain. Also makes it obvious when you hit a time bomb or bonus ball that something happened.


# GITHUB COMMIT LOG:

Latest to oldest order:

### Commits on Jun 13, 2021

    Documentation 

### Commits on Jun 12, 2021

	Update Log.md 


	added events to log that i forgot to add
	
	some file management


	Active Specialty Balls now don't register collisions at low Z values.…



	Finalized game over.
	
	Highscore + Game Over screen

### Commits on Jun 1, 2021

	Update README.md
	Merge pull request #1 from Silveridge/patch-1
		(Sam's User Feedback)
	
	User Feedback @Silveridge

### Commits on May 31, 2021

	Update log.md
	 
	Implemented the specialty balls.

### Commits on May 30, 2021	


	Update README.md
	
	Updated README to incl link to log.md
	
	Added basic files
	
	Initial commit 

