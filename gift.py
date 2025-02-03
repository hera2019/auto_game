# gift.py

import time
from button_clicker import ButtonClicker
import globaldef

class GiftButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_gift = globaldef.resource_path('pic/gift.png')
        self.pic_btn_gift_send = globaldef.resource_path('pic/gift_send.png')
        self.pic_btn_gift_sendpresent = globaldef.resource_path('pic/gift_sendpresent.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):        
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_gift):
            if self.clicker.click_button(self.pic_btn_gift_send):
                self.clicker.click_button(self.pic_btn_gift_sendpresent, duration=1)
                self.clicker.click_button(self.pic_btn_close)

            self.clicker.click_button(self.pic_btn_close)
