from validation import *

phone_list=[]
code_check=[]

def get_data():
    code = input("Enter code : ")
    name = input("Enter name : ")
    brand = input("Enter brand : ")
    price = int(input("Enter price : "))

    code_check.append(code)
    # از استاد بپرسم todo
    if code in code_check:
        if code_validator(code) and name_validator(name) and brand_validator(brand) and price_validator(price):
            phone = {"code":code,"name": name, "brand": brand, "price": price}
            phone_list.append(phone)
            print("Info : mobile data Saved")
    else:
        print("Error : Code has already been entered !!!")