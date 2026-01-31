import json
from colorist import Color
from colorist import Effect
from colorist import ColorHex

ORANGE = ColorHex("#ff8800")

def rerror(code, jsonr):
    print(f"{Color.RED}MacaroniPM: An error has occured!")
    print(f"Status code: {code}")
    print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(jsonr.decode())["error"]}{Effect.OFF}")
    if json.loads(jsonr.decode())["error"]) == "Project not found":
        print(f"{Color.RED}Hint: ")