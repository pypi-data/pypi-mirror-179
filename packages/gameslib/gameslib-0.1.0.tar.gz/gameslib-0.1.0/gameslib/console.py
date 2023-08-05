import time
def clear():
		print("\033c")

def clear_return():
    return "\033c"



class Terminal:

    def __init__(self, columns = 80, lines = 25):
        self.columns = columns
        self.lines = lines
        self.clear()

    def clear(self):
        baseline = " " * self.columns
        self.canvas = []
        for line_no in range(0, self.lines - 1):
            self.canvas.append(baseline)
        print("")

    def clearLine(self, y):
        baseline = " " * self.columns
        self.canvas[y] = baseline

    def setChar(self, x, y, char):
        self.canvas[y] = self.canvas[y][:x] + char + self.canvas[y][x+1:]

    def setChars(self, x, y, chars):
        self.canvas[y] = self.canvas[y][:x] + chars + self.canvas[y][x+len(chars):]
      
    def setLineBlob(self, x, y, string):
        for line in string.split("\n"):
            self.setChars(x, y, line)
            y += 1

    def typewrite(self, x, y, line, delay = 0.1):
        for letter in line:
            self.setChar(x, y, letter)
            self.update()
            time.sleep(delay)
            x += 1

    def update(self):
        #print("\033[2J\033[1;1H",end="")
        print("\033[1;1H", end="")
        for line in self.canvas:
            print(line)

    def test(self):
        self.typewrite(0, 1, "This is a test Text")
        x = 10
        y = 5
        blob = f"""
This text is at x = {x}, y = {y}.
I love it!
        """
        self.setLineBlob(x, y, blob)
        self.update()
        time.sleep(1)
        x = 5
        y = 2
        blob = f"""
This Text is at x = {x}, y = {y}.
I just love it!!!!
        """
        self.setLineBlob(x, y, blob)
        self.update()
        time.sleep(1)
        self.clearLine(1)
        self.typewrite(0, 1, "Another test Text")
        self.typewrite(0, 2, "The Test comes to an end.")
        
