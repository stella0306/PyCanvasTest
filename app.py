import sys
from PyQt6.QtWidgets import QApplication
from UI.Canvas.Interface.CanvasInterface import CanvasInterface

def main():
    app = QApplication(sys.argv)
    window = CanvasInterface()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
