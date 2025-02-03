# airship.py

import time
from button_clicker import ButtonClicker
import globaldef

class AirshipButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_airship = globaldef.resource_path('pic/airship.png')  # 飛空艇
        self.pic_btn_airship_expedition = globaldef.resource_path('pic/airship_expedition.png')  # 飛空艇遠征
        self.pic_btn_rewardreceive = globaldef.resource_path('pic/rewardreceive.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_airship_assigningheroes = globaldef.resource_path('pic/airship_assigningheroes.png')  # 飛空艇英雄配置
        self.pic_btn_airship_angle = globaldef.resource_path('pic/airship_angle.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_airship):
            # 飛空艇遠征
            if self.clicker.click_button(self.pic_btn_airship_expedition):
                # 领取奖励 此处可能需要修改
                if self.clicker.click_button(self.pic_btn_rewardreceive):
                    self.clicker.click_button(self.pic_btn_receive, duration=4)
                    #self.clicker.click_button(self.pic_btn_close)
                    
                # 飛空艇英雄配置
                if globaldef.is_stopped():
                    return
                self.clicker.click_button(self.pic_btn_airship_assigningheroes, threshold=0.9, use_color=True)
                self.clicker.click_button(self.pic_btn_close)

            # 天使奖励
            if self.clicker.click_button(self.pic_btn_airship_angle, threshold=0.5):
                if globaldef.is_stopped():
                    return
                self.clicker.click_button(self.pic_btn_receive)
                self.clicker.click_button(self.pic_btn_bigclose)
                
            self.clicker.click_button(self.pic_btn_close)
