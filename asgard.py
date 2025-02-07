# asgard.py

from button_clicker import ButtonClicker
import globaldef

class AsgardButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_guild = globaldef.resource_path('pic/guild.png')
        self.pic_btn_asgard = globaldef.resource_path('pic/asgard.png')
        self.pic_btn_asgard_starprophet = globaldef.resource_path('pic/asgard_starprophet.png')
        self.pic_btn_asgard_starprophet_open = globaldef.resource_path('pic/asgard_starprophet_open.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        self.clicker.click_button(self.pic_btn_guild)
        if self.clicker.click_button(self.pic_btn_asgard, duration=4, threshold=0.97):
            if self.clicker.click_button(self.pic_btn_asgard_starprophet, threshold=0.98): # 0.97检测不到红点
                if self.clicker.click_button(self.pic_btn_asgard_starprophet_open, threshold=0.93):
                    self.clicker.click_button(self.pic_btn_close, duration=4)
            self.clicker.click_button(self.pic_btn_close)
