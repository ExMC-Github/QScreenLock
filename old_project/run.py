from tkinter import *
import ctypes
import sys
from types import ModuleType
import redirect
import redirect_nw
import os
import tkinter as tk
from tkinter import messagebox
import threading
import time
from typing import Final
from tkinter import ttk

def get_meipass():
    return sys._MEIPASS
# 使用示例
if __name__ == '__main__':
    if os.path.exists('main.rxc'):
        code_obj = redirect_nw.drf_to_pyobject(open('main.rxc', 'rb').read())
    else:
        if os.path.exists(get_meipass() + '\\main.rxc'):
            code_obj = redirect_nw.drf_to_pyobject(open(get_meipass() + '\\main.rxc', 'rb').read())
        else:
            if os.path.exists('_INTERNAL\\main.rxc'):
                code_obj = redirect_nw.drf_to_pyobject(open('_INTERNAL\\main.rxc', 'rb').read())
            else:
                sys.exit(1)

    exec(code_obj)
