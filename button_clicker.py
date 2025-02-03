# button_clicker.py

import cv2
import pyautogui
import time
import numpy as np
import logging
import math

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ButtonClicker:     
    PIC_INDENT = 10 # 图像点击缩进像素
    
    def __init__(self, scale_factor=2):
        self.scale_factor = scale_factor
        self.pic_width = self.PIC_INDENT  
        self.pic_height = self.PIC_INDENT    

    def screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)    
        return screenshot

    def positions_close(self, pos1, pos2, tolerance=2):
        """
        判断两个坐标是否在允许的容差范围内
        """
        distance = math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])
        return distance <= tolerance
        
    def click_button(self, pic_path, duration=2, threshold=0.8, use_color=False, double_click=False, click_pos=0, checktwice=True):
        """
        每秒查找一次是否存在对应的图片，找到即刻返回。若在指定时间内未找到，返回空列表。        
        :param pic_path: 模板图像路径
        :param duration: 查找的持续时间（秒）
        :param threshold: 匹配阈值
        :param double_click: 是否双击
        :param click_pos: 0-8，代表9个方位：0-左上，1-上，2-右上，3-左，4-中，5-右，6-左下，7-下，8-右下
        :param checktwice: 是否再次检查
        :return: 匹配到的坐标列表或空列表
        """        
        button_positions = self.find_button(pic_path, duration, threshold, use_color)
        if button_positions:
            self.click(button_positions[0], double_click, click_pos)
            if checktwice:
                # 再次匹配，检查是不是按到了，窗口处于未激活状态，第一下按不到，但是不再等待
                time.sleep(0.3)
                button_positions2 = self.find_button(pic_path, duration=1, threshold=threshold, use_color=use_color)
                if button_positions2:
                    if self.positions_close(button_positions[0], button_positions2[0]):
                        logging.info(f"再次匹配到同一位置相同图像，再次点击")
                        self.click(button_positions2[0], double_click, click_pos)
            return True
        else:
            return False
            
    def find_button(self, pic_path, duration=2, threshold=0.8, use_color=False):
        end_time = time.time() + duration
        while time.time() < end_time:
            matched_points = []
                
            if use_color:
                template = cv2.imread(pic_path, cv2.IMREAD_COLOR)
                if template is None:
                    raise FileNotFoundError(f"未能加载图像: {pic_path}")
                screenshot_img = self.screenshot()  # 保留彩色截图
            else:
                template = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)
                if template is None:
                    raise FileNotFoundError(f"未能加载图像: {pic_path}")
                screenshot_img = cv2.cvtColor(self.screenshot(), cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(screenshot_img, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= threshold)

            for y, x in zip(*loc[::-1]):
                matched_points.append((int(x / self.scale_factor), int(y / self.scale_factor))) 
            
            if matched_points:
                logging.info(f"匹配图像: {pic_path}, use_color: {use_color}")
                        
                # 获取模板图像的宽度和高度
                template_height, template_width = template.shape[:2]
                self.pic_height = template_height / self.scale_factor
                self.pic_width = template_width / self.scale_factor
                #print(f"模板图像的宽度和高度: {self.pic_width}, {self.pic_height}")
                
                return matched_points  # 找到匹配点，立即返回
            else:
                #logging.info(f"暂时未寻找到图像: {pic_path}, use_color: {use_color}")
                pass
                        
            time.sleep(0.5)  # 等待0.5秒后再次查找
            
        logging.info(f"图像未匹配: {pic_path}, use_color: {use_color}")
        return matched_points  # 未找到匹配点，返回空列表
    
    def click(self, position, double_click=False, click_pos=0):
        logical_x = position[1] + self.PIC_INDENT
        logical_y = position[0] + self.PIC_INDENT
        if click_pos == 1: # 上
            logical_x = position[1] + self.pic_width / 2
            logical_y = position[0] + self.PIC_INDENT      
        elif click_pos == 2: # 右上
            logical_x = position[1] + self.pic_width - self.PIC_INDENT
            logical_y = position[0] + self.PIC_INDENT
        elif click_pos == 3: # 左
            logical_x = position[1] + self.PIC_INDENT
            logical_y = position[0] + self.pic_height / 2
        elif click_pos == 4: # 中
            logical_x = position[1] + self.pic_width / 2
            logical_y = position[0] + self.pic_height / 2
        elif click_pos == 5: # 右
            logical_x = position[1] + self.pic_width - self.PIC_INDENT
            logical_y = position[0] + self.pic_height / 2
        elif click_pos == 6: # 左下
            logical_x = position[1] + self.PIC_INDENT
            logical_y = position[0] + self.pic_height - self.PIC_INDENT
        elif click_pos == 7: # 下
            logical_x = position[1] + self.pic_width / 2
            logical_y = position[0] + self.pic_height - self.PIC_INDENT
        elif click_pos == 8: # 右下
            logical_x = position[1] + self.pic_width - self.PIC_INDENT
            logical_y = position[0] + self.pic_height - self.PIC_INDENT      
            
        self.click_point(logical_x, logical_y, double_click)
            
    def click_point(self, x, y, double_click=False):
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.1)
        
        if double_click:
            pyautogui.click(clicks=2)
            logging.info(f"Double-clicked button at position: {x}, {y}")
        else:
            pyautogui.click()
            logging.info(f"Clicked button at position: {x}, {y}")
                