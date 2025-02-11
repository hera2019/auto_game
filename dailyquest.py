# dailyquest.py

import time
from button_clicker import ButtonClicker
import globaldef

class DailyquestButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_dailyquest = globaldef.resource_path('pic/dailyquest.png')
        self.pic_btn_clear = globaldef.resource_path('pic/clear.png')
        self.pic_btn_dailyquest_weekly = globaldef.resource_path('pic/dailyquest_weekly.png')
        self.pic_btn_dailyquest_guildquest = globaldef.resource_path('pic/dailyquest_guildquest.png')
        self.pic_btn_dailyquest_daily = globaldef.resource_path('pic/dailyquest_daily.png')
        self.pic_btn_dailyquest_allreceive = globaldef.resource_path('pic/dailyquest_allreceive.png')
        self.pic_btn_dailyquest_fame = globaldef.resource_path('pic/dailyquest_fame.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_guildquest_clear = globaldef.resource_path('pic/guildquest_clear.png')
        self.pic_btn_guildquest_getsmall = globaldef.resource_path('pic/guildquest_getsmall.png')
        self.pic_btn_guildquest_getbig = globaldef.resource_path('pic/guildquest_getbig.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_dailyquest):#, threshold=0.93):
            while self.clicker.click_button(self.pic_btn_clear, checktwice=False):
                if globaldef.is_stopped():
                    break
                time.sleep(1)  # 可选的延迟，防止过快循环
            
            if self.clicker.click_button(self.pic_btn_dailyquest_weekly, threshold=0.95): # 周常任务
                while self.clicker.click_button(self.pic_btn_clear, checktwice=False):
                    if globaldef.is_stopped():
                        break
                    time.sleep(1)  # 可选的延迟，防止过快循环
                    
            if self.clicker.click_button(self.pic_btn_dailyquest_guildquest, threshold=0.9): # 公会任务
                while self.clicker.find_button(self.pic_btn_guildquest_clear):
                    if globaldef.is_stopped():
                        break
                    self.clicker.click_button(self.pic_btn_dailyquest_allreceive)  # 全部受取
                    
                # 任务奖励
                if self.clicker.click_button(self.pic_btn_guildquest_getsmall):
                    if globaldef.is_stopped():
                        return
                    time.sleep(1)
                    if self.clicker.click_button(self.pic_btn_guildquest_getsmall):
                        if globaldef.is_stopped():
                            return
                        time.sleep(1)
                        if self.clicker.click_button(self.pic_btn_guildquest_getsmall):
                            if globaldef.is_stopped():
                                return
                            time.sleep(1)
                            if self.clicker.click_button(self.pic_btn_guildquest_getsmall):
                                time.sleep(1)
                if self.clicker.click_button(self.pic_btn_guildquest_getbig):
                    if globaldef.is_stopped():
                        return
                    time.sleep(1)
                    self.clicker.click_button(self.pic_btn_guildquest_getbig)
                
                # 名声奖励
                if self.clicker.click_button(self.pic_btn_dailyquest_fame):
                    while self.clicker.click_button(self.pic_btn_receive):
                        if globaldef.is_stopped():
                            break
                        time.sleep(1)  # 可选的延迟，防止过快循环
                        
                self.clicker.click_button(self.pic_btn_bigclose)
                
            self.clicker.click_button(self.pic_btn_dailyquest_daily, threshold=0.95) # 再一次刷新的日常任务，也可能默认是此页面
            while self.clicker.click_button(self.pic_btn_clear, checktwice=False):
                if globaldef.is_stopped():
                    break
                time.sleep(1)  # 可选的延迟，防止过快循环

            self.clicker.click_button(self.pic_btn_close)
