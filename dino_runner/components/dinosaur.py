import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SCREEN_WIDTH
class Dinosaur(Sprite):
    X_Pos = 80
    Y_Pos = 310
    JUMP_VEL = 8.5
    POS_DUCK = 340
    
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_Pos
        self.dino_rect.y = self.Y_Pos
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.type = DEFAULT_TYPE
        self.setup_state_booleans()
    
    
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()  
        if self.dino_duck:
            self.duck() 
            
        if user_input[pygame.K_DOWN]and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False    
        if self.step_index >= 10:
            self.step_index = 0         
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
    def run(self):
        if self.shield:
            self.image = RUNNING_SHIELD 
            self.dino_rect.y = self.Y_Pos
            if self.step_index< 5:
                self.image = RUNNING_SHIELD[0]
            else:
                self.image = RUNNING_SHIELD[1]
            self.step_index += 1
        else:
            self.image = RUNNING
            self.dino_rect.y = self.Y_Pos
            if self.step_index< 5:
                self.image = RUNNING[0]
            else:
                self.image = RUNNING[1]
        self.step_index += 1
               
    def jump(self):
        if self.shield:
            self.image = JUMPING_SHIELD
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            if self.jump_vel < -self.JUMP_VEL:
                self.dino_rect.y = self.Y_Pos
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL
        
        else:
            self.image = JUMPING
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            if self.jump_vel < -self.JUMP_VEL:
                self.dino_rect.y = self.Y_Pos
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL
                
    
    def duck(self):
        if self.shield:
           self.image = DUCKING_SHIELD[0] 
           self.dino_rect.y = self.POS_DUCK
           if self.step_index< 5:
               self.image = DUCKING_SHIELD[0]
           else:
               self.image = DUCKING_SHIELD[1]
           self.step_index += 1
                
        else:
            self.image = DUCKING [0]
            self.dino_rect.y = self.POS_DUCK
            if self.step_index< 5:
                self.image = DUCKING[0]
            else:
                self.image = DUCKING[1]
            self.step_index += 1
            
                
            
        
    def setup_state_booleans(self):
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
        self.has_powerup = False
    
    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round ((self.shield_time_up - pygame.time.get_ticks())/1000,2)
            if time_to_show >= 0:
                if self.show_text:
                    font = pygame.font.Font('freesansbold.ttf', 18)
                    text = font.render(f'Shield enable for {time_to_show}', True, (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (500, 40)
                    screen.blit(text, textRect)
            else:
                self.shield = False
            