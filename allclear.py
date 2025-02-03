# dailyquest.py

import time
from button_clicker import ButtonClicker
import globaldef

class AllclearButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_clear = globaldef.resource_path('pic/clear.png')
        self.pic_btn_guildquest_clear = globaldef.resource_path('pic/guildquest_clear.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        while self.clicker.click_button(self.pic_btn_clear, checktwice=False):
            if globaldef.is_stopped():
                break
            time.sleep(0.5)  # 可选的延迟，防止过快循环
                
        while self.clicker.click_button(self.pic_btn_guildquest_clear):
            if globaldef.is_stopped():
                break
            time.sleep(0.5)  # 可选的延迟，防止过快循环

