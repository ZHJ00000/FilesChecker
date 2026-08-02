import shutil
import os
import datetime
import subprocess
import glob

subprocess.run(['xattr', '-cr', '.'], check=False)
shutil.copyfile('FilesChecker.pyw', './Build-macOS/FilesChecker.pyw')
shutil.copyfile('UI.py', './Build-macOS/UI.py')
if os.path.isdir('./Build-macOS/build'):
    shutil.rmtree('./Build-macOS/build')
if os.path.isdir('./Build-macOS/dist'):
    shutil.rmtree('./Build-macOS/dist')
with open('./Build-macOS/FilesChecker.pyw', 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace('[__BUILD__]', datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S'))
with open('./Build-macOS/FilesChecker.pyw', 'w', encoding='utf-8') as f:
    f.write(code)
os.chdir('./Build-macOS')
subprocess.run(['../.venv_macos/bin/pyinstaller', '-w',
                './FilesChecker.pyw'], check=True)
shutil.copytree('../Languages', './dist/FilesChecker.app/Contents/Resources/Languages')
shutil.copyfile('../Logo.png', './dist/FilesChecker.app/Contents/Resources/Logo.png')
shutil.copyfile('../Encodings.txt', './dist/FilesChecker.app/Contents/Resources/Encodings.txt')
shutil.copyfile('../curl-macos', './dist/FilesChecker.app/Contents/Resources/curl-macos')
shutil.copyfile('./Info.plist', './dist/FilesChecker.app/Contents/Info.plist')
shutil.copytree('../.venv_macos/lib/python3.14/site-packages/wx/locale', './dist/FilesChecker.app/Contents/Resources/locale')
shutil.copyfile('../LICENSE', './dist/FilesChecker.app/Contents/Resources/LICENSE')
# ! Replace '../.venv_macos/lib/python3.14/site-packages/wx/locale' into actual path!
for i in glob.glob('./Locale/*'):
    shutil.copytree(i, './dist/FilesChecker.app/Contents/Resources/' + i[9:])
subprocess.run(['chmod', '+x', './dist/FilesChecker.app/Contents/Resources/curl-macos'], check=True)
subprocess.run(['codesign', '--force', '--sign', '-', './dist/FilesChecker.app'], check=True)