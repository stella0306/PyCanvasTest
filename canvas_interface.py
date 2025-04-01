import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
import random, math

from canvas_css import *



def random_rgb():
    return (
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255)
        )



class CircleDrawingWidget(QWidget):
    def __init__(self, parent, r, g, b):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # 위젯 크기 설정 (원형을 그릴 공간 확보)
        self.parent = parent
        self.r = r  # RGB 값 저장
        self.g = g
        self.b = b

    def update_circle_properties(self):
        # 위젯 크기 기반으로 반지름을 자동으로 계산
        widget_size = min(self.width(), self.height())
        self.radius = widget_size // 3  # 반지름은 위젯 크기의 1/3로 설정 (임의로 설정 가능)
        self.centerX = (self.width() - self.radius * 2) // 2  # 중앙에 맞춘 X 좌표
        self.centerY = (self.height() - self.radius * 2) // 2  # 중앙에 맞춘 Y 좌표

    def paintEvent(self, event):
        qp = QPainter(self)  # QPainter 객체 생성
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)  # 안티앨리어싱을 켜서 부드러운 곡선을 그립니다.

        # 펜 설정
        pen = QPen(Qt.PenStyle.NoPen) 
        qp.setPen(pen)  # 펜 적용

        # RGB 값으로 브러시 설정 (원 내부 색상 설정)
        brush = QBrush(QColor(self.r, self.g, self.b))  # RGB 값으로 색상 설정
        qp.setBrush(brush)  # 브러시 적용

        # 원형을 중앙에 그리기
        # (위젯의 중앙 좌표 계산)

        # 원형 그리기 (중앙 좌표, 크기 80x80)
        qp.drawEllipse(self.centerX, self.centerY, 80, 80)  # (x, y, width, height)

        qp.end()  # 그리기 종료

    def mousePressEvent(self, event):
        # 클릭한 좌표
        click_pos = event.pos()
        # 원의 중심과 클릭 좌표 간의 거리 계산
        distance = math.sqrt((click_pos.x() - self.centerX - self.radius) ** 2 + (click_pos.y() - self.centerY - self.radius) ** 2)

        # 원 안에 클릭이 있을 경우
        if distance <= self.radius:
            print(f"클릭한 원의 RGB 값: ({self.r}, {self.g}, {self.b})")
            # 부모 위젯의 left_label 색상 변경
            if self.parent:
                # left_label이 MainWindow에 존재한다고 가정
                self.parent.left_label.setStyleSheet(
                    left_frame_qlabel(
                        r=self.r, 
                        g=self.g, 
                        b=self.g
                        )
                        )
        else:
            print("원 외부를 클릭했습니다.")

    def resizeEvent(self, event):
        # 위젯 크기가 변경되면 반지름을 다시 계산하고 업데이트
        self.update_circle_properties()
        self.update()  # 다시 그리기

# 그림판 인터페이스
class CanvasInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.leftFrame()
        self.rightFrame()

        # 표시
        self.show()

    # 기본적인 UI 설정
    def initUI(self):
        # 윈도우 창 정렬 및 위치
        self.setWindowTitle('그림판 - 스크래치 시발아')
        self.resize(1600, 900)
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

        # 메인 위젯 설정
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # 레이아웃 생성
        self.main_layout = QHBoxLayout(main_widget)
    

    # 좌우 프레임
    def leftFrame(self):
        # 왼쪽 30%를 담당하는 QFrame
        left_frame = QFrame(self)

        # 내부 레이아웃 정의 (QVBoxLayout)
        left_layout = QVBoxLayout(left_frame)

        # 레이블 추가
        self.left_label = QLabel("색상 선택 및 기능 - 스크래치 시발아", self)
        self.left_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 텍스트 가운데 정렬
        self.left_label.setStyleSheet(left_frame_qlabel())
        left_layout.addWidget(self.left_label, alignment=Qt.AlignmentFlag.AlignTop)

        left_layout.addSpacing(10) # 간격

        # 그리드 레이아웃 추가
        grid_layout = QGridLayout()
    
        for i in range(4): # row
            for ii in range(4): # col
                grid_layout.addWidget(self.colorSelect(), ii, i, alignment=Qt.AlignmentFlag.AlignTop)
            grid_layout.setVerticalSpacing(20) # 간격


        left_layout.addLayout(grid_layout)  # QGridLayout을 QVBoxLayout에 추가
        left_layout.addStretch(1) # 간격

        # 스타일 설정
        left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        left_frame.setFrameShadow(QFrame.Shadow.Sunken)

        # 좌우 프레임을 30%, 70%로 나누기 위한 레이아웃 설정
        self.main_layout.addWidget(left_frame, 30)

    # 컬러 선택 위젯
    def colorSelect(self):
        r, g, b = random_rgb()
        return CircleDrawingWidget(
            parent=self, 
            r=r,
            g=g,
            b=b
            )

    # 좌우 프레임
    def rightFrame(self):
        # 오른쪽 70%를 담당하는 QFrame
        right_frame = QFrame(self)
        right_frame.setFrameShape(QFrame.Shape.StyledPanel)  # 스타일 지정
        right_frame.setFrameShadow(QFrame.Shadow.Sunken)  # 그림자 효과 추가


        right_label = QLabel("그림판 - 스크래치 시발아", right_frame)
        right_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 텍스트 가운데 정렬
        right_label.setStyleSheet(right_frame_qlabel())

        right_layout = QVBoxLayout(right_frame)  # 내부 레이아웃

        # 주요 위젯 추가
        right_layout.addWidget(right_label, alignment=Qt.AlignmentFlag.AlignTop)

        # 좌우 프레임을 30%, 70%로 나누기 위한 레이아웃 설정
        self.main_layout.addWidget(right_frame, 70)


def main():
    app = QApplication(sys.argv)
    window = CanvasInterface()

    # Start the event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()