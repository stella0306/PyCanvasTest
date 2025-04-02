from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt

from Dto.RightFrame.DrawingDto import DrawingDTO  # DrawingDTO 임포트

class CanvasWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # DrawingDTO 인스턴스를 생성하여 선 및 색상 저장
        self.drawing_data = DrawingDTO()

        # 마우스 이벤트를 캔버스에서 처리할 수 있도록
        self.setMouseTracking(True)  # 마우스 이동 추적
        self.setAutoFillBackground(True)  # 배경색 설정 가능
        self.setStyleSheet("background-color: blue;")  # 배경색 파란색 설정

    # 현재 그려진 선 삭제
    def canvasClear(self):
        self.drawing_data.paths.clear()
        self.drawing_data.current_path.clear()
        self.update()

    def setColor(self, r, g, b):
        self.drawing_data.current_color = QColor(r, g, b)  # QColor 객체로 색상 변경

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # 선 그리기 시작점
            self.drawing_data.current_path = [event.pos()]

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            # 마우스를 드래그할 때 선 그리기
            self.drawing_data.current_path.append(event.pos())
            self.update()  # 화면 갱신 (repaint)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # 선과 색상 정보를 DrawingDTO에 저장
            self.drawing_data.add_path(self.drawing_data.current_path, self.drawing_data.current_color)
            self.drawing_data.current_path = []  # 현재 선 초기화
            self.update()  # 화면 갱신

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 선 부드럽게 그리기
        
        # 이미 그려진 모든 선을 그리기
        if self.drawing_data.paths:
            for path_data in self.drawing_data.paths:
                pen = QPen(path_data['color'], 2)  # 선 색상과 두께 설정
                painter.setPen(pen)
                painter.drawPolyline(*path_data['path'])  # 선 그리기

        # 현재 그리는 선도 그리기
        if self.drawing_data.current_path:
            pen = QPen(self.drawing_data.current_color, 2)  # 현재 색상으로 선 설정
            painter.setPen(pen)
            painter.drawPolyline(*self.drawing_data.current_path)  # 현재 선 그리기