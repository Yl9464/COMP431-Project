#Root/Admins check utilities 
import os
import sys
import ctypes

def is_admin() -> bool:
    """Check if the program is running with elevated admin privileges"""
    if sys.platform == "win32": #only run on windows system
        return windll.shell32.IsUserAnAdmin() != 0 if windll else False 
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False 