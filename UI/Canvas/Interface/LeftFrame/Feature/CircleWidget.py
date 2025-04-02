import math
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
from PyQt6.QtCore import Qt, pyqtSignal

class CircleWidget(QWidget):
    # RGB 값을 전달하는 시그널 정의
    colorClicked = pyqtSignal(int, int, int)  # (r, g, b) 값 전달

    def __init__(self, parent, colorDTO):
        super().__init__(parent)
        self.setFixedSize(80, 80)
        self.colorDTO = colorDTO

        self.parent = parent
        self.updateCircleProperties()

    # 화면 크기 변경 시 위치를 재계산 하는 함수
    def updateCircleProperties(self):
        size = min(self.width(), self.height())
        self.radius = size // 3
        self.centerX = (self.width() - self.radius * 2) // 2
        self.centerY = (self.height() - self.radius * 2) // 2

    # 원을 그리는 이벤트
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.PenStyle.NoPen))  # 펜 적용

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 부드러운 곡선
        painter.setBrush(QBrush(QColor(self.colorDTO.r, self.colorDTO.g, self.colorDTO.b)))  # RGB 색상 적용
        painter.drawEllipse(self.centerX, self.centerY, self.radius * 2, self.radius * 2)

    # 원을 마우스로 클릭 시 rgb 값을 출력하는 이벤트
    def mousePressEvent(self, event):
        click_x, click_y = event.pos().x(), event.pos().y()
        dist = math.sqrt(
            (
                click_x - self.centerX - self.radius
            ) ** 2 + (
                click_y - self.centerY - self.radius
            ) ** 2)

        if dist <= self.radius:
            self.colorClicked.emit(self.colorDTO.r, self.colorDTO.g, self.colorDTO.b)  # 시그널 발생

    # 화면 크기 변경 시 위치를 재계산 하는 이벤트
    def resizeEvent(self, event):
        self.updateCircleProperties()
        self.update()
