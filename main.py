import os
import sys
import time

import random

def collect_air_data(sensor_obj):
    starttime=time.time()
    while True:
        print("tick")
        #print(random.randint(1,101))
        year, month, day, hour, minute, sec = map(int, time.strftime("%Y %m %d %H %M %S").split())
        print(year, " : ", month, " : ", day, " : ", hour, " : ", minute, " : ", sec)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

def main(argv):
    collect_air_data("nothing")


if __name__ == "__main__":
    main(sys.argv)
