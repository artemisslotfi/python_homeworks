import model

while True:
    option = model.show_menu()

    if option == 1:
        phone = model.get_data()

    elif option == 2:
        model.search_phone_code()

    elif option == 3:
        model.search_phone_price()

    elif option == 4:
        print("phone List")
        model.show_list()

    elif option == 0:
        break

    else:
        print("Error : Invalid Option !!!")

    print("-" * 50)