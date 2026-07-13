def seconds_to_base60(seconds: int | float):
    minutes = int(seconds//60)
    display_seconds = int(seconds % 60)
    
    return f"{minutes}:{display_seconds:02d}"

