import requests
import json
import smtplib
from email.message import EmailMessage
import time
from datetime import date


def get_data(threshold):
    # Retrieve list of 30 trending equities
    r = requests.get('https://www.bookmyforex.com/api/secure/v1/get-full-rate-card')
    ans = json.loads(r.text)
    value = (ans['result'][0]['bpc'])
    print(value)

    if float(value) <= threshold:
        msg = EmailMessage()
        msg.set_content('Current rate: ' + value + ' Time: ' + str(date.today()))
        msg['Subject'] = 'BookMyForex: Good News. Dollar Rate dropped down: %s'

        msg['From'] = 'jainpeeyush20@gmail.com'
        recipients = ['jainpeeyush20@gmail.com']
        msg['To'] = ", ".join(recipients)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('user@gmail.com', 'bla')
        s.send_message(msg)
        s.quit()


if __name__ == '__main__':
    start_time = time.time()
    cnt = 0
    print('Enter dollar/inr rate below which you want to get notified: ')
    threshold = float(input())
    while True:
        get_data(threshold)
        time.sleep(300.0-((time.time() - start_time) % 300.0))
        cnt += 1

        # we will break the loop once we reach 1 hour of time.
        if cnt == 12:
            break
