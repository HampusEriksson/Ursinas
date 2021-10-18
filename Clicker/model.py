import controller
gold = 0

def getgold():
    global gold
    return gold

def addgold():
    global gold
    gold += 1
    controller.changetext()

