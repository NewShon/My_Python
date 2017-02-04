import sys, os, pickle, shelve
def open_file(file_name,mode):
    """Открывает файл"""
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Невозможно открыть файл", file_name,", работа программы бдет завершена.\n",e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    score = next_line(the_file)
    if score:
        score = score[0]
    return category, question, answers, correct, explanation, score

def welcome(title):
    """Приветствует игрока и сообщает тему игры"""
    print("\t\tДобол пожаловать в игру 'Викторина'!\n")
    print("\t\t",title,"\n")

def main():
    wtd()
    name = input("Введите ваше имя: ")
    trivia_file = open_file("trivia.txt","r")
    title = next_line(trivia_file)
    welcome(title)
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    sc = 0
    while (category):
        print(category)
        print(question)
        for i in range(4):
            print("\t",i+1,"-",answers[i])
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("\nДа!")
            sc += int(score)
        else:
            print("\nНет.")
        print(explanation)
        print("Счет: ",sc,"\n\n")
        category, question, answers, correct, explanation, score = next_block(trivia_file)
    trivia_file.close()
    score = str(sc)
    write_score(name, score)
    print("Это был последний вопрос!")
    print("Ваш Счет: ",sc,"\n\n")

def write_score(name,score):
    player = [name,'    ',score,"\n"]
    records = open("records.txt","a")
    records.writelines(player)
    records.close()

def wtd():
    print("1 - начать игру  || 2 - показать рекорды ||  3 - выйти")
    choice = None
    while choice != ("1","2"):
        choice = input("Ваш выбор: ")
        if choice == "1":
            break
        elif choice =="2":
            records = open("records.txt","r")
            print("\n"+records.read())
            records.close()
        elif choice == "3":
            sys.exit()
        else:
            print("Вы ввели не то значение")
    os.system("cls")
            
main()
input()
