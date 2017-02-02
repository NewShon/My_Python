X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def instructions():
    """Выводит на экран инструкцию"""
    print(
        """Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
Чтобы сделать ход, введи число от 0 до 8. Числа однозначо соответствуют полям доски - так, как показано ниже:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

Приготовься к бою, жалкий белковый человечешка. Вот-вот начнется решающее сражение.\n""")

def ask_yes_no(question):
    """Задает вопрос с ответом да/нет"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def ask_number(question, low, hight):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low,hight):
        response = int(input(question))
    return response

def pieces():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить первый ход за собой? (y/n): ")
    if go_first == "y":
        print("\nНу что ж, даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nТвоя удаль тебя погубит... Буду начинать я.")
        computer = O
        human = X
    return computer, human

def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","---------")
    print("\n\t",board[3],"|",board[4],"|",board[5])
    print("\t","---------")
    print("\n\t",board[6],"|",board[7],"|",board[8],"\n")

def legal_moves(board):
    """Создать список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя  игре"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board,human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0-8):",0,NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move

def computer_move(board,computer,human):
    """Делает ход за компьютерного противника"""
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Я выберу поле номер")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print("Три ",the_winner," в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Как я и предсазывалб победа в очередной раз осталась за мной.\nВо всем.")
    elif the_winner == human:
        print("О нет, этого не может быть! Неужели ты как-то сумел перехитрить меня, белковый?\nКлянусь: я, компьютер, не допущу этого больше никогда!")
    elif the_winner == TIE:
        print("Тебе несказанно повезло, дружок: ты сумел свести игру вничью.\nРадуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить.")

def main():
    instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
        congrat_winner(the_winner,computer,human)

main()
input("Enter ")
