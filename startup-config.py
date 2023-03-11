import os, winshell
from win32com.client import Dispatch

# Get shell:startup path using os
shellPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

path = shellPath + "/Discord-PC-Remote.lnk"
target = os.getcwd() + "/main (no-console).pyw"
workDir = os.getcwd() 

if os.path.exists('main (no-console).pyw'):
    choice = None
    while (not choice in ['1', '2']):
        choice = input('(1) Activate startup with windows\n(2) Deactivate startup with windows\nEnter your choice: ')
        if choice == '1':
            if os.path.exists(path):
                os.remove(path) # Incase it's a broken shortcut
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = workDir
            shortcut.save()
            print('Startup with windows activated!')
            input('Press enter to exit...')
        elif choice == "2":
            if os.path.exists(path):
                os.remove(path)
                print('Startup with windows deactivated!')
                input('Press enter to exit...')
            else:
                print('Startup with windows is already deactivated!')
                input('Press enter to exit...')
else:
    print('main (no-console).pyw not found! Please reinstall the full program from GitHub.')