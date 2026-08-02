import os
import sys
import platform
def GetBitmapPath():
    if os.path.basename(sys.argv[0]).split('.')[-1].lower().startswith('py'):
        return os.path.join(os.path.dirname(sys.argv[0]), 'Logo.png')
    if platform.system() != 'Darwin':
        return os.path.join(os.path.dirname(sys.argv[0]), 'Logo.png')
    else:
        return os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'Resources', 'Logo.png')