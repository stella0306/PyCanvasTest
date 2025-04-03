from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication, QDialog, QLabel
from PyQt6.QtCore import Qt

from UI.Canvas.style.infoWindowsStyle import mainSelf, infoQLable

class infoWindows(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # 윈도우 창 정렬 및 위치
        self.setWindowTitle('info - 스크래치 시발아')
        self.setStyleSheet(mainSelf())
        self.resize(750, 750)
        screenGeometry = QApplication.primaryScreen().geometry()
        windowGeometry = self.geometry()
        x = (screenGeometry.width() - windowGeometry.width()) // 2
        y = (screenGeometry.height() - windowGeometry.height()) // 2
        self.move(x, y)

        # 메인 위젯 설정
        mainWidget = QWidget(self)
        
        # 레이아웃 생성
        layout = QHBoxLayout(mainWidget)

        # 위젯 추가
        layout.addWidget(self.createLabel())

        self.setLayout(layout)  # Set the layout to the dialog
        self.show()
    
    def createLabel(self):
        label = QLabel('만든이: ?', self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(infoQLable())

        return label