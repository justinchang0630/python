from microbit import *
compass.calibrate()
while True:
    value = compass.heading()
    if value <= 45 or value >= 314:
        display.show('n')
    elif value >= 46  and value < 135:
        display.show('e')
    elif value >= 135  and value < 225:
        display.show('s')
    elif value >= 225  and value < 314:
        display.show('w')
    else :
        display.show()
