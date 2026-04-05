import os
os.system('pyinstaller --noconfirm --onefile --windowed --name "QScreenLock" --version-file "version.txt"  "main.py"')
os.system('pyinstaller --noconfirm --onefile --windowed --name "QScreenLock-CreatePwd" --version-file "version_createpwd.txt"  "create_pwd.py"')