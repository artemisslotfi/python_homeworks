from user_input import *

def search_phone_code():
    code = input("Enter the mobile code to search : ")

    for phone in phone_list:
        if phone["code"] == code:
            print(phone["code"], phone["name"], phone["brand"], phone["price"])
            break
    else:
        print("Error : phone not found !!!")

def search_phone_price():
    min = int(input("Enter the minimum price to search : "))
    max = int(input("Enter the maximum price to search : "))

    price_list = []
    # از استاد بپرسم todo
    for phone in phone_list:
        if min<phone["price"] and phone["price"]<max:
            price_list.append(phone)
            print(price_list)
            break
    else:
        print("Error : phone not found !!!")