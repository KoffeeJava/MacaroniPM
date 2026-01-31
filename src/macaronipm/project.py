from . import misc
from. import error
import io
import requests
import json
import base64
from colorist import Color
from colorist import Effect

def getThumbnail():
    url = f"https://projects.penguinmod.com/api/v1/projects/getproject?projectID={misc.PID}&requestType=thumbnail"

    response = requests.get(url)

    if not response.status_code == 200:
        error.rerror(response.status_code, response.content)
        return -1
         
    base64_data = base64.b64encode(io.BytesIO(response.content).read()).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_data}"

def getMeta():
    url = f"https://projects.penguinmod.com/api/v1/projects/getproject?projectID={misc.PID}&requestType=metadata"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    return json.loads(response.content)

def loveToggle(toggle):
    url = "https://projects.penguinmod.com/api/v1/projects/interactions/loveToggle"

    data = f'{{"projectId":"{misc.PID}","token":"{misc.TOKEN}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    
    return 0

def voteToggle(toggle):
    url = "https://projects.penguinmod.com/api/v1/projects/interactions/voteToggle"

    data = f'{{"projectId":"{misc.PID}","token":"{misc.TOKEN}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    
    return 0

def getRankedProjects(page):
    url = f"https://projects.penguinmod.com/api/v1/projects/getprojects?page={page}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    return json.loads(response.content)

def hasLovedVoted():
    url = f"https://projects.penguinmod.com/api/v1/projects/getuserstatewrapper?projectId={misc.PID}&token={misc.TOKEN}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    return json.loads(response.content)

def getFrontpage():
    url = f"https://projects.penguinmod.com/api/v1/projects/frontpage"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1

    return json.loads(response.content)
