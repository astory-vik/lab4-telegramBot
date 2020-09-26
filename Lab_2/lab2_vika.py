import random
print("Добро пожаловать в игру 'камень ножницы бумага'")
while(2 + 2 == 4):
    print("Сделайте ваш выбор: 1)Камень 2)Ножницы 3)Бумага")
    result = input("Впишите желаемую цифру: ")
    def winner(x, y):
        if(y == 1):
            print("Бот: камень")
        elif(y == 2):
            print("Бот: ножницы")
        else:
            print("Бот: бумага")
        if x == 1 and y == 1:
            print("Ничья")
        elif x == 1 and y == 2:
            print("Вы выиграли")
        elif x == 1 and y == 3:
            print("Вы проиграли")
        elif x == 2 and y == 2:
            print("Ничья")
        elif x == 2 and y == 1:
            print("Вы проиграли")
        elif x == 2 and y == 3:
            print("Вы выиграли")
        elif x == 3 and y == 3:
            print("Ничья")
        elif x == 3 and y == 1:
            print("Вы выйграли")
        elif x == 3 and y == 2:
            print("Вы проиграли")
    
    winner(int(result), random.randint(1, 3))