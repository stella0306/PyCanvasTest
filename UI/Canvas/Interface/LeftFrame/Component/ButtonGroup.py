from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, pyqtSignal

from UI.Canvas.style.LeftFrame.LeftFrameQButtonStyle import frameQButton

class ButtonGroup(QWidget):
    buttonClicked = pyqtSignal(str)  # 버튼 클릭 시 버튼 텍스트 전달

    def __init__(self, parent=None):
        super().__init__(parent)

        # 버튼 레이아웃 (수평 정렬)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 여백 제거
        layout.setSpacing(10)  # 버튼 간격 설정

        # 버튼 생성
        self.canvasClearBtn = QPushButton("지우기", self)
        self.infoBtn = QPushButton("Info", self)

        # 스타일 적용
        self.canvasClearBtn.setStyleSheet(frameQButton())
        self.infoBtn.setStyleSheet(frameQButton())

        # 버튼 추가
        layout.addWidget(self.canvasClearBtn)
        layout.addWidget(self.infoBtn)

        # 버튼 클릭 이벤트 연결
        self.canvasClearBtn.clicked.connect(lambda: self.buttonClicked.emit("지우기"))
        self.infoBtn.clicked.connect(lambda: self.buttonClicked.emit("Info"))
