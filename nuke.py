import requests
import time

a = 0
WEBHOOK_URL = input('enter a valid webhook: ')
MESSAGE_CONTENT = input('Message Content: ')
COOLDOWN_SECONDS = 0.7

while True:
    response = requests.post(WEBHOOK_URL, json={'content': MESSAGE_CONTENT})
    if response.status_code == 204:
        a += 1
        message1 = "succefully send the {} message".format(a)
        print(message1)
    else:
        a += 1
        message2 = "failed on send the {} message we retry soon".format(a)
        print(message2)
        a -= 1
    time.sleep(COOLDOWN_SECONDS)
