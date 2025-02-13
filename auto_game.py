# auto_game.py

import tkinter as tk
import tkinter.font as font
import threading
import json
import globaldef

# 设置缩放因子：由于Retina显示器的缩放比例为2，设置SCALE_FACTOR为2
SCALE_FACTOR = 2

# 创建主窗口
root = tk.Tk()
root.title("HeroWarsAutoPlay")
# 设置窗口大小
window_width = 742 #每个按钮大概106像素 106*7=742
window_height = 60
# 获取屏幕尺寸
globaldef.screen_width = root.winfo_screenwidth()
globaldef.screen_height = root.winfo_screenheight()
# 计算窗口位置（中上部）
x = int(globaldef.screen_width / 2 - window_width / 2)
y = 30 #screen_height - window_height - 100  # 50像素用于任务栏或Dock空间
# 设置窗口大小和位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# 设置窗口始终在最上层
root.attributes('-topmost', True)

# 使用资源文件
icon_path = globaldef.resource_path('app_icon.ico')
root.iconbitmap(icon_path)

# 创建按钮
btnWidth = 10
smallbtnWidth = 10
btnHeight = 1
rowButton = 0 # 按钮行数
colButton = 0 # 按钮行数
# 定义较小的字体
small_font = font.Font(family="Helvetica", size=7)

# 重置按钮布局逻辑
colButton = 0

# 定义颜色和字体
WINDOW_BG = "lightgray"  # 窗口背景色
BUTTON_BG = "#CCCCCC"  # 按钮背景色
BUTTON_MAIN_FG = "#666600"  # 按钮文字颜色
BUTTON_SUB_FG = "#AAAA00"  # 按钮文字颜色
BUTTON_FONT = ("Helvetica", 8, "bold")

# 设置窗口背景色
root.configure(bg=WINDOW_BG)

# 修改 place_main_button 和 place_sub_button 函数以设置按钮样式
def place_main_button(btnText, btnCommand):
    global colButton
    def async_command():
        button.configure(state="disabled")
        try:
            btnCommand()
        finally:
            button.configure(state="normal")

    button = tk.Button(root, text=btnText, command=lambda: threading.Thread(target=async_command, daemon=True).start(), width=btnWidth, height=btnHeight)
    button.configure(
        highlightbackground=BUTTON_BG,
        bg=BUTTON_BG,
        fg=BUTTON_MAIN_FG,
        font=BUTTON_FONT,
        relief=tk.RAISED,
        borderwidth=0)
    button.grid(row=0, column=colButton, padx=0, pady=0, sticky='w')
    colButton += 1
    return button
    
def place_sub_button(btnText, btnCommand, col=0, row=0, realsub=False):
    global colButton
    def async_command():
        button.configure(state="disabled")
        try:
            btnCommand()
        finally:
            button.configure(state="normal")

    button = tk.Button(root, text=btnText, command=lambda: threading.Thread(target=async_command, daemon=True).start(), width=btnWidth, height=btnHeight)
    fgcolor = BUTTON_MAIN_FG
    if(realsub):
        fgcolor = BUTTON_SUB_FG
        
    button.configure(
        highlightbackground=BUTTON_BG,
        bg=BUTTON_BG,
        fg=fgcolor,
        font=BUTTON_FONT,
        relief=tk.RAISED,
        borderwidth=0)
    button.grid(row=row + 1, column=colButton + col - 1, padx=0, pady=0, sticky='w')
    return button

# デイリークエスト
from dailyquest import DailyquestButton
dailyquest_button = DailyquestButton(SCALE_FACTOR)
click_btn_dailyquest = place_main_button("デイリークエスト", dailyquest_button.on_button_click)

# 飛空艇
from airship import AirshipButton
airship_button = AirshipButton(SCALE_FACTOR)
click_btn_airship = place_sub_button("飛空艇", airship_button.on_button_click)

# アウトランド
from outland import OutlandButton
outland_button = OutlandButton(SCALE_FACTOR)
click_btn_outland = place_sub_button("アウトランド", outland_button.on_button_click, row=1)

# メール
from mail import MailButton
mail_button = MailButton(SCALE_FACTOR)
click_btn_mail = place_main_button("メール", mail_button.on_button_click)

# ギフト
from gift import GiftButton
gift_button = GiftButton(SCALE_FACTOR)
click_btn_gift = place_sub_button("ギフト", gift_button.on_button_click)

# ソウルアトリウム
from soul import SoulButton
soul_button = SoulButton(SCALE_FACTOR)
click_btn_soul = place_sub_button("ソウルアトリウム", soul_button.on_button_click, row=1)

# タイタンの谷
from titanvalley import TitanvalleyButton
titanvalley_button = TitanvalleyButton(SCALE_FACTOR)
click_btn_titanvalley = place_main_button("タイタンの谷", titanvalley_button.on_button_click)

# アスガルド
from asgard import AsgardButton
asgard_button = AsgardButton(SCALE_FACTOR)
click_btn_asgard = place_sub_button("アスガルド", asgard_button.on_button_click)

# 特別イベント
from event import EventButton
event_button = EventButton(SCALE_FACTOR)
click_btn_event = place_sub_button("特別イベント", event_button.on_button_click, row=1)

