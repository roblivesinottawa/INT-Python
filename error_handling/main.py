class InvalidLevelError(Exception):
    def __init__(self, message):
        self.message = message


level = -1

try:
    if level < 1:
        raise InvalidLevelError(f"Invalid Level: {level}")
except InvalidLevelError as e:
    print(e.message)