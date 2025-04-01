from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt6.QtCore import Qt

from UI.Canvas.Interface.RightFrame.Component.RightLable import RightLabel
from UI.Canvas.Interface.RightFrame.CanvasDrawingWidget.CanvasWidget import CanvasWidget

class RightFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        # 내부 레이아웃 설정
        Layout = QVBoxLayout(self)

        # 레이블 추가
        self.mainRightLabel = RightLabel(self)
        Layout.addWidget(self.mainRightLabel, alignment=Qt.AlignmentFlag.AlignTop)
        Layout.addSpacing(10)

        # 캔버스 위젯 추가
        self.canvasWidget = CanvasWidget(self)
        self.canvasWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        Layout.addWidget(self.canvasWidget)  # CanvasWidget 바로 추가
