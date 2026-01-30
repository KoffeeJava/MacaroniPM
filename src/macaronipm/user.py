from . import misc
import io
import requests
import json
import base64
from colorist import Color
from colorist import Effect

def getMeta(target):   
    url = f"https://projects.penguinmod.com/api/v1/users/profile?target={target}&token={misc.misc.TOKEN}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    return json.loads(response.content)

def isBlocking(target):
    url = f"https://projects.penguinmod.com/api/v1/users/hasblocked?target={target}&token={misc.misc.TOKEN}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    jsons = json.loads(response.content.decode())
    return jsons['has_blocked']

def getPfp(target):
    url = f"https://projects.penguinmod.com/api/v1/users/getpfp?username={target}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    
    base64_data = base64.b64encode(io.BytesIO(response.content).read()).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_data}"

def userExist(target):
    url = f"https://projects.penguinmod.com/api/v1/users/userexists?username={target}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    

    return json.loads(response.content)['exists']

def isBanned(target):
    url = f"https://projects.penguinmod.com/api/v1/users/isBanned?username={target}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    

    return json.loads(response.content)['isBanned']

def logout():
    url = "https://projects.penguinmod.com/api/v1/users/logout"

    data = f'{{"token":"{misc.misc.TOKEN}"}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    
    return 0

def getMessages():
    url = f"https://projects.penguinmod.com/api/v1/users/getmessages?token={misc.TOKEN}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    jsons = json.loads(response.content.decode())
    return jsons

def getUnreadMessages():
    url = f"https://projects.penguinmod.com/api/v1/users/getunreadmessages?token={misc.TOKEN}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    jsons = json.loads(response.content.decode())
    return jsons