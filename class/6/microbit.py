from microbit import *
boat = Image ('00000:'
              '09090:'
              '08080:'
              '07070:'
              '06060:')
boat2 = Image ('00000:'
               '90909:'
               '80808:'
               '70707:'
               '60606:')
all_boats = [boat, boat2]
display.show(all_boats, delay=2000)