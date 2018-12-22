import pygame
import os
import random
from pygame.locals import *

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=700
screen_height=400
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# --- Classes
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        
        self.image.fill(color)

        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0
        
    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([10, 20])
        self.image.fill(red)
         
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keystate[pygame.K_RIGHT]:
            self.rect.x += 5
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(white)
        
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 5

def game():
    # --- Sprite lists

    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
     
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    # List of each block in the game
    block_list = pygame.sprite.Group()
     
    # List of each bullet
    bullet_list = pygame.sprite.Group()

    # Create a red player block
    player = Player()
    all_sprites_list.add(player)

    # --- Create the sprites

    for i in range(5):
        # This represents a block
        block = Block(blue, 20, 15)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(350)

        block.change_x = random.randrange(-3, 4)
        block.change_y = random.randrange(-3, 4)
        block.left_boundary = 0
        block.top_boundary = 0
        block.right_boundary = screen_width
        block.bottom_boundary = screen_height
        
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)
     
    score = 0
    player.rect.y = 380

    # Current level
    level = 1

    # Current live
    live = 3

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                done = True
     
            elif keystate[pygame.K_SPACE]:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
     
        # --- Game logic
     
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
     
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
     
            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)
     
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                
        block_hit_player = pygame.sprite.spritecollide(player, block_list, True)
        if block_hit_player:
            live -= 1
            if live == 0:
                done = True

        # --- Draw a frame

        # Check to see if all the blocks are gone.
        # If they are, level up.
        if len(block_list) == 0:
            # Add one to the level
            level += 1

            # Add more blocks. How many depends on the level.
            # Also, an 'if' statement could be used to change what
            # happens customized to levels 2, 3, 4, etc.
            for i in range(level * 5):
                # This represents a block
                block = Block(blue, 20, 15)

                # Set a random location for the block
                block.rect.x = random.randrange(screen_width)
                block.rect.y = random.randrange(350)

                block.change_x = random.randrange(-3, 4)
                block.change_y = random.randrange(-3, 4)
                block.left_boundary = 0
                block.top_boundary = 0
                block.right_boundary = screen_width
                block.bottom_boundary = screen_height
                
                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)
     
        # Clear the screen
        screen.fill(black)
     
        # Draw all the spites
        all_sprites_list.draw(screen)

        text = font.render("Score: "+str(score), True, white)
        screen.blit(text, [10, 10])
            
        text = font.render("Level: "+str(level), True, white)
        screen.blit(text, [10, 40])

        text = font.render("Live: "+str(live), True, white)
        screen.blit(text, [10, 70])
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
     
    main_menu()

# Game Fonts
font = "Limelight.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(blue)
        title=text_format("Shooter Pro", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 70))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 260))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 320))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

#Initialize the Game
main_menu()
