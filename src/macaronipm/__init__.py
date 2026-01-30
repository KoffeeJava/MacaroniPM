import requests
from . import misc
from . import project
from . import user

def isOnline():
    url = f"https://projects.penguinmod.com/api/v1/ping"

    response = requests.get(url)

    if not response.status_code == 200:
        return -1

    return 0