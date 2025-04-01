from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import Qt, pyqtSignal
import sys
import os
# 프로젝트의 최상위 디렉토리 경로를 sys.path에 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))  # 4단계 위로 올라감
sys.path.append(project_root)

# 절대 경로로 모듈 임포트
from UI.Canvas.Interface.LeftFrame.CircleDrawingWidget.CircleWidget import CircleWidget
from utils.ColorUtils import randomRGB
from Dto.LeftFrame.ColorDto import ColorDTO


class ColorGrid(QGridLayout):
    colorChanged = pyqtSignal(int, int, int)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.setVerticalSpacing(5)

        # 그리드 레이아웃 설정
        for i in range(4):  # row
            for ii in range(4):  # col
                r, g, b = randomRGB()  # 튜플로 값 받기
                
                # ColorDTO 생성
                colorDTO=ColorDTO(
                        r=r, 
                        g=g, 
                        b=b
                    )

                self.addWidget(
                    self.createCircleWidget(
                        parent=parent, colorDTO=colorDTO
                        ),
                    ii, 
                    i,
                    alignment=Qt.AlignmentFlag.AlignTop
                )

    # 원형 생성 함수
    def createCircleWidget(self, parent, colorDTO):
        self.circleWidget = CircleWidget(
            parent=parent, 
            colorDTO=colorDTO
            )
        
        # 위젯 함수 연결
        self.circleWidget.colorClicked.connect(self.rgbSignalEmit)
        return self.circleWidget
    
    def rgbSignalEmit(self, r, g, b):
        # 클래스 밖으로 RGB 값 전송 (이벤트 발생)
        self.colorChanged.emit(r, g, b)