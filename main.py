"""
install python and check the add to path option
next to install required modules put this into a cmd:
python -m pip install requests json
or uncomment the next comment:
"""

""" remove this line
# and restart twice the script
from os import system
system('python -m pip install requests json')
"""#remove this line

import requests
import time
import json

########################################################################################
# I am not responsible for what can happen to you or to someone if you use that script #
########################################################################################

token = 'PUT YOUR TOKEN HERE'    # if you dont do that it wont work

# option = 'light' ^ 'dark'
def change_client_color(token, option):
    headers = {
        'authorization': token,
        'Content-Type': 'application/json',   
    }
    data = {
        'theme': option
    }

    response = requests.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=json.dumps(data))
    #print(response.text)
    print('>theme switched to {}'.format(option))

while 1:
    time.sleep(0.5)
    change_client_color(token, 'light')
    time.sleep(0.5)
    change_client_color(token, 'dark')
