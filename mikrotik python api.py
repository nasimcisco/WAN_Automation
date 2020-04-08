#pip3 install librouteros
#in mikrotik enable /ip services api 8728 port 

from librouteros import connect
from getpass import getpass
import json
ip = "10.0.0.20"
user = input("Input username: ")
passw = getpass()
api = connect(username=user, password=passw, host=ip)
ip_info = api(cmd="/ip/address/print")
print (json.dumps(ip_info, indent=3))
