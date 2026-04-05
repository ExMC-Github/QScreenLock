from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
from ui.create_pwd import Ui_MainWindow
import sys
import json
import zlib
import hashlib
import os
class CreatePassword(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.setFixedSize(self.width(), self.height())
        self.ui.CancelButton.clicked.connect(self.cancel)
        self.ui.AppendPasswordButton.clicked.connect(self.append_pwd)
        self.ui.SetPasswordButton.clicked.connect(self.set_pwd)
    
    def cancel(self):
        self.close()
    
    def _compute_hash(self, password: str) -> str:
        text_bytes = zlib.compress(password.encode('utf-16'))
        sha256_hash = hashlib.sha256()
        sha256_hash.update(text_bytes)
        return sha256_hash.hexdigest()
    
    def _read_pwd_file(self):
        if not os.path.exists('pwd.json'):
            default_hashs = []
            with open('pwd.json', 'w') as f:
                json.dump({"pwd_hashs": default_hashs}, f, indent=4)
            return default_hashs
        else:
            with open('pwd.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('pwd_hashs', [])
    
    def _write_pwd_file(self, hash_list):
        with open('pwd.json', 'w', encoding='utf-8') as f:
            json.dump({"pwd_hashs": hash_list}, f, indent=4)
    
    def append_pwd(self):
        password = self.ui.lineEdit.text()
        if not password.strip():
            QMessageBox.warning(self, "Warning", "Password cannot be empty!")
            return
        
        new_hash = self._compute_hash(password)
        current_hashs = self._read_pwd_file()
        
        if new_hash in current_hashs:
            QMessageBox.information(self, "Info", "This password already exists in the list.")
        else:
            current_hashs.append(new_hash)
            self._write_pwd_file(current_hashs)
            QMessageBox.information(self, "Success", f"Password added successfully!\nTotal passwords: {len(current_hashs)}.")
            self.ui.lineEdit.clear()
    
    def set_pwd(self):
        password = self.ui.lineEdit.text()
        if not password.strip():
            QMessageBox.warning(self, "Warning", "Password cannot be empty!")
            return
        
        reply = QMessageBox.question(
            self, "Confirm Overwrite",
            "This will erase all existing passwords and set the current input as the only master password.\nAre you sure?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        
        new_hash = self._compute_hash(password)
        self._write_pwd_file([new_hash])
        QMessageBox.information(self, "Success", "Master password set successfully!")
        self.close()

if __name__ == "__main__":
    app = QApplication()
    app.setStyle('Fusion')
    window = CreatePassword()
    window.show()
    sys.exit(app.exec())