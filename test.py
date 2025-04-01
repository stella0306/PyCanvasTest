import sys
from dataclasses import dataclass, field
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QPoint


@dataclass
class DrawingApp(QWidget):
    paths: list = field(default_factory=list, init=False)  # 그려진 선을 저장
    current_path: list = field(default_factory=list, init=False)  # 현재 그리고 있는 선
    current_color: QColor = field(default_factory=lambda: QColor(0, 0, 0), init=False)  # 기본 검정색

    def __post_init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 자유 드로잉")
        self.setGeometry(100, 100, 800, 600)

        # 색상 선택 버튼
        self.color_button = QPushButton("색상 선택", self)
        self.color_button.clicked.connect(self.chooseColor)

        # 지우기 버튼
        self.clear_button = QPushButton("모든 선 지우기", self)
        self.clear_button.clicked.connect(self.clearCanvas)

        # 레이아웃 설정
        layout = QVBoxLayout(self)
        layout.addWidget(self.color_button)
        layout.addWidget(self.clear_button)
        layout.addStretch()
        self.setLayout(layout)

    def chooseColor(self):
        """색상 선택 다이얼로그"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.current_color = color  # 선택한 색상 저장

    def mousePressEvent(self, event):
        """마우스를 누르면 새로운 경로를 시작"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.current_path = [(event.position().toPoint(), self.current_color)]

    def mouseMoveEvent(self, event):
        """마우스를 움직이면 현재 선을 계속 그리기"""
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.current_path.append((event.position().toPoint(), self.current_color))
            self.update()

    def mouseReleaseEvent(self, event):
        """마우스를 떼면 현재 선을 paths 리스트에 저장"""
        if event.button() == Qt.MouseButton.LeftButton and self.current_path:
            self.paths.append(self.current_path)
            self.current_path = []
            self.update()

    def paintEvent(self, event):
        """화면을 다시 그릴 때 호출되는 함수"""
        painter = QPainter(self)
        
        # 기존에 그린 선들 그리기
        for path in self.paths:
            if path:
                pen = QPen(path[0][1], 2, Qt.PenStyle.SolidLine)
                painter.setPen(pen)
                for i in range(1, len(path)):
                    painter.drawLine(path[i - 1][0], path[i][0])

        # 현재 그리고 있는 선 그리기
        if self.current_path:
            pen = QPen(self.current_path[0][1], 2, Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            for i in range(1, len(self.current_path)):
                painter.drawLine(self.current_path[i - 1][0], self.current_path[i][0])

    def clearCanvas(self):
        """모든 선을 지우는 기능"""
        self.paths.clear()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec())
