from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, pyqtSignal

from UI.Canvas.Interface.LeftFrame.Component.ColorGrid import ColorGrid
from UI.Canvas.Interface.LeftFrame.Component.LeftLable import LeftLabel
from UI.Canvas.Interface.LeftFrame.Component.ButtonGroup import ButtonGroup

class LeftFrame(QFrame):
    colorChanged = pyqtSignal(int, int, int)
    btnMessage = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        # 내부 레이아웃 설정
        Layout = QVBoxLayout(self)

        # 레이블 추가
        self.mainLeftLabel = LeftLabel(self)
        Layout.addWidget(self.mainLeftLabel, alignment=Qt.AlignmentFlag.AlignTop)
        Layout.addSpacing(10)

        # 색상 원 그리드 추가
        self.colorGrid = ColorGrid(self)
        Layout.addLayout(self.colorGrid)
        Layout.addSpacing(10)
        
        # 버튼 그룹 추가 (컴포넌트 활용)
        self.buttonGroup = ButtonGroup(self)
        Layout.addWidget(self.buttonGroup)

        # 빈 공간 확장하여 UI 정렬
        Layout.addStretch(1)

        # 커맨드 연결
        self.colorGrid.colorChanged.connect(self.handleLabelColorChange)  # Signal 연결
        self.buttonGroup.buttonClicked.connect(self.handleBtnMessage)

    def handleLabelColorChange(self, r, g, b):
        self.mainLeftLabel.changeColor(r, g, b)
        self.colorChanged.emit(r, g, b)
        # print(f"클래스 밖에서 받은 RGB 값: {r}, {g}, {b}")

    def handleBtnMessage(self, btnMessage):
        self.btnMessage.emit(btnMessage)
