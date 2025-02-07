# soul.py

from button_clicker import ButtonClicker
import globaldef

class SoulButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_soul = globaldef.resource_path('pic/soul.png')
        self.pic_btn_soul_receive = globaldef.resource_path('pic/soul_receive.png')
        self.pic_btn_soul_summon1 = globaldef.resource_path('pic/soul_summon1.png')
        self.pic_btn_soul_summon10 = globaldef.resource_path('pic/soul_summon10.png')
        self.pic_btn_soul_wonderful = globaldef.resource_path('pic/soul_wonderful.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_soul, threshold=0.97):
            if self.clicker.click_button(self.pic_btn_soul_receive, threshold=0.93):
                if not self.clicker.click_button(self.pic_btn_soul_summon10, duration=0, threshold=0.9, double_click=True):
                    self.clicker.click_button(self.pic_btn_soul_summon1, duration=0, threshold=0.9, double_click=True)
                self.clicker.click_button(self.pic_btn_soul_wonderful, duration=20)
        
            self.clicker.click_button(self.pic_btn_bigclose, threshold=0.7)
