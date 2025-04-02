from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication
from UI.Canvas.Interface.LeftFrame.LeftFrame import LeftFrame
from UI.Canvas.Interface.RightFrame.RightFrame import RightFrame
from UI.Canvas.style.CanvasInterfaceStyle import mainSelf

class CanvasInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 창 정렬 및 위치
        self.setWindowTitle('그림판 - 스크래치 시발아')
        self.setStyleSheet(mainSelf())
        self.resize(1200, 750)
        screenGeometry = QApplication.primaryScreen().geometry()
        windowGeometry = self.geometry()
        x = (screenGeometry.width() - windowGeometry.width()) // 2
        y = (screenGeometry.height() - windowGeometry.height()) // 2
        self.move(x, y)

        # 메인 위젯 설정
        mainWidget = QWidget(self)
        self.setCentralWidget(mainWidget)

        # 레이아웃 생성
        self.mainLayout = QHBoxLayout(mainWidget)

        # 좌측 프레임 추가
        self.leftFrame = LeftFrame(self)
        self.mainLayout.addWidget(self.leftFrame, 30)

        # 연결 추가
        self.leftFrame.colorGrid.colorChanged.connect(self.handleColorChange)
        self.leftFrame.btnMessage.connect(self.handleCanvasClear)
        # 우측 프레임 추가
        self.rightFrame = RightFrame(self)
        self.mainLayout.addWidget(self.rightFrame, 70)

        self.show()
    
    # 색상 변경
    def handleColorChange(self, r, g, b):
        self.leftFrame.mainLeftLabel.changeColor(r, g, b)
        self.rightFrame.mainRightLabel.changeColor(r, g, b)
        self.rightFrame.canvasWidget.setColor(r, g, b)

    # 현재 그려진 선 삭제
    def handleCanvasClear(self, btnMessage):
        self.rightFrame.canvasWidget.canvasClear() if btnMessage == "지우기" else None
        # print(btnMessage)