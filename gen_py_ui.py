import os
if os.path.exists('ui') == False:
    os.mkdir('ui')
os.system('pyside6-uic main.ui -o ui/main.py')
os.system('pyside6-uic pwd.ui -o ui/pwd.py')
os.system('pyside6-uic create_pwd.ui -o ui/create_pwd.py')