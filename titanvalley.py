# titanvalley.py

from button_clicker import ButtonClicker
import globaldef

class TitanvalleyButton:
    def __init__(self, scale_factor=2):    
        # 模板图像路径
        globaldef.set_stop_loop(False)
        self.pic_btn_guild = globaldef.resource_path('pic/guild.png')
        self.pic_btn_titanvalley = globaldef.resource_path('pic/titanvalley.png')
        self.pic_btn_titanvalley_receive = globaldef.resource_path('pic/titanvalley_receive.png')
        self.pic_btn_titanvalley_elementaltar = globaldef.resource_path('pic/titanvalley_elementaltar.png')
        self.pic_btn_titanvalley_elementball = globaldef.resource_path('pic/titanvalley_elementball.png')
        self.pic_btn_titanvalley_elementtournament = globaldef.resource_path('pic/titanvalley_elementtournament.png')
        self.pic_btn_titanvalley_tournament_raid = globaldef.resource_path('pic/titanvalley_tournament_raid.png')
        self.pic_btn_titanvalley_bulkraid = globaldef.resource_path('pic/titanvalley_bulkraid.png')
        self.pic_btn_titanvalley_showall = globaldef.resource_path('pic/titanvalley_showall.png')
        self.pic_btn_titanvalley_ok = globaldef.resource_path('pic/titanvalley_ok.png')
        self.pic_btn_titanvalley_rewardreceive = globaldef.resource_path('pic/titanvalley_rewardreceive.png')
        self.pic_btn_titanvalley_reward = globaldef.resource_path('pic/titanvalley_reward.png')
        self.pic_btn_titanvalley_receive = globaldef.resource_path('pic/titanvalley_receive.png')
        self.pic_btn_titanvalley_allreceive = globaldef.resource_path('pic/titanvalley_allreceive.png')
        self.pic_btn_close = globaldef.resource_path('pic/close.png')
        self.clicker = ButtonClicker(scale_factor=scale_factor)
    
    def on_button_click(self):
        globaldef.set_stop_loop(False)
        self.clicker.click_button(self.pic_btn_guild)
        if self.clicker.click_button(self.pic_btn_titanvalley, duration=4, threshold=0.97):
            
            # 泰坦Raid    
            if self.clicker.click_button(self.pic_btn_titanvalley_elementtournament, threshold=0.95, use_color=True):
                if self.clicker.click_button(self.pic_btn_titanvalley_tournament_raid):
                    if self.clicker.click_button(self.pic_btn_titanvalley_bulkraid):
                        self.clicker.click_button(self.pic_btn_titanvalley_showall, duration=4)
                        self.clicker.click_button(self.pic_btn_titanvalley_ok, duration=6)
                        self.clicker.click_button(self.pic_btn_titanvalley_rewardreceive)
                        self.clicker.click_button(self.pic_btn_titanvalley_reward)
                        self.clicker.click_button(self.pic_btn_titanvalley_receive)
                        self.clicker.click_button(self.pic_btn_titanvalley_allreceive)
                self.clicker.click_button(self.pic_btn_close)
        
            # 点开元素球
            if self.clicker.click_button(self.pic_btn_titanvalley_elementaltar, use_color=True):
                self.clicker.click_button(self.pic_btn_titanvalley_elementball, use_color=True)
                self.clicker.click_button(self.pic_btn_close, duration=3)
                
            self.clicker.click_button(self.pic_btn_close)
