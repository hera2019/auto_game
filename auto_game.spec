block_cipher = None

a = Analysis(
    ['auto_game.py'],
    pathex=['/Users/Hera/Documents/auto_game'],
    binaries=[],
    datas=[
        ('auto_game.ico', './'),  # 图标文件路径
        ('pic/dailyquest.png', 'pic/'),
        ('pic/clear.png', 'pic/'),
        ('pic/dailyquest_weekly.png', 'pic/'),
        ('pic/dailyquest_guildquest.png', 'pic/'),
        ('pic/dailyquest_allreceive.png', 'pic/'),
        ('pic/dailyquest_fame.png', 'pic/'),
        ('pic/receive.png', 'pic/'),
        ('pic/guildquest_clear.png', 'pic/'),
        ('pic/guildquest_getsmall.png', 'pic/'),
        ('pic/guildquest_getbig.png', 'pic/'),
        ('pic/close.png', 'pic/'),
        ('pic/bigclose.png', 'pic/'),
        ('pic/airship.png', 'pic/'),
        ('pic/airship_expedition.png', 'pic/'),
        ('pic/rewardreceive.png', 'pic/'),
        ('pic/airship_assigningheroes.png', 'pic/'),
        ('pic/airship_angle.png', 'pic/'),
        ('pic/mail.png', 'pic/'),
        ('pic/allreceive.png', 'pic/'),
        ('pic/guild.png', 'pic/'),
        ('pic/guild_guildisland.png', 'pic/'),
        ('pic/dungeon.png', 'pic/'),
        ('pic/dungeon_getcard.png', 'pic/'),
        ('pic/dungeon_usecard.png', 'pic/'),
        ('pic/dungeon_herodoor.png', 'pic/'),
        ('pic/dungeon_titandoor_nature.png', 'pic/'),
        ('pic/dungeon_titandoor_water.png', 'pic/'),
        ('pic/dungeon_titandoor3.png', 'pic/'),
    ],  # 添加资源文件
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='HeroWarsAutoPlay',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    console=True,  # 将此处设置为 True 
    icon='auto_game.ico'  # 图标文件路径
)

app = BUNDLE(
    exe,
    name='HeroWarsAutoPlay.app',
    icon='auto_game.ico',  # 图标文件路径
    bundle_identifier=None,
)
