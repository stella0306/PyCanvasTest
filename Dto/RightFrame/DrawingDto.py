from PyQt6.QtGui import QColor
from dataclasses import dataclass, field
from PyQt6.QtCore import QPoint
from typing import List

@dataclass
class DrawingDTO:
    paths: List[dict] = field(default_factory=list)  # 경로와 색상을 저장할 리스트
    current_path: List[QPoint] = field(default_factory=list)  # 현재 그리는 선
    current_color: QColor = field(default_factory=lambda: QColor(0, 0, 0))  # 기본 색상 (검정색)
    
    # 경로와 색상을 저장
    def add_path(self, path: List[QPoint], color: QColor):
        self.paths.append({
            'path': path, 
            'color': color
            })