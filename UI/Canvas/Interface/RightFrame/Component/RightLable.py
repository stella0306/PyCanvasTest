from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

from UI.Canvas.style.RightFrame.RightFrameQLable import frameQLable

class RightLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("그림판 - 스크래치 시발아")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(frameQLable())

    # 색상을 변경하는 함수
    def changeColor(self, r:int, g:int, b:int):
        self.setStyleSheet(frameQLable(r, g, b)) 