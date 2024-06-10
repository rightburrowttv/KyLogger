import os, sys
from LogTypes import INFO, WARNING, ERROR, FATAL, ACCESS, LogType, CustomType
from datetime import datetime

class LoggerOptions:
    def __init__(self, default: LogType, filePath: str, ):
        self.default = default
        self.path = filePath

class Logger:
    def __init__(self, options: LoggerOptions | None):
        if (options.path != None or options.path != ""):
            self.path = options.path
        if (options != None):
            self.options = options

    def Log(self, message: str, mode: LogType | None) -> None:
        mode = "[INFO]"
        if self.options.default == 0:
            mode = "[INFO]"
        elif self.options.default == 1:
            mode = "[WARNING]"
        elif self.options.default == 2:
            mode = "[ERROR]"
        elif self.options.default == 3:
            mode = "[FATAL]"
        else:
            mode = "[INFO]"

        with open(self.path, "a") as f:
            f.write(f"{mode} {message} - {datetime.now()}\n")
            return
    
    def Info(self, message: str):
        with open(self.path, "a") as f:
            f.write(f"[INFO] {message} - {datetime.now()}\n")
            return
    
    def Warn(self, message: str):
        with open(self.path, "a") as f:
            f.write(f"[WARNING] {message} - {datetime.now()}\n")
            return
        
    def Error(self, message: str):
        with open(self.path, "a") as f:
            f.write(f"[ERROR] {message} - {datetime.now()}\n")
            return
        
    def Fatal(self, message: str):
        with open(self.path, "a") as f:
            f.write(f"[FATAL] {message} - {datetime.now()}\n")
            return
        
    def Custom(self, message: str, type: CustomType):
        with open(self.path, "a") as f:
            f.write(f"[{type.message}] {message} - {datetime.now()}\n")
            return