
from storage import OrderManager
from user import User


manager = OrderManager()
def show_main_menu():
    print("========= Здравейте =========")
    print("Изберете една от следните опции")
    print("1 - Виж инвентара   2 - Доабави продукт в кошницата  3 - Виж продуктите в кошницата  q - За да излезеш от програмата")

def get_user_credentials():
    name = input("Име: ")
    age = int(input("Възраст: "))
    health = int(input("Как се чусвате от 1 до 10: "))
    return manager.user_is_authorized(name,age,health)
"""
 Главната функция на програмата , която се грижи за нейният работен цикъл
"""
def run():
    # Инициализираме обект от тип OrderManager

    if get_user_credentials():
        is_active = True

        while(is_active):
            show_main_menu()

            user_choice = input("Вашият избор: ")
            if user_choice == 'q':
                is_active = False
            elif user_choice == '1':

                manager.list_products()
            elif user_choice == '2':
                manager.list_products()
                item_number = int(input("Номер на желаният от вас продукт: "))
                item_quantity = int(input("Количество: "))
                manager.add_item_basket(item_number, item_quantity)
                manager.list_basket()

            elif user_choice == '3':
                manager.list_basket()
            else:
                show_main_menu()
    else:

        print("Съжаляваме , но не можем да ви обслужим")


run()

