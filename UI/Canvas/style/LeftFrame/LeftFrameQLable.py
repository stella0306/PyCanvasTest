def frameQLable(r=0, g=0, b=255):
    return f"""
    QLabel {{
        font-size: 20px;
        font-weight: bold;
        color: rgb({r}, {g}, {b});
        
    }}
    """