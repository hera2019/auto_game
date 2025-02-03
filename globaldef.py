# globaldef.py 用于定义全局变量

import os
import sys

# 定义屏幕尺寸
screen_width = 1280
screen_height = 800

# 定义全局变量
stop_loop = False

def set_stop_loop(value=True):
    global stop_loop
    stop_loop = value
    if(value):
        print(f"stop_loop set: {stop_loop}")
    
def is_stopped():
    global stop_loop
    stop_loop_value = stop_loop
    stop_loop = False
    if(stop_loop_value):
        print("stop_loop: True 停止循环，重置为 False")
    return stop_loop_value

def resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

"""
# 检测当前游戏为激活窗口
#from AppKit import NSWorkspace
#import Quartz
def is_game_window_active():
    try:
        # 获取当前活动应用程序
        active_app = NSWorkspace.sharedWorkspace().frontmostApplication()
        # 获取当前活动窗口的标题
        options = Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements
        window_list = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID)
        for window in window_list:
            if window['kCGWindowOwnerName'] == active_app.localizedName():
                wtitle = window.get('kCGWindowName', u'Unknown')
                print(f"当前窗口为：{wtitle}")
                if "Hero Wars" in wtitle and "Chrome" in active_app.localizedName():
                    return True
    except Exception as e:
        print(f"Error: {e}")
    return False
"""
# 获取当前脚本的目录
#root_dir = '//Users//Hera//Documents//auto_game'
#root_dir = os.path.dirname(os.path.abspath(__file__))
#root_dir += '/'
