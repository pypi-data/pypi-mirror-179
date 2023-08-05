import sys
import random
import time
class BString(str):
    def contains(self, contains: str):
        if contains in self:
            return True
        else:
            return False
    def printAnimation(self, speed: int = 42):
        for l in self:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/speed)
        print("")

    def print(self):
        print(str(self))
        return str(self)

    def reverse(self):
        return self[::-1]

    def toLower(self):
        return self.lower()

    def toUpper(self):
        return self.upper()

    def add(self, plus):
        return self + plus

    def remove(self, remove:str):
        return self.replace(remove, "")

    def removeNumbers(self):
        return self.replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")

    def removeSpecials(self):
        return self.replace("!", "").replace('"', '').replace("§", "").replace("$", "").replace("%", "").replace("&", "").replace("/", "").replace("(", "").replace(")", "").replace("=", "").replace("?", "").replace("´", "").replace("²", "").replace("³", "").replace("{", "").replace("[", "").replace("]", "").replace("}", "").replace("ß", "ss").replace("\\", "").replace("*", "").replace("+", "").replace("~", "").replace("'", "").replace("#", "").replace("-", "").replace("_", "").replace(".", "").replace(":", "").replace(".", "").replace("`", "").replace(";", "").replace("<", "").replace(">", "").replace("|", "").replace("^", "").replace("°", "").replace("@", "").replace("€", "").replace("µ", "")

    def toFilename(self):
        return self.replace("!", "").replace('"', '').replace("§", "").replace("$", "").replace("%", "").replace("&", "").replace("/", "").replace("(", "").replace(")", "").replace("=", "").replace("?", "").replace("´", "").replace("²", "").replace("³", "").replace("{", "").replace("[", "").replace("]", "").replace("}", "").replace("ß", "ss").replace("\\", "").replace("*", "").replace("+", "").replace("~", "").replace("'", "").replace("#", "").replace(".", "").replace(":", "").replace(".", "").replace("`", "").replace(";", "").replace("<", "").replace(">", "").replace("|", "").replace("^", "").replace("°", "").replace("@", "").replace("€", "").replace("µ", "")

    def length(self):
        return len(self)

    def randomString(length: int = 8, choiceChars: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
        return "".join(random.choice(choiceChars) for x in range(length))