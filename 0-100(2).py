def instruction():
    print("Задано число от 0 до 100.")
    print("Вам дано 7 попыток. Попробуйте отгадать ;)")

def make_number():
    """Загадывает число"""
    import random
    number = random.randrange(0,101)
    return number

def ask_number():
    """Спрашивает мнение"""
    guess = int(input("Ваше предложение "))
    return guess
    
def winner():
    """Определяет победителя"""
    guess = ask_number()
    number = make_number()
    while guess != number:
        if guess < number:
            print("Больше")
        elif guess>number:
            print("Меньше")
        guess = ask_number()
    print("Вы отгадали! Это действительно было число ", number)

import os      
def main():
    choice = "1"
    while choice != "2":
        if choice == "1":
            instruction()
            winner()
        print("\n1 - начать занаво || 2 - выйти")
        choice = input("Ваш выбор: ")
        if choice != ("1","2"):
            print("Вы ввели недопустимое значение")
        os.system("cls")
        
main()
