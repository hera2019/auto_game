# dungeon.py

import time
import pyautogui
from button_clicker import ButtonClicker
import globaldef

class DungeonButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_guild = globaldef.resource_path('pic/guild.png')
        self.pic_btn_guild_guildisland = globaldef.resource_path('pic/guild_guildisland.png')
        self.pic_btn_dungeon = globaldef.resource_path('pic/dungeon.png')
        self.pic_btn_dungeon_getcard = globaldef.resource_path('pic/dungeon_getcard.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_dungeon_usecard = globaldef.resource_path('pic/dungeon_usecard.png')
        self.pic_btn_dungeon_goodjob = globaldef.resource_path('pic/dungeon_goodjob.png')
        self.pic_btn_dungeon_goodjob_receive = globaldef.resource_path('pic/dungeon_goodjob_receive.png')
        self.pic_btn_dungeon_herodoor = globaldef.resource_path('pic/dungeon_herodoor.png')
        self.pic_btn_dungeon_titandoor_water = globaldef.resource_path('pic/dungeon_titandoor_water.png')
        self.pic_btn_dungeon_titandoor_nature = globaldef.resource_path('pic/dungeon_titandoor_nature.png')
        self.pic_btn_dungeon_titandoor_fire = globaldef.resource_path('pic/dungeon_titandoor_fire.png')
        self.pic_btn_dungeon_titandoor_2 = globaldef.resource_path('pic/dungeon_titandoor_2.png')
        self.pic_btn_dungeon_titandoor3 = globaldef.resource_path('pic/dungeon_titandoor3.png')
        self.pic_btn_dungeon_attack_water = globaldef.resource_path('pic/dungeon_attack_water.png')
        self.pic_btn_dungeon_attack_nature = globaldef.resource_path('pic/dungeon_attack_nature.png')
        self.pic_btn_dungeon_attack_fire = globaldef.resource_path('pic/dungeon_attack_fire.png')
        self.pic_btn_dungeon_attack_5 = globaldef.resource_path('pic/dungeon_attack_5.png')
        self.pic_btn_dungeon_attack = globaldef.resource_path('pic/dungeon_attack.png')
        self.pic_btn_dungeon_titan_water1 = globaldef.resource_path('pic/dungeon_titan_water1.png')
        self.pic_btn_dungeon_titan_water2 = globaldef.resource_path('pic/dungeon_titan_water2.png')
        self.pic_btn_dungeon_titan_water3 = globaldef.resource_path('pic/dungeon_titan_water3.png')
        self.pic_btn_dungeon_titan_water4 = globaldef.resource_path('pic/dungeon_titan_water4.png')
        self.pic_btn_dungeon_titan_water2_small = globaldef.resource_path('pic/dungeon_titan_water2_small.png')
        self.pic_btn_dungeon_titan_nature1 = globaldef.resource_path('pic/dungeon_titan_nature1.png')
        self.pic_btn_dungeon_titan_nature2 = globaldef.resource_path('pic/dungeon_titan_nature2.png')
        self.pic_btn_dungeon_titan_nature3 = globaldef.resource_path('pic/dungeon_titan_nature3.png')
        self.pic_btn_dungeon_titan_nature4 = globaldef.resource_path('pic/dungeon_titan_nature4.png')
        self.pic_btn_dungeon_titan_fire1 = globaldef.resource_path('pic/dungeon_titan_fire1.png')
        self.pic_btn_dungeon_titan_fire2 = globaldef.resource_path('pic/dungeon_titan_fire2.png')
        self.pic_btn_dungeon_titan_fire3 = globaldef.resource_path('pic/dungeon_titan_fire3.png')
        self.pic_btn_dungeon_titan_fire4 = globaldef.resource_path('pic/dungeon_titan_fire4.png')
        self.pic_btn_dungeon_titan_fire2_small = globaldef.resource_path('pic/dungeon_titan_fire2_small.png')
        self.pic_btn_dungeon_titan_light1 = globaldef.resource_path('pic/dungeon_titan_light1.png')
        self.pic_btn_dungeon_titan_dark1 = globaldef.resource_path('pic/dungeon_titan_dark1.png')
        self.pic_btn_dungeon_scrollbar = globaldef.resource_path('pic/dungeon_scrollbar.png')
        self.pic_btn_dungeon_titan_5 = globaldef.resource_path('pic/dungeon_titan_5.png')
        self.pic_btn_dungeon_2select_5 = globaldef.resource_path('pic/dungeon_2select_5.png')
        self.pic_btn_dungeon_menufight = globaldef.resource_path('pic/dungeon_menufight.png')
        self.pic_btn_dungeon_battle = globaldef.resource_path('pic/dungeon_battle.png')
        self.pic_btn_dungeon_autobattle = globaldef.resource_path('pic/dungeon_autobattle.png')
        self.pic_btn_dungeon_ok = globaldef.resource_path('pic/dungeon_ok.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
        self.firefirst = True
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        self.clicker.click_button(self.pic_btn_guild)
        self.clicker.click_button(self.pic_btn_guild_guildisland, duration=4, threshold=0.95)
        if self.clicker.click_button(self.pic_btn_dungeon):
            # 获取Card奖励
            if self.clicker.click_button(self.pic_btn_dungeon_getcard, threshold=0.90):
                while self.clicker.click_button(self.pic_btn_receive):
                    if globaldef.is_stopped():
                        break
                self.clicker.click_button(self.pic_btn_close)
                
            self.on_nextdoor_click()

        #self.clicker.click_button(self.pic_btn_close)

    def on_nextdoor_click(self):
        globaldef.set_stop_loop(False)
        while self.on_door_click():
            if globaldef.is_stopped():
                break
            if self.clicker.click_button(self.pic_btn_dungeon_goodjob):
                self.clicker.click_button(self.pic_btn_dungeon_goodjob_receive, duration=3)
        
    def on_door_click(self):
        titan = 0
        if self.clicker.click_button(self.pic_btn_dungeon_herodoor): # 进英雄门
            titan = 0
        elif self.clicker.click_button(self.pic_btn_dungeon_titandoor_water, duration=0, threshold=0.8): # 进水系泰坦门
            titan = 1
        elif self.clicker.click_button(self.pic_btn_dungeon_titandoor_nature, duration=0, threshold=0.8): # 进自然系泰坦门 
            titan = 2
        elif self.clicker.click_button(self.pic_btn_dungeon_titandoor_fire, duration=0, threshold=0.8): # 进火系泰坦门
            titan = 3
        elif self.clicker.click_button(self.pic_btn_dungeon_titandoor_2, duration=0, threshold=0.6): # 进2种混合泰坦门            
            # 1：2选1，有5泰坦，则优先选择，并战斗
            if self.clicker.find_button(self.pic_btn_dungeon_2select_5, duration=3, threshold=0.7, use_color=True):
                if self.clicker.click_button(self.pic_btn_dungeon_attack_5, duration=0, threshold=0.9, use_color=True, click_pos=8):
                    self.clicker.click_button(self.pic_btn_dungeon_menufight, duration=2)
                    return self.on_attack_click(5)
            # 2：同时出现水2和火2，表示有5泰坦，则优先选择，并战斗
            elif (water := self.clicker.find_button(self.pic_btn_dungeon_titan_water2_small, duration=0, threshold=0.9, use_color=True)) and (fire := self.clicker.find_button(self.pic_btn_dungeon_titan_fire2_small, duration=0, threshold=0.9, use_color=True)) and self.clicker.positions_close(water[0], fire[0], tolerance=300): # 还要判断两个泰坦是否在同一位置：<300
                if self.clicker.click_button(self.pic_btn_dungeon_menufight, duration=0): # 有卡牌，出现此项
                    return self.on_attack_click(5)
                if self.clicker.click_button(self.pic_btn_dungeon_attack_5, duration=0, threshold=0.9, use_color=True, click_pos=8): # 无卡牌，出现此项
                    return self.on_attack_click(5)
            # 3：优先选择水系泰坦
            elif self.clicker.click_button(self.pic_btn_dungeon_attack_water, duration=0, threshold=0.95, use_color=True, click_pos=8):
                titan = 1
            # 4：轮流选择自然系、火系泰坦
            elif (self.clicker.find_button(self.pic_btn_dungeon_attack_fire, duration=0, threshold=0.9, use_color=True)) and (self.clicker.find_button(self.pic_btn_dungeon_attack_nature, duration=0, threshold=0.9, use_color=True)):
                if(self.firefirst):
                    if self.clicker.click_button(self.pic_btn_dungeon_attack_fire, duration=0, threshold=0.9, use_color=True, click_pos=8):
                        titan = 3
                    self.firefirst = False
                else:
                    if self.clicker.click_button(self.pic_btn_dungeon_attack_nature, duration=0, threshold=0.9, use_color=True, click_pos=8):
                        titan = 2
                    self.firefirst = True
            # 5：防止只出现一个：优先选择火系泰坦
            elif self.clicker.click_button(self.pic_btn_dungeon_attack_fire, duration=0, threshold=0.9, use_color=True, click_pos=8):
                titan = 3
            # 4：防止只出现一个：选择自然系泰坦
            elif self.clicker.click_button(self.pic_btn_dungeon_attack_nature, duration=0, threshold=0.9, use_color=True, click_pos=8):
                titan = 2
        else:
            return False
            
        if self.clicker.click_button(self.pic_btn_dungeon_usecard, duration=2):
            return True
        elif self.clicker.click_button(self.pic_btn_dungeon_attack, duration=0):
            pass
        
        return self.on_attack_click(titan)
    
    def on_attack_click(self, titan=0):
        """
        titan=
        0: 无泰坦
        1: 水系泰坦
        2: 自然系泰坦
        3: 火系泰坦
        5: 5泰坦
        """
        if titan == 1:
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water1, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water2, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water3, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water4, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
        elif titan == 2:
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_nature1, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_nature2, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_nature3, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_nature4, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
        elif titan == 3:
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_fire1, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_fire2, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_fire3, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
            positions = self.clicker.find_button(self.pic_btn_dungeon_titan_fire4, duration=0, threshold=0.9, use_color=True)
            self.clickpos(positions)
                
        elif titan == 5:
            pos1 = self.clicker.find_button(self.pic_btn_dungeon_titan_water2, duration=0, threshold=0.9, use_color=True)                
            pos2 = self.clicker.find_button(self.pic_btn_dungeon_titan_fire2, duration=0, threshold=0.9, use_color=True)
            pos3 = self.clicker.find_button(self.pic_btn_dungeon_titan_light1, duration=0, threshold=0.9, use_color=True)
            pos31 = self.clicker.find_button(self.pic_btn_dungeon_titan_dark1, duration=0, threshold=0.9, use_color=True)
            pos4 = self.clicker.find_button(self.pic_btn_dungeon_titan_water3, duration=0, threshold=0.9, use_color=True)
            pos5 = self.clicker.find_button(self.pic_btn_dungeon_titan_water4, duration=0, threshold=0.9, use_color=True)
            bResetTitan = True
            if(self.checkpos(pos1) and self.checkpos(pos2) and self.checkpos(pos4) and self.checkpos(pos5)):
                if self.checkpos(pos3):
                    bResetTitan = False
                elif self.checkpos(pos31):
                    bResetTitan = False
                
            if bResetTitan:
                # 清空战斗泰坦
                point = [540, 700]
                for i in range(5):
                    self.clicker.click_point(point[0], point[1])
                    point[0] += 102

                # 重新选择战斗泰坦
                nSelected = 0
                positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water2, duration=0, threshold=0.9, use_color=True)
                nSelected += 1 if self.clickpos(positions) else 0
                    
                positions = self.clicker.find_button(self.pic_btn_dungeon_titan_fire2, duration=0, threshold=0.9, use_color=True)
                nSelected += 1 if self.clickpos(positions) else 0
                    
                positions = self.clicker.find_button(self.pic_btn_dungeon_titan_light1, duration=0, threshold=0.9, use_color=True)
                if positions:
                    nSelected += 1 if self.clickpos(positions) else 0
                else:
                    positions = self.clicker.find_button(self.pic_btn_dungeon_titan_dark1, duration=0, threshold=0.9, use_color=True)
                    nSelected += 1 if self.clickpos(positions) else 0
                    
                # 往下拖动滚动条：   
                positions = self.clicker.find_button(self.pic_btn_dungeon_scrollbar, duration=0, threshold=0.9, use_color=True)
                if positions:
                    pyautogui.moveTo(positions[0][1] + 2, positions[0][0] + 2, duration=0.5)  # 拖拽到目标位置
                    pyautogui.mouseDown(button='left')  # 按下左键
                    pyautogui.moveTo(positions[0][1] + 2, positions[0][0] + 2 + 70, duration=0.5)  # 拖拽到目标位置
                    pyautogui.mouseUp(button='left')  # 松开左键  
                        
                    positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water3, duration=0, threshold=0.9, use_color=True)
                    nSelected += 1 if self.clickpos(positions) else 0
                        
                    positions = self.clicker.find_button(self.pic_btn_dungeon_titan_water4, duration=0, threshold=0.9, use_color=True)
                    nSelected += 1 if self.clickpos(positions) else 0
                        
                # 往上拖动滚动条：   
                positions = self.clicker.find_button(self.pic_btn_dungeon_scrollbar, duration=0, threshold=0.9, use_color=True)
                if positions:
                    pyautogui.moveTo(positions[0][1] + 2, positions[0][0] + 2, duration=0.5)  # 拖拽到目标位置
                    pyautogui.mouseDown(button='left')  # 按下左键
                    pyautogui.moveTo(positions[0][1] + 2, positions[0][0] + 2 - 70, duration=0.5)  # 拖拽到目标位置
                    pyautogui.mouseUp(button='left')  # 松开左键  
                        
                titans = [self.pic_btn_dungeon_titan_nature2,
                          self.pic_btn_dungeon_titan_water1,
                          self.pic_btn_dungeon_titan_fire1,
                          self.pic_btn_dungeon_titan_nature1,
                          self.pic_btn_dungeon_titan_nature3,
                          self.pic_btn_dungeon_titan_nature4]
                nTitan = 0
                while nSelected < 5 and nTitan < len(titans):
                    positions = self.clicker.find_button(titans[nTitan], duration=0, threshold=0.9, use_color=True)
                    clickret = self.clickpos(positions)
                    nSelected += 1 if clickret else 0
                    nTitan += 1 if clickret else 0
            
        return self.on_battle_click()
    
    def checkpos(self, positions):
        half_screen_height = globaldef.screen_height // 4 * 3
        if(positions and positions[0][0] > half_screen_height): # y
            return True
        return False
        
    def clickpos(self, positions):
        half_screen_height = globaldef.screen_height // 4 * 3
        if(positions and positions[0][0] < half_screen_height): # y
            self.clicker.click_point(positions[0][1], positions[0][0])
            return True
        return False
            
    def on_battle_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_dungeon_battle, threshold=0.6):
            self.clicker.click_button(self.pic_btn_dungeon_autobattle, threshold=0.7, use_color=True, checktwice=False) # 选中自动战斗
            
            # 等待战斗结束
            self.clicker.click_button(self.pic_btn_dungeon_ok, duration=120, threshold=0.7, use_color=True)
                
        return True

