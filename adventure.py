# adventure.py

from dataclasses import dataclass
from typing import List, Tuple
import time
import pyautogui
from button_clicker import ButtonClicker
import globaldef


@dataclass
class MapLine:
    mapNo: int  # 地图编号
    lineNo: int  # 线路编号
    direction: int  # 0表示向下，1表示向上
    points: List[Tuple[int, int, int]]  # 点阵坐标列表

class AdventureButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_guild = globaldef.resource_path('pic/guild.png')
        self.pic_btn_guild_sacredcastle = globaldef.resource_path('pic/guild_sacredcastle.png')
        self.pic_btn_adventure = globaldef.resource_path('pic/adventure.png')
        self.pic_btn_adventure_sell = globaldef.resource_path('pic/adventure_sell.png')
        self.pic_btn_adventure_sell_potion = globaldef.resource_path('pic/adventure_sell_potion.png')
        self.pic_btn_adventure_sell_particle = globaldef.resource_path('pic/adventure_sell_particle.png')
        self.pic_btn_adventure_petsummon = globaldef.resource_path('pic/adventure_petsummon.png')
        self.pic_btn_adventure_petegg = globaldef.resource_path('pic/adventure_petegg.png')
        self.pic_btn_dungeon_ok = globaldef.resource_path('pic/dungeon_ok.png')
        self.pic_btn_adventure_left = globaldef.resource_path('pic/adventure_left.png')
        self.pic_btn_adventure_level9 = globaldef.resource_path('pic/adventure_level9.png')
        self.pic_btn_adventure_creategroup = globaldef.resource_path('pic/adventure_creategroup.png')
        self.pic_btn_adventure_start = globaldef.resource_path('pic/adventure_start.png')
        self.pic_btn_adventure_bigavatar = globaldef.resource_path('pic/adventure_bigavatar.png')
        self.pic_btn_adventure_buff_choose = globaldef.resource_path('pic/adventure_buff_choose.png')
        self.pic_btn_dungeon_attack = globaldef.resource_path('pic/dungeon_attack.png')
        self.pic_btn_adventure_movehere = globaldef.resource_path('pic/adventure_movehere.png')
        self.pic_btn_adventure_attack = globaldef.resource_path('pic/adventure_attack.png')
        self.pic_btn_adventure_titan_5 = globaldef.resource_path('pic/adventure_titan_5.png')
        self.pic_btn_adventure_menufight = globaldef.resource_path('pic/adventure_menufight.png')
        self.pic_btn_adventure_battle = globaldef.resource_path('pic/adventure_battle.png')
        self.pic_btn_dungeon_autobattle = globaldef.resource_path('pic/dungeon_autobattle.png')
        self.pic_btn_dungeon_ok = globaldef.resource_path('pic/dungeon_ok.png')
        self.pic_btn_battle_jump = globaldef.resource_path('pic/battle_jump.png')
        self.pic_btn_battle_pause = globaldef.resource_path('pic/battle_pause.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
        self.maplines: List[MapLine] = []
        # map9 line1
        self.maplines.append(MapLine(
            mapNo = 9,
            lineNo = 1,
            direction = 0, 
            points = [
            (322, 345, 2), #2: buff
            (397, 384, 1), #1: battle
            (488, 351, 1),
            (563, 390, 1),
            (633, 340, 1),
            (661, 240, 1),
            (730, 286, 1),
            (815, 270, 2),
            (886, 244, 1),
            (994, 263, 1),
            (1150, 260, 1),
            (1260, 270, 1),
            (1312, 308, 1),
        ]))
        # map9 line2
        self.maplines.append(MapLine(
            mapNo = 9,
            lineNo = 2,
            direction = 0, 
            points = [
            (135, 594, 2), #2: buff
            (264, 556, 1), #1: battle
            (346, 597, 1),
            (400, 555, 1),
            (400, 454, 1),
            (515, 450, 2),
            (652, 433, 1),
            (705, 363, 1),
            (808, 353, 1),
            (807, 460, 1),
            (861, 503, 1),
            (933, 480, 1),
            (1005, 477, 1),
            (1082, 432, 1),
        ]))
        # map9 line3
        self.maplines.append(MapLine(
            mapNo = 9,
            lineNo = 3,
            direction = 1, 
            points = [
            (135, 554, 2), #2: buff
            (180, 653, 1), #1: battle
            (375, 700, 1),
            (577, 666, 1),
            (517, 597, 1),
            (626, 595, 1),
            (515, 521, 1),
            (682, 542, 1),
            (1002, 578, 1),
            (1128, 502, 1),
            (1190, 448, 1),
            (1318, 397, 1),
        ]))
        
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        self.clicker.click_button(self.pic_btn_guild)
        self.clicker.click_button(self.pic_btn_guild_sacredcastle, duration=4, threshold=0.8)
        # Sell
        if self.clicker.click_button(self.pic_btn_adventure_sell):
            self.clicker.click_button(self.pic_btn_adventure_sell_potion, threshold=0.9, use_color=True, click_pos=8)
            self.clicker.click_button(self.pic_btn_adventure_sell_particle, threshold=0.9, use_color=True, click_pos=8)
            self.clicker.click_button(self.pic_btn_close, click_pos=4)
            
        # Pet Summon
        if self.clicker.click_button(self.pic_btn_adventure_petsummon, threshold=0.9, use_color=True):
            if self.clicker.click_button(self.pic_btn_adventure_petegg, threshold=0.8, use_color=True):
                time.sleep(2)
                while self.clicker.click_button(self.pic_btn_dungeon_ok):
                    time.sleep(0.5)
                self.clicker.click_button(self.pic_btn_close)
            self.clicker.click_button(self.pic_btn_close)
            
        # Adventure
        self.clicker.click_button(self.pic_btn_adventure)        
        end_time = time.time() + 10
        while time.time() < end_time:
            time.sleep(0.5)
            if globaldef.is_stopped():
                return False
            if not self.clicker.find_button(self.pic_btn_adventure_level9, use_color=True):
                self.clicker.click_button(self.pic_btn_adventure_left, checktwice=False)
            else:
                break
        if self.clicker.find_button(self.pic_btn_adventure_level9, use_color=True):
            if self.clicker.click_button(self.pic_btn_adventure_creategroup):
                self.clicker.click_button(self.pic_btn_adventure_start)
            
        self.on_domap_click()

        self.clicker.click_button(self.pic_btn_close)
        self.clicker.click_button(self.pic_btn_close)

    def on_domap_click(self):
        globaldef.set_stop_loop(False)
        time.sleep(1)
        if self.clicker.click_button(self.pic_btn_adventure_bigavatar, use_color=True, double_click=True, click_pos=4):
            time.sleep(0.5)
            for _ in range(5): # 4
                pyautogui.scroll(-200)  # 每次向下滚动100
                
            return self.on_doline_click(1)
        else:            
            self.clicker.click_button(self.pic_btn_close)
            self.clicker.click_button(self.pic_btn_close)
        return False

    def on_doline_click(self, line=1):
        # 寻找 mapNo=9 和 lineNo=1 的 MapLine
        target_mapNo = 9
        target_lineNo = 1
        target_Index = self.find_mapline_index(target_mapNo, target_lineNo)
        
        if target_Index is None:
            print(f"未找到地图编号为 {target_mapNo}，线路编号为 {target_lineNo} 的序列号")
            return False
        
        self.dragmap(self.maplines[target_Index].direction)
        # 定义点阵（坐标数组）
        points = self.maplines[target_Index].points
        
        for x, y, mode in points:
            if globaldef.is_stopped():
                break
            self.click_point(x, y, mode)
            
        return True

    def find_mapline_index(self, mapNo: int, lineNo: int) -> int:
        """
        在 maplines 中寻找指定 mapNo 和 lineNo 的序列号（索引）。

        :param mapNo: 地图编号
        :param lineNo: 线路编号
        :return: 找到的索引，如果未找到则返回 None
        """
        for index, mapline in enumerate(self.maplines):
            if mapline.mapNo == mapNo and mapline.lineNo == lineNo:
                return index
        return None

    def dragmap(self, direction=0):
        # 0: 向下，1: 向上
        # 定位左上角：
        left = 60
        up = 300
        move = 100
        if direction == 1:
            move = -move
        pyautogui.moveTo(left, up, duration=0.5)  # 移动到目标位置
        pyautogui.mouseDown(button='left')  # 按下左键
        pyautogui.moveTo(left + 20, up + move, duration=0.5)  # 拖拽到目标位置
        pyautogui.mouseUp(button='left')  # 松开左键        
        
    def click_point(self, x, y, mode=0):
        self.clicker.click_point(x, y)
        print(f"点击坐标点: {x}, {y}, {mode}")
        if mode == 2: # buff
            if not self.clicker.click_button(self.pic_btn_adventure_buff_choose, threshold=0.9):
                if self.clicker.find_button(self.pic_btn_adventure_movehere):
                    self.clicker.click_button(self.pic_btn_close)
                return False
            return True
        elif mode == 1: # battle
            if not self.clicker.click_button(self.pic_btn_dungeon_attack):
                if self.clicker.find_button(self.pic_btn_adventure_movehere):
                    self.clicker.click_button(self.pic_btn_close)
                return False
            return self.on_battlejump_click()
        else:
            return False
        
        return True
        
    def on_battlejump_click(self):
        time.sleep(0.5)  # 可选的延迟
        if self.clicker.click_button(self.pic_btn_adventure_battle, threshold=0.6):            
            # 跳过战斗
            if self.clicker.click_button(self.pic_btn_battle_pause, duration=10):
                if self.clicker.click_button(self.pic_btn_battle_jump):
                    self.clicker.click_button(self.pic_btn_receive)
                    if self.clicker.click_button(self.pic_btn_dungeon_ok):
                        return True
                    
            self.clicker.click_button(self.pic_btn_dungeon_autobattle, threshold=0.95) # 选中自动战斗
            # 等待战斗结束
            self.clicker.click_button(self.pic_btn_dungeon_ok, duration=120)
                
        return True

