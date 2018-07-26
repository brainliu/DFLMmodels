#-*-coding:utf8-*-
#user:brian
#created_at:2018/7/13 14:00
# file: hahahh.py
#location: china chengdu 610000
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyInstaller.__main__ import run
# -F:打包成一个EXE文件
# -w:不带console输出控制台，window窗体格式
# --paths：依赖包路径
# --icon：图标
# --noupx：不用upx压缩
# --clean：清理掉临时文件

hiddenimports=["pandas._libs.tslibs.timedeltas","scipy._lib.messagestream","statsmodels.tsa.statespace._filters",
             "statsmodels.tsa.statespace._filters._conventional","statsmodels.tsa.statespace._filters._univariate",
             "statsmodels.tsa.statespace._filters._inversions","import statsmodels.tsa.statespace._smoothers",
             ],
if __name__ == '__main__':
    opts = ['-F', '-w', '--paths=D:/Anaconda364/Lib/site-packages/PyQt5/Qt/bin',
            '--paths=D:/Anaconda35/Lib/site-packages/PyQt5/Qt/plugins',
            # '--paths=F:\\KwDownload\\x86',
            # '--icon', 'rxx.ico', '--noupx', '--clean',
            '222.py']

    run(opts)