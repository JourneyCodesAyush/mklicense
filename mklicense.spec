# mklicense.spec
a = Analysis(
    ['src/mklicense/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['mklicense.licenses'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mklicense',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
)
