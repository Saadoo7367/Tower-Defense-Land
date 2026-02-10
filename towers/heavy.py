import pygame
from towers.tower import Tower
from projectiles.bullet import Bullet
import os

class Heavy(Tower):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'cool_sniper_tower.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    keybind = pygame.K_r #default keybind
    
    def __init__(self, screen):
        super().__init__(range=1000, cd=1100, image=Heavy.pic, projectile=Bullet, cost=1250, screen=screen)
        self.image = pygame.transform.scale(Heavy.pic, (75, 75))
        self.position = (0,0)
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.cd = 1100  # Cooldown in frames
        self.current_cd = self.cd  # Initialize current cooldown
