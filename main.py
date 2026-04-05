import sys
from functions.system import get_screen_resolution_windows, is_winnt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PySide6.QtCore import Qt
from ui.main import Ui_MainWindow
from ui.pwd import Ui_InputPwdForm
Version = '0.1.2'
class ScreenLock(QMainWindow):
    def __init__(self):
        self.width, self.height = get_screen_resolution_windows()
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centralWidget().installEventFilter(self)
        self.width, self.height = get_screen_resolution_windows()
        self.resize(self.width, self.height)
        self.move(0, 0)

        self.centralWidget().installEventFilter(self)
        self.ui.versionlabel.setText(f"Version: {Version}")
        self.ui.versionlabel.move(self.ui.versionlabel.x(),self.height-240)

    def eventFilter(self, obj, event):
        if obj == self.centralWidget() and event.type() == event.Type.MouseButtonPress:
            pos = event.position().toPoint()
            if self.centralWidget().childAt(pos) is None:
                self.click_window()
                return True
        return super().eventFilter(obj, event)
    
    def closeEvent(self, event):
        QApplication.quit()
    
    def click_window(self):
        dlg = InputPwdDialog(self)
        dlg.setWindowFlags(dlg.windowFlags() | Qt.WindowStaysOnTopHint)
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        dlg.move(screen_center - dlg.rect().center())
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.hide()
            msg_box = QMessageBox(None)
            msg_box.setWindowTitle("QScreenLock")
            msg_box.setText("Password correct, This Window will closed.")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
            msg_box.exec()
            self.close()
        """
        msg_box = QMessageBox(None)
        msg_box.setWindowTitle("QScreenLock")
        msg_box.setText("This window will closed.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
        msg_box.exec()
        self.close()
        """

class InputPwdDialog(QDialog, Ui_InputPwdForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Entry Password")
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.reject)
        self.correct_password = "123456"

    def confirm(self):
        if self.lineEdit.text() == self.correct_password:
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Password incorrect, please try again.")
            self.lineEdit.clear()
            self.lineEdit.setFocus()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows11")
    window = ScreenLock()
    if is_winnt() == False:
        QMessageBox.critical(None, "Error!", "This Program cannot run in not Windows system.")
        sys.exit(1)
    window.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
    window.setWindowOpacity(0.5)
    window.show()
    sys.exit(app.exec())