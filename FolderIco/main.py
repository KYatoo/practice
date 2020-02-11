import os, subprocess, codecs
import win32con, win32api

ini_str = '''
[.ShellClassInfo]\r\n
IconResource=icon.ico,0\r\n
[ViewState]\r\n
Mode=\r\n
Vid=\r\n
FolderType=Pictures\r\n
'''
Any2Ico_path = 'Quick_Any2Ico.exe'
ext = ["jpg", "jpeg", "png", "gif", "icns", "ico"]

while True:
    root = input('请输入目录(q/Q=Quit)：')
    if root.upper() == 'Q':
        break
    root = root.strip('"').strip("'")
    print('--->', root)

    for parent, dirnames, filenames in os.walk(root):
        if not dirnames:
            print(parent)
            try:
                first = min(p for p in os.listdir(parent) if p.split(".")[-1].lower() in ext)
                cmd = '"{0}" "-img={1}\{2}" "-icon={1}\icon.ico"'.format(Any2Ico_path, parent, first)
                subprocess.run(cmd)
                win32api.SetFileAttributes('{0}/icon.ico'.format(parent), win32con.FILE_ATTRIBUTE_HIDDEN)

                desktop_ini = '{0}/desktop.ini'.format(parent)
                if os.path.exists(desktop_ini):
                    os.remove(desktop_ini)
                f = codecs.open(desktop_ini, 'w', 'utf-8')
                f.write(ini_str)
                f.close()
                win32api.SetFileAttributes(desktop_ini, win32con.FILE_ATTRIBUTE_HIDDEN + win32con.FILE_ATTRIBUTE_SYSTEM)
                win32api.SetFileAttributes(parent, win32con.FILE_ATTRIBUTE_READONLY)
            except Exception as e:
                print(e)
                pass