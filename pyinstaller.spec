# -*- mode: python -*-
import os
from pathlib import Path


# find paths relative to this file
root_path  = Path(__file__).parent
hooks_path = root_path / 'pyinstaller-hooks'
icon_path  = root_path / 'src' / 'widgets' / 'images' / 'icon.ico'

# path for pyinstaller hooks
# https://pyinstaller.readthedocs.io/en/stable/hooks.html
hookspath     = [str(hooks_path)]

# This work-around is required until
# pyinstaller releases this fix for pkg_resources (setuptools):
# https://github.com/pyinstaller/pyinstaller/commit/91481570517707fc70aa70dca9eb986c61eac35d#diff-dc99be50fd6e9451bec5c3e6c135c4b9
hiddenimports = ['pkg_resources.py2_warn']

# ???
block_cipher  = None

a = Analysis(['__main__.py'],
             pathex=[str(root_path)],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=hookspath,
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='qt_python_project',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon=str(icon_path))
