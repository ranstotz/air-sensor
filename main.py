import os
import sys
import time

import random

def collect_data(sensor_obj):
    year, month, day, hour, minute = map(int, time.strftime("%Y %m %d %H %M").split())

    print(year, " : ", month, " : ", day, " : ", hour, " : ", minute)
    for x in range(10):
        print(random.randint(1,101))
  

def main(argv):
    collect_data("nothing")


if __name__ == "__main__":
    main(sys.argv)
