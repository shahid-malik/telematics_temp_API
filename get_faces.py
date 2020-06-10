import json
import datetime
import requests
from datetime import timedelta

from emails import *


now = datetime.datetime.utcnow()
now_start = now - timedelta(seconds=2000000000)
start_time = datetime.datetime.strftime(now_start, '%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
headers = {'Content-Type': 'application/json'}
base_url = "http://" + MACHINE_IP + ":8080/api/v1/face/"


# def ipc_getAttendRecordCount():
#     payload = {
#         "startTime": start_time,
#         "endTime": end_time,
#         "startId": -1
#     }
#     url = base_url + "getAttendRecordCount"
#     response = requests.post(url, json=payload, headers=headers)
#     response = json.loads(response.content.decode('utf-8'))
#     print(response)
#     # response.raise_for_status()
#     return response
#
#
def ipc_queryAttendRecord():
    payload = {"startId": -1, "reqCount": 5, "needImg": True}
    url = base_url + "queryAttendRecord"
    response = requests.post(url, json=payload, headers=headers)
    response = json.loads(response.content.decode('utf-8'))

    data = response['data']
    for obj in data:
        name = obj["name"]
        temperature = float(obj['bodyTemperature'])
        image = obj['img']
        print(obj['timestamp'])

        if temperature < 90.0:
            send_email(name, temperature, image)
    return response

# ipc_getAttendRecordCount()
# ipc_queryAttendRecord()


def ipc_getDefaultMqtt():
    ipaddr = MACHINE_IP

    # post body
    headers = {}
    headers['Content-Type'] = 'application/json'

    # post send
    url = "http://" + ipaddr + ":8080/api/v1/face/getDefaultHttpCloud"
    print(url)
    response = requests.post(url, headers=headers)

    response.raise_for_status()

    return response

ipc_getDefaultMqtt()
# def ipc_queryAllPerson():
#     ipaddr = MACHINE_IP
#     filename = '/home/shahid/PycharmProjects/telematics_temperature_senser_app/ipc_queryAllPerson.ini'
#
#     # post body
#     headers = {}
#     headers['Content-Type'] = 'application/json'
#     f = open(filename, 'r')
#     payload = json.loads(f.read())
#
#     # post send
#     url = "http://" + ipaddr + ":8080/api/v1/face/queryAllPerson"
#     response = requests.post(url, json=payload, headers=headers)
#
#     response.raise_for_status()
#
#     return response
#
# ipc_queryAllPerson()