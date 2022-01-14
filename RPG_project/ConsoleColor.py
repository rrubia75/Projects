class Color:
    BOLD= "\033[1m"
    RED= "\u001b[31m"
    BRIGHT_RED= "\u001b[31;1m"
    GREEN= "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RED_BACKGROUND= "\u001b[41m"

def text(string, Color):
    return Color + string + resetColor()

def resetColor():
    return "\u001b[0m"
