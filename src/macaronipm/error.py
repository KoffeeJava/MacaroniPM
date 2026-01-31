import json
from colorist import Color
from colorist import Effect
from colorist import ColorHex

ORANGE = ColorHex("#ff8800")

def rerror(code, jsonr):
    error_ = json.loads(jsonr.decode())["error"]

    print(f"{Color.RED}MacaroniPM: An error has occured!")
    print(f"Status code: {code}")
    print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{error_}{Effect.OFF}")

    if error_ == "Project not found":
        print(f"{ORANGE}{Effect.BOLD}Hint: Try checking to see if the PID is correct!{Effect.OFF}")
    elif error_ == "NotFound":
        print(f"{ORANGE}{Effect.BOLD}Hint: Try checking to see if the username is correct{Effect.OFF}")
    elif error_ == "Reauthenticate":
        print(f"{ORANGE}{Effect.BOLD}Hint: Try checking to see if the token is correct or try to get a new token.{Effect.OFF}")