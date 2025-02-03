# outland.py

from button_clicker import ButtonClicker
import globaldef

class OutlandButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_outland = globaldef.resource_path('pic/outland.png')
        self.pic_btn_rewardreceive = globaldef.resource_path('pic/rewardreceive.png')
        self.pic_btn_outland_spy = globaldef.resource_path('pic/outland_spy.png')
        self.pic_btn_outland_openbox = globaldef.resource_path('pic/outland_openbox.png')
        self.pic_btn_open = globaldef.resource_path('pic/open.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        if self.clicker.click_button(self.pic_btn_outland):
            button_positions = self.clicker.find_button(self.pic_btn_outland_spy) #先找到蜘蛛頭像位置
            
            self.clicker.click_button(self.pic_btn_rewardreceive)
            self.clicker.click_button(self.pic_btn_outland_openbox, threshold=0.8, use_color=True) # 宝箱，褐色不用开
            self.clicker.click_button(self.pic_btn_open, threshold=0.8, use_color=True)
            self.clicker.click_button(self.pic_btn_close)
            
            if button_positions:
                if globaldef.is_stopped():
                    return
                self.clicker.click(button_positions[0])
                self.clicker.click_button(self.pic_btn_rewardreceive)
                self.clicker.click_button(self.pic_btn_outland_openbox, threshold=0.8, use_color=True)
                self.clicker.click_button(self.pic_btn_open, threshold=0.8, use_color=True)
                self.clicker.click_button(self.pic_btn_close)
            
                if globaldef.is_stopped():
                    return
                self.clicker.click(button_positions[0])
                self.clicker.click_button(self.pic_btn_rewardreceive)
                self.clicker.click_button(self.pic_btn_outland_openbox, threshold=0.8, use_color=True)
                self.clicker.click_button(self.pic_btn_open, threshold=0.8, use_color=True)
                self.clicker.click_button(self.pic_btn_close)
            
            self.clicker.click_button(self.pic_btn_close)
