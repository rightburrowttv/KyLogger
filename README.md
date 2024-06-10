# KyLogger

## About
Kylogger is a simplistic logging package for easy logging to files

## Installation
```python3 -m pip install KyLogger```

## Examples
```
>> from KyLogger import Logger, LoggerOptions, INFO
>> options = LoggerOptions(INFO, "Info.log")
>> logger = Logger(options)
>> logger.Info("Test Message")
[INFO] Test Message - 2024-06-10 13:17:00 >> Info.log
```