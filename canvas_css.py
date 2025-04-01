
def left_frame_qlabel(r=0, g=0, b=255):
    return f"""
    QLabel {{
        font-size: 20px;
        font-weight: bold;
        color: rgb({r}, {g}, {b});
        
    }}
    """


def right_frame_qlabel():
    return """
    QLabel {
        font-size: 20px;
        font-weight: bold;
        color: blue;
        
    }
    """