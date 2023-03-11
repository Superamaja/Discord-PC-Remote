import os, winshell
from win32com.client import Dispatch

# Get shell:startup path using os
shellPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

path = shellPath + "/thing.lnk" # Path to be saved (shortcut)
target = os.getcwd() + "/main (no-console).pyw"  # The shortcut target file or folder
workDir = os.getcwd()  # The parent folder of your file

if os.path.exists('main (no-console).pyw'):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = workDir
    shortcut.save()