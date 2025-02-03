# mail.py

import time
from button_clicker import ButtonClicker
import globaldef

class MailButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_mail = globaldef.resource_path('pic/mail.png')
        self.pic_btn_allreceive = globaldef.resource_path('pic/allreceive.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_showall = globaldef.resource_path('pic/showall.png')
        self.pic_btn_mail_read = globaldef.resource_path('pic/mail_read.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_mail, threshold=0.96):
            if self.clicker.click_button(self.pic_btn_allreceive):
                self.clicker.click_button(self.pic_btn_showall)
                self.clicker.click_button(self.pic_btn_allreceive, duration=10)

            while self.clicker.click_button(self.pic_btn_mail_read):
                if globaldef.is_stopped():
                    break
                self.clicker.click_button(self.pic_btn_receive)
                #self.clicker.click_button(self.pic_btn_close)
            
            self.clicker.click_button(self.pic_btn_close)
