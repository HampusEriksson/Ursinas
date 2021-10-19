from constants import *
import model, view

seccounter = 0

def changetext():
    view.counter.text = str(model.getgold())
    view.gpsCounter.text = str(model.getgps())

def addgold():
    model.addgold()

def main():
    view.setup(addgold)

def update():
    global seccounter
    stop = time.time()
    view.timecounter.text = str(round(stop-STARTTIME, 1))

    if model.player.gold_per_sec > 120:
        seccounter += 1 / 120
        model.player.gold += model.player.gold_per_sec/120

    if stop-STARTTIME > seccounter and model.player.gold_per_sec != 0:
        seccounter += 1 / model.player.gold_per_sec
        model.player.gold += 1

    changetext()


if __name__ == '__main__':
    main()