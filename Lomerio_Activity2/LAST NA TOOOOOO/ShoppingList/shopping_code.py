import os
import time
import sys
basket = []

try:
    f = open("shopping_list.txt", "r")
    for line in f:
        basket.append(line.strip())
    f.close()
except:
    pass


def screen():
    os.system('cls')
    print("----------------------------------------")
    print("             Shopping List              ")
    print("----------------------------------------")
    print('\n')
    print("""
        1) Add Item
        2) View Items
        3) Delete Items
        4) Exit application
    """)
    print('Which option would you like to pick?(1, 2 or 3?) ')
    option = input('Choice: ')
    if len(option) > 0:
        if option == '1':
            add_item()
        elif option == '2':
            view_items()
        elif option == '3':
            delete_items()
        elif option == '4':
            exit_app()
        else:
            print('Sorry, Invalid Choice!')
        screen()
    else:
        screen()


def add_item():
    global basket
    os.system('cls')
    print("----------------------------------------")
    print("             Adding item                ")
    print("----------------------------------------")
    print('Press enter to return to main menu')

    choice = input("Enter item: ")

    if len(choice) > 0:
        basket.append(choice)
        print('Item added')
        shopping_list()
        time.sleep(1)
        add_item()
    else:
        screen()


def view_items():
    os.system('cls')
    print("----------------------------------------")
    print("             Viewing Items              ")
    print("----------------------------------------")
    print('\n\n')
    if not basket:
        print('Sorry, your basket is empty.')
    else:
        for item in basket:
            print(item)
        print('Press enter to return to main menu')
        input()
        screen()





def delete_items():
    global basket
    os.system('cls')
    print("----------------------------------------")
    print("             Viewing Items              ")
    print("----------------------------------------")
    print('\n\n')
    count = 0
    for item in basket:
        print(count, '-', item)
        count = count + 1
    print('What number to delete')
    choice = input('Number: ')
    if len(choice) > 0:
        try:
            del basket[int(choice)]
            print('Item Deleted!!!')
            shopping_list()
            time.sleep(1)
        except:
            print('Invalid Choice!')
            time.sleep(1)
        delete_items()

    else:
        screen()


def exit_app():
    return sys.exit()


def shopping_list():
    f = open("shopping_list.txt", "w")
    for item in basket:
        f.write(item + '\n')
    f.close()


screen()
