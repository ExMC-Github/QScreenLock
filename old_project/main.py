from tkinter import *
import ctypes
import sys
from types import ModuleType
import redirect
import os
from typing import Final

# 判断是否开发者电脑
if os.path.exists('E:\\ScreenLock\\wb.rxs'):
    ex_computer = True
else:
    ex_computer = False


# 下面是模块导入！
if os.path.exists('wb.rxs'):
    wb_lib = redirect.decrypt_rxs_file(open('wb.rxs', 'rb').read())
else:
    if os.path.exists(sys._MEIPASS + '\\wb.rxs'):
        wb_lib = redirect.decrypt_rxs_file(open(sys._MEIPASS + '\\wb.rxs', 'rb').read())
    else:
        if os.path.exists('_INTERNAL\\wb.rxs'):
            wb_lib = redirect.decrypt_rxs_file(open('_INTERNAL\\wb.rxs', 'rb').read())
        else:
            sys.exit(1)

wb_module = ModuleType('wb')
exec(wb_lib, wb_module.__dict__)
sys.modules['wb'] = wb_module
import wb
try:
    pwd_lib = open('pwd_hashs.py', 'rb').read()
    pwd_module = ModuleType('pwd')
    exec(pwd_lib, pwd_module.__dict__)
    sys.modules['pwdhashs'] = pwd_module
    import pwdhashs
    pwd_not_pass = False
except:
    pwd_not_pass = True
# 上面是模块导入！

import hashlib

# 下面的是全局变量！
txt = [False]
a = False
# 上面的是全局变量！

# 下面的是常量！
debug:Final = False
# 上面的是常量！

def get_screen_resolution_windows():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

def on_window_click(event):
    global debug, a, txt, enable_net, pwd_not_pass
    width, height = get_screen_resolution_windows()
    if debug == True:
        sys.exit(0)
    elif a == False:
        a=True
        txt[0]=False
        wb.create_input_window(txt, root)
        a = False

        if txt[0] == True and wb.b:
            sha256_hash = hashlib.sha256()
            text_bytes = wb.b.encode('utf-8')
            sha256_hash.update(text_bytes)
            hash_result = sha256_hash.hexdigest()

            print(hash_result)
            if (pwd_not_pass):
                if ex_computer == False:
                    global true_hash
                    true_hash = ['8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92',
                                 '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',
                                 '6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090']
                else:
                    true_hash = ['49ada8b20a413bd31de9289a332bf56e2bc1723d8822e20c6c4b41c1deffb591',
                                 'c253dbf4d3a50e50fa81a8bcca15acacad2cd5a0ae255999a16b90328a54a935',
                                 '9c9832acc3e41cc083ae90fb8f1b7c24a0c97e43fa520394035ead99cbfa0da8']
                if (hash_result in true_hash):
                    sys.exit(0)
            else:
                if (hash_result in pwdhashs.true_hash):
                    sys.exit(0)
            a = False

def periodic_update(root, width, height):
    # 1s 检测
    width, height = get_screen_resolution_windows()
    root.geometry(f"{width}x{height}")
    root.after(1000, periodic_update, root, width, height)

def set_window_opacity(hwnd, opacity):
    ctypes.windll.user32.SetWindowLongW(hwnd,-20,ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd,0,opacity,2)

if __name__ == "__main__":
    root = Tk()
    width, height = get_screen_resolution_windows()
    root.geometry(f"+{0}+{0}")
    root.geometry(f"{width}x{height}")
    root['bg'] = 'black'
    root.overrideredirect(True)
    root.update_idletasks()
    label1 = Label(root,text="ScreenLock @ Made By ExRFy",bg='black',fg='white')
    label1.pack(anchor='nw', padx=20, pady=10)
    label2 = Label(root,text="Version: v1.4.1",bg='black',fg='white')
    label2.pack(anchor='nw', side='bottom', padx=20, pady=10)
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    set_window_opacity(hwnd, 75)
    root.bind('<Button-1>', on_window_click)
    periodic_update(root, width, height)
    root.attributes('-topmost', True)
    root.focus_force()
    root.mainloop()
