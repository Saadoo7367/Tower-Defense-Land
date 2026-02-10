import pygame
from towers.tower import Tower
from projectiles.grenade import Grenade
import os

class Grenadier(Tower):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'cool_bomber_tower.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    keybind = pygame.K_w

    def __init__(self, screen):
        super().__init__(range=200, cd=200, image=Grenadier.pic, projectile=Grenade, cost=450, screen=screen)
        self.image = pygame.transform.scale(Grenadier.pic, (75, 75))
        self.position = (0,0)
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.cd = 200  # Cooldown in frames
        self.current_cd = self.cd  # Initialize current cooldown
         #default keybind

        
