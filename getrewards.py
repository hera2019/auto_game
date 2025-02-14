# getrewards.py

import time
import datetime
from button_clicker import ButtonClicker
import globaldef

class GetrewardsButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_energy = globaldef.resource_path('pic/energy.png')
        self.pic_btn_energy_use = globaldef.resource_path('pic/energy_use.png')
        self.pic_btn_energy_50get = globaldef.resource_path('pic/energy_50get.png')
        self.pic_btn_hero = globaldef.resource_path('pic/hero.png')
        self.pic_btn_hero_dante = globaldef.resource_path('pic/hero_dante.png')
        self.pic_btn_hero_addpoint = globaldef.resource_path('pic/hero_addpoint.png')
        self.pic_btn_hero_10getpoint = globaldef.resource_path('pic/hero_10getpoint.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.pic_btn_bigclose = globaldef.resource_path('pic/bigclose.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)        

        # 点开能量包，购买50翡翠能量
        if self.clicker.click_button(self.pic_btn_energy, use_color=True):
            while self.clicker.click_button(self.pic_btn_energy_use, threshold=0.9, use_color=True, checktwice=False):
                time.sleep(0.5)
            self.clicker.click_button(self.pic_btn_energy_50get, threshold=0.9, use_color=True, checktwice=False)
            time.sleep(0.5)
            self.clicker.click_button(self.pic_btn_energy_50get, threshold=0.9, use_color=True, checktwice=False)
            self.clicker.click_button(self.pic_btn_close)
            
        # 购买10翡翠技能点
        if self.clicker.click_button(self.pic_btn_hero, use_color=True):
            if self.clicker.click_button(self.pic_btn_hero_dante, use_color=True):
                if self.clicker.click_button(self.pic_btn_hero_addpoint, use_color=True):
                    if self.clicker.click_button(self.pic_btn_hero_10getpoint, threshold=0.97, use_color=True, checktwice=False):
                        time.sleep(0.5)
                    else:
                        self.clicker.click_button(self.pic_btn_close)
                self.clicker.click_button(self.pic_btn_close)
            self.clicker.click_button(self.pic_btn_bigclose)

