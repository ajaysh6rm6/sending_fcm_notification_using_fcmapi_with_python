#LINK : https://medium.com/devmins/firebase-cloud-messaging-api-with-python-6c0755e41eb5
## Install request module by running ->
#  pip3 install requests
import requests
import json

serverToken = 'AAAANs-SMqY:APA91bFcdhIKXFdDpD007zjx2JphhTF5qF-pvsUR5abfSU74vF1lwUIAT8aX_5jDTci3rhQhGk26ue29fiDiIIJKdcR0HhcKeQNaCGt9UUYfpiNO6P_r7mgNselPQuQ6nu7d2pmhnikN'
deviceToken = 'c6CmtkKFSsepdreoi5zEV7:APA91bEbHpgYsut2nLinJoR9QTXvmlYRCiFJvxnZ0wg-IHcefUN_efr_6X5Hq8j-U-yjq_8a3mPD7Ojt6-yks67FhPGXu5lNjsmX7hd9P0u4yOdQK4bpQ0vVkBTXw5vZQlehlT0SDgyJ'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + serverToken,
}

body = {
    'notification': {
        'title': 'Sending push form python script',
        'body': 'Test Message'
    },
    'to':deviceToken,
    'priority': 'high',
    #'data': dataPayLoad,
}
response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
print(response.status_code)
print(response.json())