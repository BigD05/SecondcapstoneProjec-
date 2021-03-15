import pygame 
import random  #imports pygame and random

pygame.init() 

screen_width = 1100
screen_height = 700 #sets the screen height and with
screen = pygame.display.set_mode((screen_width,screen_height))#this displays it 



player = pygame.image.load("download.jpeg")
enemy = pygame.image.load("arrow.png")
enemy2 = pygame.image.load("knife.png") #stores all our image files in these variables 
prize = pygame.image.load("prize.jpg")


image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()    #gets the height and width of all the images and stores them in the appropriate variable
enemy2_width = enemy2.get_width()
enemy2_height = enemy2.get_height()
prize_height = prize.get_height()
prize_width = prize.get_width()



playerXPosition = 100
playerYPosition = 50
enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)
enemy2XPosition = screen_width                                     #spawns in the images on the screen at a random position
enemy2YPosition = random.randint(0,screen_height - enemy2_height)
prizeXPosition = screen_width
prizeYPosition = random.randint(0,screen_height - prize_height)


while 1: 
    
    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2,(enemy2XPosition,enemy2YPosition))
    screen.blit(prize,(prizeXPosition,prizeYPosition))
    pygame.display.flip()

    for event in pygame.event.get():
                                        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    if event.type == pygame.KEYDOWN:
        
                                                        
                                                        # Test if the key pressed is the one we want.
        if event.key == pygame.K_LEFT: 
            if playerXPosition  > 0   :
                    playerXPosition -=1 
        if event.key == pygame.K_RIGHT:
            if playerXPosition < screen_width - image_width :
                    playerXPosition +=1 
        if event.key == pygame.K_UP:        # pygame.K_UP represents a keyboard key constant. 
            if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
                    playerYPosition -= 1
        if event.key == pygame.K_DOWN:
            if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
                    playerYPosition += 1

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.
    ## Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition


    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
                                                        # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
                                        # Display losing status to the user: 
        print("You lose!")

                                        #Quite game and exit window: 
        pygame.quit()
        exit(0)
    if playerBox.colliderect(enemy2Box):
    
                                        # Display losing status to the user: 
        print("You lose!")

                                        #Quite game and exit window: 
        pygame.quit()
        exit(0)
        
    if playerBox.colliderect(prizeBox):
    
                                        # Display losing status to the user: 
        print("You Win")

                                        #Quite game and exit window: 
        pygame.quit()
        exit(0)  
                                                    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
                                                        # Display wining status to the user: 
        
        print("You win!")
        
                                                            # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    

    
                                                                # Make enemy approach the player at the specific speeds.
    prizeXPosition -=0.13
    enemyXPosition -= 0.10
    enemy2XPosition -=0.15 


