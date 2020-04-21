import os
import sys
import time
import boto3
import json
import random

def event_per_second():
    ''' Collect data point every second and return a 
    minute's worth of data. '''
    
    minute_of_data = []
    counter = 0

    starttime=time.time()
    while counter < 5:
        
        fake_co2 = random.randint(200,600)
        fake_tvoc = random.randint(1,20)

        year, month, day, hour, minute, sec = \
            time.strftime("%Y %m %d %H %M %S").split()
        timestamp = [year, month, day, hour, minute, sec]
        print("tick")
        print("counter: ", counter)
        print(timestamp)

        minute_of_data.append(
            {"timestamp": timestamp, "co2": fake_co2, "tvoc": fake_tvoc}
        )
        counter += 1
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
        
    return minute_of_data

def main(argv):

    s3_client = boto3.client('s3')

    # get minute for which we measure from first
    key_name = 'test/' + time.strftime("%Y%m%d%H%M") + '.json'
    # now collect second data for that minute
    minute_data = event_per_second()
    json_dump = json.dumps(minute_data)
    
    s3_client.put_object(Body=json_dump, Bucket='air-quality-sensor-ccs811', Key=key_name)
    

if __name__ == "__main__":
    main(sys.argv)
