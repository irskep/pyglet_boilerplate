# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['/Users/steve/dev/_scratch/pyglet_boilerplate'],
             binaries=[],
             datas=[],
             hiddenimports=['future'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='PygletGame',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PygletGame')
app = BUNDLE(coll,
             name='PygletGame.app',
             icon=None,
             bundle_identifier='com.steveasleep.PygletGame')
