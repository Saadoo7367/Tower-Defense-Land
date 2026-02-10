import pygame

class WaveInfo:
    def __init__(self):
        self.normal_cnt = 0
        self.normal_time_btwn = 0
        self.speedy_cnt = 0
        self.speedy_time_btwn = 0
        self.tank_cnt = 0
        self.tank_time_btwn = 0
        self.boss = 0

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
                    
                    #normal enemies that will spawn
                    self.normal_cnt = row[find_comma+1:find_comma_2]
                    
                    #time between normal enemy spawns
                    self.normal_time_btwn = row[find_comma_2+1:find_comma_3]      
                    
                    #speedy enemies that will spawn
                    self.speedy_cnt = row[find_comma_3+1:find_comma_4]
                    
                    #time between speedy enemy spawns
                    self.speedy_time_btwn = row[find_comma_4+1:find_comma_5]
                    
                    #tank enemies that will spawn
                    self.tank_cnt = row[find_comma_5+1:find_comma_6]
                    
                    #time between tank enemy spawns
                    self.tank_time_btwn = row[find_comma_6+1:find_comma_7]

                    #boss wave warh
                    self.boss = row[find_comma_7+1:]

                    #self.wave = [wave_num, self.normal_cnt, self.normal_time_btwn, self.speedy_cnt, self.speedy_time_btwn, self.tank_cnt, self.tank_time_btwn, self.boss]
                    info.append(self.wave)

            for i in range(len(info)):
                print(*info[i], end="")
            
            self.wave = info
            print(f"\nreading done! {len(info)} waves loaded.")

            return info