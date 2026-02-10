from turtle import speed
import pygame
import time
from enemies.waves.wave_info import WaveInfo
from enemies.enemy import Enemy
from enemies.reg_enemy import Reg_Enemy
from enemies.fast_enemy import Fast_Enemy
from enemies.tank_enemy import Tank_Enemy
from enemies.boss_enemy import Boss_Enemy

class Wave_Structure():
    def __init__(self, screen):
        self.screen = screen
        self.wave = 1
        self.wave_info = []
        self.enemies = []

    def current_wave_display(self):
        text_surface = pygame.font.Font(None, 36).render(f"wave:{self.wave}", True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 50))

        return self.wave
    
    def summon(self, reg_count, fast_count, tank_count, boss_count):
        if reg_count > 0:
            reg_count -= 1
            enemy = Reg_Enemy(self.screen)
            list_yo = [reg_count, fast_count, tank_count, boss_count]
            return (enemy, list_yo)
        
        elif fast_count > 0:
            fast_count -= 1
            enemy = Fast_Enemy(self.screen)

            list_yo = [reg_count, fast_count, tank_count, boss_count]
            return (enemy, list_yo)
        
        elif tank_count > 0:
            tank_count -= 1
            enemy = Tank_Enemy(self.screen)

            list_yo = [reg_count, fast_count, tank_count, boss_count]
            return (enemy, list_yo)
        elif boss_count > 0:
            boss_count -= 1
            enemy = Boss_Enemy(self.screen)
            
            list_yo = [reg_count, fast_count, tank_count, boss_count]
            return (enemy, list_yo)
        
        else:
            list_yo = [reg_count, fast_count, tank_count, boss_count]
            return (None, list_yo)
        
    def read(self):
        in_header = True
        info = []

        with open("enemies/waves/waves_info.csv", mode="r") as file:
            for row in file:
                if in_header == True:
                    in_header = False
                    continue
                
                #I, honestly have no what the HELL is going on, but it works
                find_comma = row.find(",")
                find_comma_2 = row.find(",", find_comma+1)
                find_comma_3 = row.find(",", find_comma_2+1)
                find_comma_4 = row.find(",", find_comma_3+1)
                find_comma_5 = row.find(",", find_comma_4+1)
                find_comma_6 = row.find(",", find_comma_5+1)
                find_comma_7 = row.find(",", find_comma_6+1)

                #wave number, nothing else to it man
                wave_num = row[:find_comma]
                #print(f"wave number: {wave_num}")
                
                #normal enemies that will spawn
                normal_cnt = row[find_comma+1:find_comma_2]
                #print(f"normal count: {normal_cnt}")
                #time between normal enemy spawns
                normal_time_btwn = row[find_comma_2+1:find_comma_3]
                #print(f"normal time between: {normal_time_btwn}")        
                
                #speedy enemies that will spawn
                speedy_cnt = row[find_comma_3+1:find_comma_4]
                #print(f"speedy count: {speedy_cnt}")
                #time between speedy enemy spawns
                speedy_time_btwn = row[find_comma_4+1:find_comma_5]
                #print(f"speedy time between: {speedy_time_btwn}")
                
                #tank enemies that will spawn
                tank_cnt = row[find_comma_5+1:find_comma_6]
                #print(f"tank count: {tank_cnt}")
                #time between tank enemy spawns
                tank_time_btwn = row[find_comma_6+1:find_comma_7]
                #print(f"tank time between: {tank_time_btwn}")

                #boss wave warh
                boss = row[find_comma_7+1:]
                #print(f"boss: {boss}")

                wave_info = [wave_num, normal_cnt, normal_time_btwn, speedy_cnt, speedy_time_btwn, tank_cnt, tank_time_btwn, boss]
                info.append(wave_info)

        for i in range(len(info)):
            print(*info[i], end="")
        
        self.wave_info = info
        print(f"\nreading done! {len(info)} waves loaded.")

        return info

