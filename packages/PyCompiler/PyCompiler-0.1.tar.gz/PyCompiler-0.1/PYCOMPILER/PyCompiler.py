import os
import time
import sys

class PyCompiler():
    def PyCompiler(file, onefile = None):
        if onefile == None:
            os.system("python -m PyInstaller " + file)
        elif onefile == True:
            os.system("python -m PyInstaller --onefile " + file)
        else:
            print("Please provide a valid boolean; Null or True")
            print("Script Restarting in 3 Seconds")
            time.sleep(3)
            os.execl(sys.executable, sys.executable, *sys.argv)

    def Download():
        os.system("pip install pyinstaller")


