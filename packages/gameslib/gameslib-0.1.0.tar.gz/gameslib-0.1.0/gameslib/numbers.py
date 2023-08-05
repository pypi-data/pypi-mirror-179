# Written by TRC Loop

def to_display(num: float, digits: int = 1) -> str:
    newNum = format(num, f".{digits}f")
    return newNum

def to_readable(num: float):
    return f"{num:,}"

print(to_display(100.1828327))
print(to_display(100))