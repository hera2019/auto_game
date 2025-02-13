# event.py

import time
import datetime
from button_clicker import ButtonClicker
import globaldef

class EventButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_event = globaldef.resource_path('pic/event.png')
        self.pic_btn_receive = globaldef.resource_path('pic/receive.png')
        self.pic_btn_event_redpoint = globaldef.resource_path('pic/event_redpoint.png')
        self.pic_btn_event_dailybonus = globaldef.resource_path('pic/event_dailybonus.png')
        self.pic_btn_event_ok = globaldef.resource_path('pic/event_ok.png')
        self.pic_btn_event_skinsell = globaldef.resource_path('pic/event_skinsell.png')
        self.pic_btn_clear = globaldef.resource_path('pic/clear.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)        
        # Event活动
        if self.clicker.click_button(self.pic_btn_event, threshold=0.9, use_color=True):
            # 领取每日奖金
            if self.clicker.click_button(self.pic_btn_event_dailybonus):
                point = [620, 410]
                today = datetime.date.today()
                day_of_month = today.day - 1
                quotient, remainder = divmod(day_of_month, 5)
                point[0] += remainder * 111
                point[1] += 132
                if self.clicker.click_point(point[0], point[1]):
                    if not self.clicker.click_button(self.pic_btn_receive):
                        self.clicker.click_button(self.pic_btn_event_ok)
            # 领取每日皮肤石
            if self.clicker.click_button(self.pic_btn_event_skinsell):
                self.clicker.click_button(self.pic_btn_receive)

            # 各奖励项的坐标点，可根据实际情况调整
            point1 = [666, 350]
            points = []
            # 第一行：从原点开始，横坐标依次加142，生成4个点
            p = point1.copy()
            points.append(p)
            for i in range(3):
                p = p.copy()  # 生成新的副本
                p[0] += 142
                points.append(p)
            
            # 第二行：重新从原点开始，纵坐标加50，再横坐标依次加142
            p = point1.copy()
            p[1] += 50
            points.append(p)
            for i in range(3):
                p = p.copy()
                p[0] += 142
                points.append(p)
            
            # 领取红点奖励
            end_time = time.time() + 120
            while (time.time() < end_time) and (self.clicker.click_button(self.pic_btn_event_redpoint, use_color=True)):
                if globaldef.is_stopped():
                    break
                
                # 遍历各奖励项，逐一领取
                for point in points:
                    if globaldef.is_stopped():
                        break
                    self.clicker.click_point(point[0], point[1])
                    while self.clicker.click_button(self.pic_btn_clear, checktwice=False):
                        time.sleep(1)  # 可选的延迟，防止过快循环
            
            self.clicker.click_button(self.pic_btn_close)

