import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus, Cactus_2
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                 self.obstacles.append(Cactus(SMALL_CACTUS))
            
            elif random.randint(0, 2) == 1:
                 self.obstacles.append(Cactus_2(LARGE_CACTUS))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        