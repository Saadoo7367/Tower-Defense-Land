import pygame
from assets import tower_assets
from towers.thrower import Thrower
from towers.swordsman import Swordsman 
from towers.grenadier import Grenadier
from towers.heavy import Heavy
from path import Path

class Tower_Summoner():
    def __init__(self, screen):
        self.screen = screen
        self.towers = {
            Thrower.keybind: Thrower,
            Grenadier.keybind: Grenadier,
            Heavy.keybind: Heavy,
            Swordsman.keybind: Swordsman
        }

    def place_tower(self, keybind):
        path = Path()
        path_rects = path.get_rects()

        for k, v in self.towers.items():
            if k == keybind:
                chosen_tower = v(self.screen) #make object
                break
        
        if chosen_tower:
            tower_instance = chosen_tower 
            #Towers can stack
            #Make towers place in the middle of the mouse cursor

            mouse_pos = pygame.mouse.get_pos()

            if any(pygame.Rect(rect).collidepoint(mouse_pos) for rect in path_rects):
                return None  # Can't place tower on the path
            tower_instance.position = (mouse_pos[0] - 50, mouse_pos[1] - 50)
            tower_instance.screen.blit(tower_instance.image, mouse_pos)

            return tower_instance
        return None