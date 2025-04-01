from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

from UI.Canvas.style.LeftFrame.LeftFrameQLable import frameQLable

class LeftLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("색상 선택 및 기능 - 스크래치 시발아")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(frameQLable())

    # 색상을 변경하는 함수
    def changeColor(self, r:int, g:int, b:int):
        self.setStyleSheet(frameQLable(r, g, b)) 