import json
import requests
from datetime import timedelta

from emails import *


now = datetime.datetime.utcnow()
now_start = now - timedelta(seconds=2000000000)
start_time = datetime.datetime.strftime(now_start, '%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
headers = {'Content-Type': 'application/json'}
base_url = "http://" + MACHINE_IP + ":8080/api/v1/face/"


def ipc_query_attend_record():
    payload = {"startId": -1, "reqCount": 1, "needImg": True}
    url = base_url + "queryAttendRecord"
    response = requests.post(url, json=payload, headers=headers)
    response = json.loads(response.content.decode('utf-8'))

    data = response['data']
    for obj in data:
        # user_id = obj['userid']
        name = obj['name']
        # gender = obj['gender']
        # phone = obj['phone']
        # id = obj['id']
        timestamp = obj['timestamp']
        temperature = float(obj['bodyTemperature'])
        image = obj['img']
        print(image)
        # if temperature < 90.0:
        send_email(name, temperature, image, timestamp)
    return response


if __name__ == "__main__":
    ipc_query_attend_record()