# グランドアリーナ
from grandarena import GrandarenaButton
grandarena_button = GrandarenaButton(SCALE_FACTOR)
click_btn_grandarena = place_main_button("グランドアリーナ", grandarena_button.on_button_click)

click_btn_grandarena_battle = place_sub_button("Battle3", grandarena_button.on_battle3_click, realsub=True)

# Get Rewards
from getrewards import GetrewardsButton
getrewards_button = GetrewardsButton(SCALE_FACTOR)
click_btn_getewards = place_sub_button("Get Rewards", getrewards_button.on_button_click, row=1)

# アドベンチャー
from adventure import AdventureButton
adventure_button = AdventureButton(SCALE_FACTOR)
click_btn_adventure = place_main_button("アドベンチャー", adventure_button.on_button_click)

click_btn_adventure_domap = place_sub_button("Do Map", adventure_button.on_domap_click, realsub=True)

click_btn_adventure_battle = place_sub_button("BattleJump", adventure_button.on_battlejump_click, row=1, realsub=True)

# ダンジョン
from dungeon import DungeonButton
dungeon_button = DungeonButton(SCALE_FACTOR)
click_btn_dungeon = place_main_button("ダンジョン", dungeon_button.on_button_click)

click_btn_dungeon_nextdoor = place_sub_button("Next Door", dungeon_button.on_nextdoor_click, realsub=True)

click_btn_dungeon_battle = place_sub_button("Battle", dungeon_button.on_battle_click, row=1, realsub=True)

CONFIG_FILE = "auto_commands_config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def open_selection_dialog():
    # 弹出新窗口，用户勾选想要执行的命令
    selection_window = tk.Toplevel(root)
    selection_window.title("选择要执行的命令")

    # 定义所有可执行的命令项（标签: 对应函数）
    commands = {
        "ソウルアトリウム": soul_button.on_button_click,
        "ギフト": gift_button.on_button_click,
        "飛空艇": airship_button.on_button_click,
        "メール": mail_button.on_button_click,
        "アウトランド": outland_button.on_button_click,
        "グランドアリーナ": grandarena_button.on_button_click,
        "デイリークエスト": dailyquest_button.on_button_click,
        "特別イベント": event_button.on_button_click,
        "Get Rewards": getrewards_button.on_button_click,
        "タイタンの谷": titanvalley_button.on_button_click,
        "アスガルド": asgard_button.on_button_click,
        "アドベンチャー": adventure_button.on_button_click,
        "ダンジョン": dungeon_button.on_button_click,
    }

    check_vars = {}
    config = load_config() or {}
    # 设定一行放多少个复选框，这里示例为两列
    columns = 2
    row_index = 0
    col_index = 0

    for label, func in commands.items():
        if not func:
            continue
        var = tk.BooleanVar(value=config.get(label, True))
        check_vars[label] = var

        cb = tk.Checkbutton(selection_window, text=label, variable=var)
        cb.grid(row=row_index, column=col_index, sticky='w', padx=5, pady=5)

        col_index += 1
        # 如果列到达最大数，则换行
        if col_index == columns:
            col_index = 0
            row_index += 1

    # 让 Tkinter 自动适应内容（先让它设置好自然大小）
    selection_window.geometry("")  # 清空几何设定，让窗口自适应
    selection_window.update_idletasks()

    main_x = root.winfo_x()
    main_y = root.winfo_y()
    main_w = root.winfo_width()
    main_h = root.winfo_height()

    dialog_w = selection_window.winfo_width()
    dialog_h = selection_window.winfo_height() + 40

    # 将对话框的顶部与主窗口的底边对齐（示例）
    x = main_x + main_w - dialog_w
    y = main_y + main_h + 30
    selection_window.geometry(f"{dialog_w}x{dialog_h}+{x}+{y}")

    def run_selected_commands(config):
        # 在对话框关闭后再执行相关命令
        for label, func in commands.items():
            if func and config.get(label):
                func()
    
    def on_ok():
        new_config = {}
        for label, var in check_vars.items():
            new_config[label] = var.get()
        save_config(new_config)
        # 先关闭对话框
        selection_window.destroy()
        # 再执行命令，给一点微小延时让界面先恢复
        root.after(200, lambda: run_selected_commands(new_config))

    ok_button = tk.Button(selection_window, text="OK", command=on_ok)
    # 放在最后一行，跨列显示
    ok_button.grid(row=row_index + 1, column=0, columnspan=columns, pady=10)

def execute_selected_commands():
    # 打开选择窗口，让用户勾选后再执行
    open_selection_dialog()

# 创建一个新的按钮来执行所有命令
click_btn_execute_all = place_main_button("Do All", execute_selected_commands)

# All Clear
from allclear import AllclearButton
allclear_button = AllclearButton(SCALE_FACTOR)
click_btn_allclear = place_sub_button("Clear All", allclear_button.on_button_click, realsub=True)

# 定义一个函数来停止所有按钮的命令
def on_stop():
    globaldef.set_stop_loop(True)
    
click_btn_stop = place_sub_button("Stop", on_stop, row=1, realsub=True)

# 运行主循环
root.mainloop()