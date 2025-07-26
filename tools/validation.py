import re

def en_name_validator(en_name):
    if type(en_name)==str and re.match(r"^[a-zA-Z\s]{3,30}$",en_name):
        return True
    else:
        print("Error : Invalid  English name !!!")
        return False

def fa_name_validator(fa_name):
    if type(fa_name)==str and re.match(r"^[\sآ-ی]{3,30}$",fa_name):
        return True
    else:
        print("Error : Invalid Persian name !!!")
        return False

def en_family_validator(en_family):
    if type(en_family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", en_family):
        return True
    else:
        print("Error : Invalid English family !!!")
        return False

def fa_family_validator(fa_family):
    if type(fa_family) == str and re.match(r"^[\sآ-ی]{3,30}$", fa_family):
        return True
    else:
        print("Error : Invalid Persian family !!!")
        return False

def address_validator(address):
    if re.match(r"^[a-zA-Z\d\s\,]{10,}$", address):
        return True
    else:
        print("Error : Invalid address !!!")
        return False

def mobile_validator(mobile):
    if re.match(r"^(09|\+989)\d{9}$", mobile):
        return True
    else:
        print("Error : Invalid mobile number !!!")
        return False

def email_validator(email):
    if re.match(r"^[\w\.-]+@(gmail|yahoo)\.com$", email):
        return True
    else:
        print("Error : Invalid email !!!")
        return False

def national_code_validator(national_code):
    if re.match(r"^\d{10}$", national_code):
        return True
    else:
        print("Error : Invalid national code !!!")
        return False

def postal_code_validator(postal_code):
    if postal_code!="0000000000" and re.match(r"^\d{10}$", postal_code):
        return True
    else:
        print("Error : Invalid postal code !!!")
        return False