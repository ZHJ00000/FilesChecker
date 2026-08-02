import shutil
import os
import datetime
import subprocess
if os.environ.get('PROCESSOR_ARCHITECTURE', '') == 'AMD64':
    shutil.copyfile('FilesChecker.pyw', '.\\Build-Windows\\FilesChecker.pyw')
    shutil.copyfile('UI.py', '.\\Build-Windows\\UI.py')
    if os.path.isdir('.\\Build-Windows\\build'):
        shutil.rmtree('.\\Build-Windows\\build')
    if os.path.isdir('.\\Build-Windows\\dist'):
        shutil.rmtree('.\\Build-Windows\\dist')
    with open('.\\Build-Windows\\FilesChecker.pyw', 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('[__BUILD__]', datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S'))
    with open('.\\Build-Windows\\FilesChecker.pyw', 'w', encoding='utf-8') as f:
        f.write(code)
    os.chdir('.\\Build-Windows')
    subprocess.run(['..\\.venv_windows\\Scripts\\pyinstaller.exe', '-w', '--version-file', '..\\Version_file.txt',
                    '.\\FilesChecker.pyw'], check=True)
elif os.environ.get('PROCESSOR_ARCHITECTURE', '') == 'ARM64':
    shutil.copyfile('FilesChecker.pyw', '.\\Build-Windows-Arm64\\FilesChecker.pyw')
    shutil.copyfile('UI.py', '.\\Build-Windows-Arm64\\UI.py')
    if os.path.isdir('.\\Build-Windows-Arm64\\build'):
        shutil.rmtree('.\\Build-Windows-Arm64\\build')
    if os.path.isdir('.\\Build-Windows-Arm64\\dist'):
        shutil.rmtree('.\\Build-Windows-Arm64\\dist')
    with open('.\\Build-Windows-Arm64\\FilesChecker.pyw', 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('[__BUILD__]', datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S'))
    with open('.\\Build-Windows-Arm64\\FilesChecker.pyw', 'w', encoding='utf-8') as f:
        f.write(code)
    os.chdir('.\\Build-Windows-Arm64')
    subprocess.run(['..\\.venv_windows-arm64\\Scripts\\pyinstaller.exe', '-w', '--version-file', '..\\Version_file.txt',
                    '.\\FilesChecker.pyw'], check=True)
shutil.copytree('..\\Languages', '.\\dist\\FilesChecker\\Languages')
shutil.copyfile('..\\Logo.png', '.\\dist\\FilesChecker\\Logo.png')
shutil.copyfile('..\\Encodings.txt', '.\\dist\\FilesChecker\\Encodings.txt')
shutil.copyfile('..\\LICENSE', '.\\dist\\FilesChecker\\LICENSE')
if os.environ.get('PROCESSOR_ARCHITECTURE', '') == 'AMD64':
    shutil.copyfile('..\\curl.exe', '.\\dist\\FilesChecker\\curl.exe')
elif os.environ.get('PROCESSOR_ARCHITECTURE', '') == 'ARM64':
    shutil.copyfile('..\\curl-arm64.exe', '.\\dist\\FilesChecker\\curl.exe')

