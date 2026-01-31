import requests
import json
from colorist import Color
from colorist import Effect
from colorist import ColorHex

ORANGE = ColorHex("#ff8800")

def setToken(settoken):
    global TOKEN
    TOKEN = settoken

def setProject(projectid):
    global PID
    PID = projectid

def follow(target, toggle):
    url = "https://projects.penguinmod.com/api/v1/users/follow"

    data = f'{{"token":"{TOKEN}","target":"{target}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"MacaroniPM: {Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
    
    return 0

def getFeatured():
    print(f"{ORANGE}MacaroniPM: The featured function is stil being worked on. It is recomended {Effect.BOLD}{Effect.UNDERLINE}NOT{Effect.OFF}{ORANGE} to use this.{Effect.OFF}")
    url = f"https://projects.penguinmod.com/api/v1/projects/searchprojects?page=0&query=&type=featured&token={TOKEN}&reverse=false"

    response = requests.get(url)
    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
        
    return response.text.split()

def getStats():
    url = f"https://projects.penguinmod.com/api/v1/misc/getStats"

    response = requests.get(url)
    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        return -1
        
    return json.loads(response.content)