
# import pygame package
import pygame
import time
from path import Path
from towers.tower import Tower
from towers.tower_summoner import Tower_Summoner
from base_health import BaseHealth
from enemies.waves.wave_structure import Wave_Structure

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
screen = pygame.display.set_mode((500, 500))

# Setting name for window
pygame.display.set_caption('Tower Defense game')

# creating a bool value which checks 
# if game is running
running = True

bg_image = pygame.image.load("map.png")
path_image = pygame.image.load("path.png")
screen.blit(bg_image, (0,0))

base = BaseHealth(100, screen)

path = Path()
path_points = path.get_path_points()

ws = Wave_Structure(screen)
enemies = []

counter = 1000
is_alive = True
towers = []

money = 500

wave_info = ws.read()
normal_count = int(wave_info[ws.wave - 1][1])
normal_time = int(wave_info[ws.wave - 1][2])
speedy_count = int(wave_info[ws.wave - 1][3])
speedy_time = int(wave_info[ws.wave - 1][4])
tank_count = int(wave_info[ws.wave - 1][5])
tank_time = int(wave_info[ws.wave - 1][6])
boss_count = int(wave_info[ws.wave - 1][7])
boss_time = 0 
wave_over = False

ts = Tower_Summoner(screen)
# Game loop
# keep game running till running is true
while running:
    # Check for event if user has pushed 
    # any event in queue

    if wave_over == True:
        wave_over = False
        ws.wave += 1
        if ws.wave > len(wave_info):
            if len(enemies) == 0:
                print(f"All waves completed! {len(wave_info)} waves defeated.")
                running = False
        else:
            print(f"Starting wave {ws.wave}!")

            normal_count = int(wave_info[ws.wave - 1][1])
            normal_time = int(wave_info[ws.wave - 1][2])
            speedy_count = int(wave_info[ws.wave - 1][3])
            speedy_time = int(wave_info[ws.wave - 1][4])
            tank_count = int(wave_info[ws.wave - 1][5])
            tank_time = int(wave_info[ws.wave - 1][6])
            boss_count = int(wave_info[ws.wave - 1][7])
            print(f"normal time: {normal_time}, speedy time: {speedy_time}, tank time: {tank_time}, boss time: {boss_time}")
            print(f"Spawning {normal_count} normal enemies, {speedy_count} speedy enemies, {tank_count} tank enemies, and {boss_count} boss enemies.")

    if counter <= 0:
        enemy_summoning_info = ws.summon(normal_count, speedy_count, tank_count, boss_count)
        num_enemies = enemy_summoning_info[1]
        
        normal_count = int(num_enemies[0]) 
        speedy_count = int(num_enemies[1])
        tank_count = int(num_enemies[2]) 
        boss_count = int(num_enemies[3]) 

        if enemy_summoning_info[0] == None:
            if normal_count <= 0 and speedy_count <= 0 and tank_count <= 0 and boss_count <= 0 and len(enemies) == 0:
                wave_over = True
                counter = 1000
        else:
            if is_alive:    
                enemies.append(enemy_summoning_info[0])

        if normal_count > 0:
            counter = normal_time
        elif normal_count <= 0:
            counter = speedy_time
        elif speedy_count <= 0:
            counter = tank_time
        elif tank_count <= 0:
            counter = boss_time
        else:
            counter = normal_time    
    else:
        counter -= 1

    for enemy in enemies:
        if enemy.move():
            take_damage = enemy.health
            base_hp = base.take_damage(take_damage)  
            money += enemy.get_bounty()
            enemies.remove(enemy)
            if base_hp <= 0:
                max_enemies = 0
                is_alive = False
                
        
        if enemy.health <= 0:
            money += enemy.get_bounty()
            enemies.remove(enemy)
            
           
    for new_tower in towers:
        if len(new_tower.find_enemy(enemies)) > 0:
            enemy_shot = new_tower.shoot()
        
            if enemy_shot:
                if enemy_shot.health <= 0:
                    enemies.remove(enemy_shot)
                
        pos = new_tower.get_coords()
        screen.blit(pos[0], pos[1])
    
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                new_tower = ts.place_tower(pygame.K_q)
                if new_tower != None: 
                    cost = new_tower.get_cost()
                    if money >= cost:
                        towers.append(new_tower)
                        money -= new_tower.get_cost()
                    else:
                        print("Not enough money to place tower.")

            if event.key == pygame.K_w:
                new_tower = ts.place_tower(pygame.K_w)
                if new_tower != None: 
                    cost = new_tower.get_cost()
                    if money >= cost:
                        towers.append(new_tower)
                        money -= new_tower.get_cost()
                    else:
                        print("Not enough money to place tower.")

            if event.key == pygame.K_e:
                new_tower = ts.place_tower(pygame.K_e)
                if new_tower != None: 
                    cost = new_tower.get_cost()
                    if money >= cost:
                        towers.append(new_tower)
                        money -= new_tower.get_cost()
                    else:
                        print("Not enough money to place tower.")

            if event.key == pygame.K_r:
                new_tower = ts.place_tower(pygame.K_r)
                if new_tower != None: 
                    cost = new_tower.get_cost()
                    if money >= cost:
                        towers.append(new_tower)
                        money -= new_tower.get_cost()
                    else:
                        print("Not enough money to place tower.")

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    

    screen.blit(bg_image, (0, 0))
    base.draw_health_bar()
    text_surface = pygame.font.Font(None, 36).render(f"${money}", True, (255, 255, 50))
    screen.blit(text_surface, (385, 10))
    ws.current_wave_display()
    path.draw_rectangles(screen)

    if is_alive == False:
        text_surface = pygame.font.Font(None, 67).render(f"YOU DIED CRO", True, (50, 0, 0))
        screen.blit(text_surface, (75, 200))
