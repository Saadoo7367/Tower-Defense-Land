import pygame
from towers.tower import Tower
from projectiles.sword import Sword
import os

class Swordsman(Tower):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'cool_sword_tower.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None
    
    keybind = pygame.K_e #default keybind

    def __init__(self, screen):
        super().__init__(range=100, cd=70, image=Swordsman.pic, projectile=Sword, cost=250, screen=screen)
        self.image = pygame.transform.scale(Swordsman.pic, (75, 75))
        self.position = (0,0)
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.cd = 70  # Cooldown in frames
        self.current_cd = self.cd  # Initialize current cooldown