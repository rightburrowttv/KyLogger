class LogType:
    def __init__(self, level: int) -> None:
        self.level = level

class CustomType:
    def __init__(self, level: int, message: str) -> None:
        self.level = level
        self.message = message

INFO = LogType(0)
WARNING = LogType(1)
ERROR = LogType(2)
FATAL = LogType(3)