import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    BIRD_POS = (250, 290, 200)
    
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_POS)
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index //5], self.rect)
        self.index += 1
        