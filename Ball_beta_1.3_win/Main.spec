# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:/PythonWorkspace/games/BaseGame/Main.py'],
             pathex=['C:\\Users\\Théo\\Desktop\\Developpement\\PythonCompiler\\PyInstaller-3.0\\Main'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Main',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='C:\\Users\\Théo\\Desktop\\Developpement\\Android\\Ball\\icons\\ball.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='Main')
