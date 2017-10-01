# -*- coding: utf-8 -*-
"""
Resize image file module.

Keyword arguments:
args[1] -- Input image file save directory path
args[2] -- Output image file save directory path
args[3] -- Image file resize magnification
"""
__author__  = "Goro Maeda"
__version__ = "0.0.1"
__date__    = "2017/10/01"

import glob
import MyUtils.ImageUtils
import os
import shutil
import sys

if __name__ == '__main__':
    # コマンドライン引数取得
    args = sys.argv
    argc = len(args)

    # コマンドライン引数チェック
    if (argc != 4):
        print("usage: python " + os.path.basename(args[0]) + " arg1 arg2 arg3")
        print("    arg1 -- Input image file save directory path")
        print("    arg2 -- Output image file save directory path")
        print("    arg3 -- Image file resize magnification")
        quit()

    print("Input directory  =[{0}]".format(args[1]))
    print("Output directory =[{0}]".format(args[2]))
    print("Magnification    =[{0}]".format(args[3]))

    # 保存先ディレクトリの存在チェック
    if not os.path.isdir(args[2]):
        os.makedirs(args[2])
    else:
        shutil.rmtree(args[2])  # 再帰的に削除
        os.makedirs(args[2])

    # ディレクトリ内のファイル一覧を取得
    files = glob.glob(args[1] + "/*.*")

    # ファイル単位に画像サイズを変更
    for file in files:
        if os.path.isdir(file):
            print("{0} is Direcotry".format(file))
        elif os.path.islink(file):
            print("{0} is Symbolic link".format(file))
        elif os.path.isfile(file):
            img = MyUtils.ImageUtils.OneImageFileConverter(file, args[2], args[3])
            img.resizeFile()
        else:
            print("{0} is Unknown".format(file))

    
    #------------------#
    # 次の書き方でもOK #
    #------------------#
    #import os
    #import sys
    #from MyUtils.ImageUtils import ImageConverter
    #
    ## Get program arguments
    #args = sys.argv
    #argc = len(args)
    #
    #print("argc=[" + str(argc) + "]")
    #print(args)
    #
    ## Program arguments check
    #if (argc != 2):
    #    print("usage: python " + os.path.basename(args[0]) + " arg1")
    #    quit()
    #
    ## Convert image file
    #img = ImageConverter(args[1])
    #img.resizeFile()
