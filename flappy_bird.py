# start modules
import pgzrun
import sys 
# create constants
WIDTH = 800
HEIGHT = 600
score = 0
# print welcome
print ("The game is about to start!")
print ('Click the mouse to "flap" upwards')
print ("Dodge the pipes and the floor")
print ("Good luck and the floor")
print ("Good luck and have fun!")

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300
# make pipes
topPipe1 = Actor("top")
topPipe1.x = 366
topPipe1.y = 0
bottomPipe1 = Actor('bottom')
bottomPipe1.x = 366
bottomPipe1.y = 800

topPipe2 = Actor("top")
topPipe2.x = 632
topPipe2.y = -200
bottomPipe2 = Actor('bottom')
bottomPipe2.x = 632
bottomPipe2.y = 560

topPipe3 = Actor("top")
topPipe3.x = 898
topPipe3.y = -120
bottomPipe3 = Actor('bottom')
bottomPipe3.x = 898
bottomPipe3.y = 710
# draw everything to screen
def draw (): 
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    topPipe1.draw()
    bottomPipe1.draw()
    topPipe2.draw()
    bottomPipe2.draw()
    topPipe3.draw()
    bottomPipe3.draw()
# update everything
def update ():
    # update bird
    global score
    bird.y = bird.y + 1 
    # update pipes
    if topPipe1.x < -44:
        topPipe1.x = WIDTH
        score = score + 1
    if topPipe2.x < -44:
        topPipe2.x = WIDTH
        score = score + 1
    if topPipe3.x < -44:
        topPipe3.x = WIDTH
        score = score + 1
    if bottomPipe1.x < -44:
        bottomPipe1.x = WIDTH
    if bottomPipe2.x < -44:
        bottomPipe2.x = WIDTH
    if bottomPipe3.x < -44:
        bottomPipe3.x = WIDTH        
    topPipe1.x = topPipe1.x - 1
    bottomPipe1.x = bottomPipe1.x - 1
    topPipe2.x = topPipe2.x - 1
    bottomPipe2.x = bottomPipe2.x - 1
    topPipe3.x = topPipe3.x - 1
    bottomPipe3.x = bottomPipe3.x - 1
    # bird hits bottom of screen
    if bird.y > HEIGHT:
        print("Game Over!")
        print(f"Score: {score}")
        sys.exit()
    # bird hits pipes
    if bird.colliderect(topPipe1):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()
    if bird.colliderect(topPipe2):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()
    if bird.colliderect(topPipe3):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()
    if bird.colliderect(bottomPipe1):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()
    if bird.colliderect(bottomPipe2):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()
    if bird.colliderect(bottomPipe3):
        print("Hit!")
        print(f"Score: {score}")
        sys.exit()                
# moving
def on_mouse_down():
    bird.y = bird.y - 50
# runs everything
pgzrun.go()