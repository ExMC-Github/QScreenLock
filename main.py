import sys
from functions.system import get_screen_resolution_windows, is_winnt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from ui.main import Ui_MainWindow
Version = '0.1.0'
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

        central = self.centralWidget()
        label_height = self.height

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
        msg_box = QMessageBox(None)
        msg_box.setWindowTitle("QScreenLock")
        msg_box.setText("This window will closed.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
        msg_box.exec()
        self.close()


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