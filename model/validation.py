import re
from user_input import *

def code_validator(code):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$", code):
        return True
    else:
        print("Error : code is not true !!!")
        return False

def name_validator(name):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$", name):
        return True
    else:
        print("Error : name is not true !!!")
        return False

def brand_validator(brand):
    if re.match(r"^(samsung|apple|nokia)$", brand):
        return True
    else:
        print("Error : brand is not true !!!")
        return False

def price_validator(price):
    if type(price)==int and price>0:
        return True
    else:
        print("Error : price is not true !!!")
        return False