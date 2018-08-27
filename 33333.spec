# -*- mode: python -*-

block_cipher = None


a = Analysis(['33333.py'],
             pathex=['D:/Anaconda3/Lib/site-packages/PyQt5/Qt/bin', 'D:/Anaconda3/Lib/site-packages/PyQt5/Qt/plugins', 'D:\\\\Anaconda3\\\\Lib\\\\site-packages\\\\statsmodels', 'E:\\DFLM'],
             binaries=[],
             datas=[],
             hiddenimports=['statsmodels.tsa.statespace._filters', 'scipy._lib.messagestream', 'statsmodels.tsa.statespace._filters',
             'statsmodels.tsa.statespace._filters._conventional', 'statsmodels.tsa.statespace._filters._univariate',
             'statsmodels.tsa.statespace._filters._inversions', 'statsmodels.tsa.statespace._smoothers',
             'statsmodels.tsa.statespace._smoothers._conventional', 'statsmodels.tsa.statespace._smoothers._univariate',
              'statsmodels.tsa.statespace._smoothers._inversions', 'statsmodels.tsa.statespace._smoothers._classical',
              'statsmodels.tsa.statespace._smoothers._alternative'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='33333',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
