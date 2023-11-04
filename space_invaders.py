# Space Invaders
# Python 3.9.5 on Mac

import turtle
import os
import math
import random
import platform



# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width = 700, height = 700)
screen.tracer(0) # shuts off all the screen updates 

# Register the shapes
turtle.register_shape("files/alien2.gif")
turtle.register_shape("files/small_ship.gif")



# Draw outer border
outer_pen = turtle.Turtle()
outer_pen.color("blue") # Spell gray not grey? test
outer_pen.pensize(55) # test
outer_pen.speed(0)
x = outer_pen.xcor = -325
y = outer_pen.ycor = -325
outer_pen.penup()
outer_pen.goto(x,y)
outer_pen.pendown()
for s in range (2): # why 2?
    outer_pen.forward(650) # test this
    outer_pen.left(90) # test
    outer_pen.forward(650) # test
    outer_pen.left(90)

# Draw title
title = turtle.Turtle()
title.speed(0)
title.shape("square")
title.color("white")
title.penup()
title.hideturtle()
title.goto(0,310)
title.write("Space Invaders", align="center", font=("courier", 30, "normal"))

# Draw inner border
border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.speed(6)
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0


# Draw score
score_pen = turtle.Turtle()
score_pen.speed()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Areial", 14, "normal"))
score_pen.hideturtle()


# Create the player turtle
player = turtle.Turtle()
player.setheading(90)
player.color("light blue")
player.shape("files/small_ship.gif")
player.penup()
player.speed(1)
player.setposition(0, -265)
player.setheading(90)
player.speed = 0

# Create enemies
# Choose a number of enemies
number_of_enemies = 30

# Create an empty list of enemies
enemies = [] # list b/c []

# Add enemies to list (actual turtle objects)
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("files/alien2.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.shapesize(50, 50)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y 
    enemy.setposition(x,y)
    # Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0 
    
enemyspeed = 0.15


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.18, .75)
bullet.hideturtle()
y = player.ycor()
bullet.sety(y)

# Create the player's bullet
bullet2 = turtle.Turtle()
bullet2.color("magenta")
bullet2.shape("square")
bullet2.penup()
bullet2.speed(0)
bullet2.setheading(90)
bullet2.shapesize(0.18, .75)
bullet2.hideturtle()
y = player.ycor()
bullet2.sety(y)

bulletspeed = 5

# Define a pause state
paused = False

# Define bullet state, which controls bullet behavior
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"
bulletstate2 = "ready"
spacestate = "1"

# define game mechanics
def move_left():
    player.speed = -2

def move_right():
    player.speed = 2

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -270:
        x = -270
    if x > 270:
        x = 270
    player.setx(x)

# Function to toggle pause state
def toggle_pause():
    global paused
    if paused:
        paused = False
    else:
        paused = True

def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bulletstate
    global bulletstate2
    global spacestate

    if spacestate == "1" and bulletstate == "ready":
        play_sound("files/3_12.WAV")
        bulletstate = "fire"
        # Move the bullet to just above the player
        x = player.xcor() 
        y = player.ycor() + 5
        bullet.setposition(x, y)
        bullet.showturtle()
        spacestate = "2"
    elif spacestate == "2" and bulletstate2 == "ready":
        play_sound("files/3_12.WAV")
        bulletstate2 = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 5
        bullet2.setposition(x, y)
        bullet2.showturtle()
        spacestate = "1"

def isCollision(t1, t2): # Going to return True or False
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

def play_sound(sound_file, time = 0): # Time is in sec, how many seconds before time file repeats?, if no time, it doesn't repeat
    os.system("afplay {}&".format(sound_file))
    
    # Repeat sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))
    

# Create keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right") # make sure to capitaize the "R"
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(fire_bullet, "space") # lower case spelled
screen.onkeypress(toggle_pause, "p") # pause

# Play background music
play_sound("files/bgm.mp3", 119)

# Main game loop
while True: # Game runs forever, keeps on running
    screen.update() # Updates each time through the loop
    if paused:
        # Display pause message
        pause_message = turtle.Turtle()
        pause_message.speed(0)
        pause_message.shape("square")
        pause_message.color("white")
        pause_message.penup()
        pause_message.hideturtle()
        pause_message.goto(0, 0)
        pause_message.write("Game Paused. Press 'p' to resume.", align="center", font=("Courier", 24, "normal"))

        while paused:
            # Game is paused; wait for the player to resume or exit
            screen.update()
        
        # Remove the pause message when unpaused
        pause_message.clear()
        pause_message.hideturtle()
    move_player()

    # Enemy mechanics
    for enemy in enemies:
        # Moving the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        # Check if the enemy is at the left or right wall
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Enemy collides with player
        if isCollision(player, enemy):
            enemyspeed = 0
            player.speed = 0
            x = player.xcor()
            player.setx(10000) # Sends the turtle out of range so the losing.mp3 does not constantly repeat
            play_sound("files/impact_crete.wav")
            play_sound("files/losing.mp3")
            player.hideturtle()
            enemy.hideturtle()
            # Draw Message
            lose = turtle.Turtle()
            lose.speed(0)
            lose.shape("square")
            lose.color("red")
            lose.penup()
            lose.hideturtle()
            lose.goto(0,0)
            lose.write("GAME OVER.", align="center", font=("Courier", 60, "normal"))
            break
            
        # Check for collision between bullet and enemy 
        if isCollision(bullet, enemy):
            play_sound("files/impact_crete.wav")
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0,10000)
                
            # Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Areial", 14, "normal"))

            # Increase enemy speed
            if enemyspeed > 0:
                enemyspeed += 0.025
            else:
                enemyspeed -= 0.025

            # Check for collision between bullet2 and enemy 
        if isCollision(bullet2, enemy):
            play_sound("files/impact_crete.wav")
            # Reset the bullet2
            bullet2.hideturtle()
            bulletstate2 = "ready"
            bullet2.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0,10000)
                
            # Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Areial", 14, "normal"))

            # Increase enemy speed
            if enemyspeed > 0:
                enemyspeed += 0.05
            else:
                enemyspeed -= 0.05


    # If enemy hits bottom border
    if enemy.ycor() < -285:
        enemyspeed = 0
        player.speed = 0
        player.sety(10000) # Sends the turtle out of range so the losing.mp3 does not constantly repeat
        play_sound("files/impact_crete.wav")
        play_sound("files/losing.mp3")
        player.hideturtle()
        enemy.hideturtle()
        # Draw Message
        lose = turtle.Turtle()
        lose.speed(0)
        lose.shape("square")
        lose.color("red")
        lose.penup()
        lose.hideturtle()
        lose.goto(0,0)
        lose.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
        break


    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)

    # Move bullet2
    if bulletstate2 == "fire":
        y = bullet2.ycor()
        y = y + bulletspeed
        bullet2.sety(y)
        screen.onkeypress(fire_bullet, "space") == False 
        

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 290:
        bullet.hideturtle()
        bulletstate = "ready"

    # Check to see if the bullet2 has gone to the top
    if bullet2.ycor() > 290:
        bullet2.hideturtle()
        bulletstate2 = "ready"

    # Play winning song if won
    if score == 300:
        play_sound("files/winning.mp3")
        player.speed = 0
        player.hideturtle()
        enemy.hideturtle()
        # Draw Message
        win = turtle.Turtle()
        win.speed(0)
        win.shape("square")
        win.color("yellow")
        win.penup()
        win.hideturtle()
        win.goto(0,0)
        win.write("YOU WIN", align="center", font=("Courier", 60, "normal"))
        break