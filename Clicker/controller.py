import model, view

def changetext():
    print(str(model.getgold()))
    view.counter.text = str(model.getgold())
    view.addbutton()

def addgold():
    model.addgold()

def main():
    print("hej")
    view.setup(addgold)

def update():
    global player, seccounter, ok

    stop = time.time()
    if stop-STARTTIME > seccounter:
        seccounter +=1
        ok += 1
        player.gold += player.gold_per_sec
    counter.text = str(player.gold)
    for b in (buttons):
        if player.gold  >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.red

if __name__ == '__main__':
    main()