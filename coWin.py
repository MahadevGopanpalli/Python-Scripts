import datetime
import json
import time

import notify2
import requests

notify2.init('app name')

pincode =413002
date=datetime.datetime.now().strftime("%d-%m-%Y")
print("Cheking for Vaccine.. " )
header={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
data=requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}".format(pincode,date),headers=header)


while 1:
    try:
        Data=data.json()

        for center in Data['centers']:
            for sess in center['sessions']:
                print(sess['available_capacity'])
                if(sess['available_capacity']>0):
                    n = notify2.Notification("Vaccine",
                            "Vaccine ia available",
                            "notification-message-im"   # Icon name
                            )
                    n.show()
        time.sleep(10)
    except Exception as e:
        print(e)
