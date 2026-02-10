import pygame
from projectiles.projectile import Projectile
import os

class Grenade(Projectile):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'grenade.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    explosion_pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'explosion.png'))
    try:
        explosion_pic = pygame.image.load(explosion_pic_location) 
    except Exception:
        explosion_pic = None

    def __init__(self, screen, position, enemies, target_enemy):
        super().__init__(name="Grenade", damage=6, speed=3.4, image=Grenade.pic, screen=screen, position=position, enemies=enemies, target_enemy=target_enemy, lifetime=120)
        self.image = pygame.transform.scale(Grenade.pic, (30, 30))
    
    def explode(self):
        size = (75, 75)
        self.position = (self.position[0] + size[0]/2, self.position[1] + size[1]/2)
        explosion_image = pygame.transform.scale(Grenade.explosion_pic, size)
        
        self.screen.blit(explosion_image, (self.position[0] - size[0]//2, self.position[1] - size[1]//2))

        for enemy in self.enemies:
            enemy_x, enemy_y = enemy.get_position()
            proj_x, proj_y = self.position

            distance = ((enemy_x - proj_x) ** 2 + (enemy_y - proj_y) ** 2) ** 0.5

            if distance <= size[0]:
                enemy.take_damage(self.damage)    