# -*- coding: utf-8 -*- 

"""
画像ファイルの操作を行う汎用パッケージ
"""
__author__  = "Goro Maeda"
__version__ = "0.0.1"
__date__    = "2017/10/01"

import imghdr
import os
from PIL import Image

class OneImageFileConverter:
    """
    単一ファイルの画像変換クラス
    """
    def __init__(self, input, output, value):
        """
        コンストラクタ
        """
        self.filePath      = input
        self.savePath      = output
        self.magnification = value


    def resizeFile(self):
        """
        画像サイズ変更
        """
        print("--------------------------------------------------")
        print("  File name : {0}".format(os.path.basename(self.filePath)))

        # 画像ファイルか判定
        if imghdr.what(self.filePath) is None:
            print("  This file is not image file")
            return

        # 画像サイズ変換
        img = Image.open(self.filePath)
        width  = int(img.size[0] * float(self.magnification))
        height = int(img.size[1] * float(self.magnification))
        imgResize = img.resize( (width, height) )
        imgResize.save(self.savePath + '/' + os.path.basename(self.filePath), quality=100, optimize=True)

        print("  ({0}, {1}) -> ({2}, {3})".format(img.size[0], img.size[1], imgResize.size[0], imgResize.size[1]))
        print("--------------------------------------------------")
