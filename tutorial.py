# Import necessary libraries
import pygame
import sys
import time
#from scripts.utils import Physics


class Game:
    def __init__(self):

        # Initiate pygame
        pygame.init()
        # Name the pygame window
        pygame.display.set_caption('Game Zero')

        # Set screen size
        self.screen = pygame.display.set_mode((640, 480))
        # Instantiate a clock object
        self.clock = pygame.time.Clock()

        # Load the player image
        self.player_entity = pygame.image.load('data/images/entities/player.png')

        # Clears the black background on the player_entity image
        self.player_entity.set_colorkey((0,0,0))

        # Define the player's beginning position
        self.player_pos = [0, 200 - self.player_entity.get_height()]

        # Create a collision box for the ground
        self.collision_area = pygame.Rect(0, 200, 100, 100)
        





    def run(self):

        def gravity(self):

            self.player_pos[1] += 0.5

        def jump(self):

            self.player_pos[1] -= 1

        while True:

            # Create a collision box for the player
            player_collision = pygame.Rect(self.player_pos[0], self.player_pos[1], self.player_entity.get_width(), self.player_entity.get_height())

            # Fill the screen with a light blue color
            self.screen.fill((14, 219, 248))

            # Blit the player at position[0], position[1]
            self.screen.blit(self.player_entity, (self.player_pos[0], self.player_pos[1]))

            pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area) 


            # If player_collision collides with collision_area, enact gravity or not
            if not player_collision.colliderect(self.collision_area):
                gravity(self)
            else:
                pass

            # Check for user input
            for event in pygame.event.get():

                
                # Check if user wants to exit program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Logic to jump and drop depending on collision boxes
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player_collision.colliderect(self.collision_area):
                        for i in range(0, 50):
                            jump(self)
                    if event.key == pygame.K_DOWN and not player_collision.colliderect(self.collision_area):
                        self.player_pos[1] += 5

            # Check if key is being held down
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.player_pos[0] -= 2
            if keys[pygame.K_RIGHT]:
                self.player_pos[0] += 2



            # Update the display
            pygame.display.update()
            # Set FPS
            self.clock.tick(60)

            

# Run the game
Game().run()

