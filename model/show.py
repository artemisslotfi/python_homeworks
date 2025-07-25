from model import user_input, phone_list


def show_list():
    for phone in phone_list:
        print(phone["code"], phone["name"], phone["brand"], phone["price"])