def frameQButton():
    return """
    QPushButton {
        background-color: #3498db;  /* 기본 배경색 (파란색 계열) */
        color: white;  /* 글씨 색상 */
        border-radius: 15px;  /* 모서리 둥글게 */
        padding: 10px 15px;  /* 내부 여백 */
        font-size: 18px;  /* 글꼴 크기 */
        font-weight: bold; /* 글꼴 볼드체로 */
        border: 2px solid #2980b9; /* 테두리 색상 */
    }

    QPushButton:hover {
        background-color: #2980b9;  /* 마우스 오버 시 색 변경 */
    }

    QPushButton:pressed {
        background-color: #1c638d;  /* 클릭 시 색 변경 */
    }
        """