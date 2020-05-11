import pygame
from car import Car
from wall import Wall
import random
import neat

pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
GREEN = (0, 255, 1)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

# Open a new window
SCREENWIDTH = 800
SCREENHEIGHT = 650
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

all_list_sprites = pygame.sprite.Group()  # this creates a group to store all the sprites for the game

playerCar = Car(RED, 40, 60, 70)
playerCar.rect.x = 200    # these three lines create the car using the Car class
playerCar.rect.y = 300

player1Car = Car(PURPLE, 40, 60, random.randint(50,100))
player1Car.rect.x = 400   # these three lines create the car using the Car class
player1Car.rect.y = SCREENHEIGHT -100

player2Car = Car(BLUE, 40, 60, random.randint(50,100))
player2Car.rect.x = 500   # these three lines create the car using the Car class
player2Car.rect.y = -100

player3Car = Car(YELLOW, 40, 60, random.randint(50,100))
player3Car.rect.x = 200   # these three lines create the car using the Car class
player3Car.rect.y = -300

player4Car = Car(CYAN, 40, 60, random.randint(50,100))
player4Car.rect.x = 300   # these three lines create the car using the Car class
player4Car.rect.y = -900

wallsprite = Wall(BLACK, 10, 800)
wallsprite.rect.x = 645
wallsprite.rect.y = 0

wallsprite2 = Wall(BLACK, 10, 800)
wallsprite2.rect.x = 155
wallsprite2.rect.y = 0


all_list_sprites.add(playerCar)  # this adds the player car sprite to the sprite list
all_list_sprites.add(player1Car)
all_list_sprites.add(player2Car)
all_list_sprites.add(player3Car)
all_list_sprites.add(player4Car)
all_list_sprites.add(wallsprite)
all_list_sprites.add(wallsprite2)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(player1Car)
all_coming_cars.add(player2Car)
all_coming_cars.add(player3Car)
all_coming_cars.add(player4Car)

all_collision_walls = pygame.sprite.Group()
all_collision_walls.add(wallsprite)
all_collision_walls.add(wallsprite2)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(20)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(20)
        if keys[pygame.K_DOWN]:
            speed += 0.05
        if keys[pygame.K_UP]:
            speed -= 0.05


        # --- Game logic should go here

    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSpeed(random.randint(50,100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200

    # Check if there is a car collision
    car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
    for car in car_collision_list:
        print("Car crash!")
        # End Of Game
        carryOn = False

    wall_collision_list = pygame.sprite.spritecollide(playerCar, all_collision_walls, False)
    for wall in wall_collision_list:
        print("Car crash!!")
        # end if game
        carryOn = False

    all_list_sprites.update()
    # --- Drawing code should go here
    # First, clear the screen to white.
    screen.fill(GREEN)
    # The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, GREY, (155, 0, 500, 800))
    pygame.draw.rect(screen, WHITE, (320, 0, 10, 800))
    pygame.draw.rect(screen, WHITE, (490, 0, 10, 800))
    all_list_sprites.draw(screen) # draw the spite(s) on the screen
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




