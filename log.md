# Stack overflow article helped with the Z scaling
https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame

# Usefull website on adding text to pygame
https://pythonprogramming.net/displaying-text-pygame-screen/

## 30/5/2021
Decisded that the gravity flip game was too basic; so have desided to make a tenis game.
There will be three balls:

The *main ball* the player must hit every time; if it goes past the player (i.e. z position is > 1) then the game ends.
The *main ball* must be hit at the right time (when the ball is green, not when the ball is red).
    When ball green and hit; player is awarded 1 point
    When ball red and hit; player does not get point for hitting ball. 
        This feature is to stop the player from holding mouse over ball; making the game harder as there is the timing component.
        It is not intendead to make the player loose the game from lack of points.

The *purple ball* gives the player 5 points when hit; compared to the main balls single point (but you must still hit the main ball)

The *yellow ball* slows down time (in pracise by decreasing the Z velocity by a positive scalar < 1). This effect is never reversed, and reliez on the z velocity being multiplied when impacted by the players and the computers racket.

### Features added as of today:
Completed the game design.
Completed the game graphics.
Implimented the main ball code, player racket and help/start sequence.