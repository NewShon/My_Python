import random, os


def menu():
    print("\t\tx_x\tDICE\tx_x")
    print("\n1 - Играть\n"
            "0 - Выход\n\n")

    choice = 3
    while choice != 1 and choice != 0:
        choice = int(input("Выш выбор: "))
    os.system("cls")
        
    if choice == 0: exit()
    else: opponents_choice()


def opponents_choice():
    print("Выберите с кем хотите сыграть:\n"
          "1 - С компьютером\n"
          "2 - С друзьями\n"
          "0 - Назад")
    
    choice = 3
    while choice != 1 and choice !=2 and choice !=0:
        choice = int(input("\nВаш выбор: "))
    os.system("cls")
        
    if choice == 1: game_with_computer()
    elif choice == 2: game_with_friends()
    elif choice == 0: menu()


def players_list():
    answer = '0'
    while answer != 'y':
        people_quantity = int(input("Сколько людей желает принять участие в игре: "))
        while answer != 'y' and answer != 'n':
            answer = input("Вы уверены (y/n): ")
            answer.lower()
    print("\n")

    players = [] 
    for i in range(1,people_quantity+1):
        print("Введите имя ",i," игрока: ")
        
        name = input()
        cash = 1000
        
        player = (name,cash)
        players.append(player)

    os.system("cls")
    return players


def computers_list():
    answer = '0'
    while answer != 'y':
        enemy_comp = int(input("Против скольки компьютеров вы желаете сыграть: "))
        while answer != 'y' and answer != 'n':
            answer = input("Вы уверены (y/n): ")
            answer.lower()
    print("\n")

    computers = [] 
    for i in range(1,enemy_comp+1): 
        name = "Компьютер " + str(i)
        cash = 1000
        
        computer = (name,cash)
        computers.append(computer)

    os.system("cls")
    return computers


def throw():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1+die2
    throw_list = [die1, die2, total]

    print("\tПервая кость - ", throw_list[0],
            "\n\tВторая кость - ", throw_list[1],
            "\n\tСумма костей - ", throw_list[2],"\n")
        
    return throw_list


def player_guess(real_players):
    players_guess = [] #содержит имена и догадки
    
    for player in real_players:
        print("\n",player[0])
        player_die1 = int(input("Ваша ставка на первую кость: "))
        player_die2 = int(input("Ваша ставка на вторую кость: "))
        player_total = int(input("Ваша ставка на сумму костей: "))
            
        guess = (player[0], player_die1, player_die2, player_total)
        players_guess.append(guess)

    return players_guess


def computer_guess(comp_players):
    computers_guess = [] #содержит имена и догадки
    
    for computer in comp_players:
        print("\n",computer[0])
        computer_dice = throw()
        guess = (computer[0], computer_dice[0], computer_dice[1], computer_dice[2])
        computers_guess.append(guess)

    return computers_guess

    
def tutorial():
    print("""Добро пожаловать в игру Кости!
Каждый игрок делает ставку и пытается угадать
какие выпадут номера костей и их сумму.
Побеждает тот, кто угадал больше всех.
\n\t\tУдачи!!!\n\n""")


def game_with_computer():
    real_players = players_list() #содержит имена и cash
    comp_players = computers_list() #содержит имена и cash
    whole_players = real_players + comp_players
    tutorial()

    stop = 2
    while stop != 0:
        os.system("cls")
        players_guess = player_guess(real_players) #содержит имена и догадки
        computers_guess = computer_guess(comp_players) #содержит имена и догадки
        input("Для броска нажмите Enter...")
        print("\nПосле броска кости выпали так:")
        random_throw = throw() #содержит бросок        
        
        whole_guess = players_guess + computers_guess #содержит все имена и догадки

        for i in range(len(whole_players)):
            counter = 0
            for guess in whole_guess[i]:
                if guess in random_throw:
                    counter+=1
            print(whole_players[i][0], " угадал ", counter, " ставки")
            
        print("\n")
        while stop != 1 and stop!= 0:
            stop = int(input("Еще раз? 1 - да  0 - нет: "))
       
    os.system("cls")
    menu()



def game_with_friends():
    os.system("cls")
    real_players = players_list() #содержит имена и cash
    tutorial()

        

menu()













