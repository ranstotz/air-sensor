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
    # number at 5 for testing.
    while counter < 60:
        
        fake_co2 = random.randint(200,600)
        fake_tvoc = random.randint(1,20)

        # iso format timestamp
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S %z")
        second = timestamp[17:19]
        print("counter: ", counter)
        print(timestamp)

        minute_of_data.append(
            {"timestamp": timestamp, "co2": fake_co2, "tvoc": fake_tvoc}
        )
        counter += 1
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

        # return each minute, therefore if second == 59, new file
        # this is for starting the script mid-minute
        if second == "59":
            return minute_of_data
        
    return minute_of_data



def main(argv):

    s3_client = boto3.client('s3')

    # Write each minute of data to file
    while True:
        
        minute_data = event_per_second()
        file_name_by_minute = minute_data[-1]['timestamp'][0:16]
        key_name = file_name_by_minute + '.json'
        json_dump = json.dumps(minute_data)
    
        with open(key_name, 'w') as fp:
            fp.write(json_dump)

        #s3_client.put_object(Body=json_dump, Bucket='air-quality-sensor-ccs811', Key=key_name)
    

if __name__ == "__main__":
    main(sys.argv)
    
