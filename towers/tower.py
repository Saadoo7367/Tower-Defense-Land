import pygame
import glob
import os

class Tower:
    assets_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets'))
    pngs = glob.glob(os.path.join(assets_dir, '*.png'))
    try:
        pic = pygame.image.load(pngs[0]) if pngs else None
    except Exception:
        pic = None

    def __init__(self, range, cd, image, projectile, cost, screen):
        self.range = range
        self.image = image
        self.projectile = projectile
        self.screen = screen
        self.position = (0,0)
        self.cost = cost
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.cd = cd  # Cooldown in frames
        self.current_cd = -12 # Initialize current cooldown
        self.keybind = pygame.K_q #default keybind

    def get_Keybind(self):
        return self.keybind
    
    def get_coords(self):
        return (self.image, self.position)
    
    def find_enemy(self, enemies):
        self.enemies_in_range = []
        for enemy in enemies:
            enemy_x, enemy_y = enemy.get_position()
            tower_x, tower_y = self.position

            distance = ((enemy_x - tower_x) ** 2 + (enemy_y - tower_y) ** 2) ** 0.5

            if distance <= self.range:
                self.enemies_in_range.append(enemy)            
               
        return enemies

    def projectile_movement(self):
        for projectile in self.projectiles_alive:
            movement = projectile.move_towards_enemy()
            if projectile.is_alive() == False:
                self.projectiles_alive.remove(projectile)

            elif movement == False:
                self.projectiles_alive.remove(projectile)

            elif not movement == False:
                return movement

    def shoot(self):
        enemies = self.find_enemy(self.enemies_in_range)

        if len(self.enemies_in_range) > 0:
            target_enemy = self.enemies_in_range[0] # change up the targeting list later

        if len(self.enemies_in_range) == 0:
            return  
        
        if self.current_cd > 0:
            self.current_cd -= 1
            movement = self.projectile_movement()

        else:
            self.current_cd = self.cd  # Reset cooldown

            self.projectiles_alive.append(self.projectile(screen=self.screen, position=self.position, enemies=enemies, target_enemy=target_enemy))
            
            movement = self.projectile_movement()


    def get_cost(self):
        return self.cost