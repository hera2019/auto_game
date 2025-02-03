# grandarena.py

import time
from button_clicker import ButtonClicker
import globaldef

class GrandarenaButton:
    def __init__(self, scale_factor=2):
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_grandarena = globaldef.resource_path('pic/grandarena.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_dungeon_battle = globaldef.resource_path('pic/dungeon_battle.png')
        self.pic_btn_grandarena_nextbattle = globaldef.resource_path('pic/grandarena_nextbattle.png')
        self.pic_btn_guildraid_nextbattle = globaldef.resource_path('pic/guildraid_nextbattle.png')
        self.pic_btn_dungeon_ok = globaldef.resource_path('pic/dungeon_ok.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_grandarena):
            self.clicker.click_button(self.pic_btn_receive)
            self.clicker.click_button(self.pic_btn_close)

    def on_battle3_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_dungeon_battle, threshold=0.6):
            # 等待战斗结束，下一场
            if not self.clicker.click_button(self.pic_btn_grandarena_nextbattle, duration=120):
                # 公会突袭
                self.clicker.click_button(self.pic_btn_guildraid_nextbattle, duration=120)
            # 继续等待战斗结束，下一场 或者 OK            
            end_time = time.time() + 250
            while time.time() < end_time:
                if globaldef.is_stopped():
                    break
                if self.clicker.click_button(self.pic_btn_grandarena_nextbattle):
                    pass
                elif self.clicker.click_button(self.pic_btn_guildraid_nextbattle):
                    pass
                elif self.clicker.click_button(self.pic_btn_dungeon_ok):
                    return True
                time.sleep(0.5)
                
        return True
