import time
import json
import requests
from datetime import timedelta

from emails import *


now = datetime.datetime.utcnow()
now_start = now - timedelta(seconds=2000000000)
start_time = datetime.datetime.strftime(now_start, '%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')


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
            temperature_fahrenheit = float(obj['bodyTemperature'])
            temperature = round((temperature_fahrenheit * 9/5) + 32,2)
            print("ID:  {}  Name:  {}, Temperature:  {}, TimeStamp:  {}".format(record_id, name, temperature, timestamp))
            image = obj['img']
            if temperature > TEMPERATURE_LIMIT:
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
