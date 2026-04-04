import ctypes
import platform
def get_screen_resolution_windows():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

def is_winnt():
    if platform.system() == "Windows":
        return True
    else:
        return False