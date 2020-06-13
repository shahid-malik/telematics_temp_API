import time
import json
import requests
from datetime import timedelta

from emails import *


def ipc_get_attend_record_count():
    """
    Get Total Record Count
    :return:
    """
    payload = {"startId": -1}
    url = BASE_URL + "getAttendRecordCount"

    response = requests.post(url, json=payload, headers=HEADERS)
    response = json.loads(response.content.decode('utf-8'))
    total_records = int(response["totalCount"])
    return total_records


def ipc_query_attend_record():
    """
    Get Attendance Records from AI Device
    :return:
    """
    # start_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
    start_time = datetime.datetime.now()

    payload = {
        "startId": -1,
        "reqCount": 30,
        "needImg": True
    }
    url = BASE_URL + "queryAttendRecord"
    response = requests.post(url, json=payload, headers=HEADERS, timeout=10)
    response = json.loads(response.content.decode('utf-8'))

    data = response['data']
    if data:
        for obj in data:
            name = obj['name']
            record_id = obj['id']
            timestamp = obj['timestamp']
            timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

            temperature_fahrenheit = float(obj['bodyTemperature'])
            temperature = round((temperature_fahrenheit * 9/5) + 32,2)
            image = obj['img']

            time_difference = (start_time - timestamp).total_seconds()
            print("ID:  {}  Name:  {}, Temperature:  {}, Time Difference: {}, TimeStamp:  {}".format(record_id, name, temperature, time_difference, timestamp))

            if temperature > TEMPERATURE_LIMIT and time_difference < TIME_PERIOD:
                send_email(name, temperature, image, timestamp)
        return response
    else:
        print("NO DATA FOUND")


if __name__ == "__main__":
    record_count = ipc_get_attend_record_count()
    print("Total Records: ", record_count)

    while 1:
        ipc_query_attend_record()
        print("Waiting for 60 seconds")
        time.sleep(TIME_PERIOD)
