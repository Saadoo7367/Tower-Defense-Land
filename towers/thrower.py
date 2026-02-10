import pygame
from towers.tower import Tower
from projectiles.turd import Turd
import os

class Thrower(Tower):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'cool_tower.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None
    
    keybind = pygame.K_q #default keybind

    def __init__(self, screen):
        super().__init__(range=200, cd=120, image=Thrower.pic, projectile=Turd, cost=300, screen=screen)
        self.image = pygame.transform.scale(Thrower.pic, (75, 75))
        self.position = (0,0)
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.cd = 120  # Cooldown in frames
        self.current_cd = self.cd  # Initialize current cooldown