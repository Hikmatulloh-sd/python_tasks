"""
Библиотека 

как использовать 

Библиотека - Введите команду 1 для просмотра всех книг в библиотеке 

Поиск - Введиете команду 2 для поичка книг 
    Чтобы добавить в карзину введите команду 1 
    Чтобы купить введите котманду 2 
    Что бы пропустить нажмине Enter

Карзинка - Введите команду 3 
    1 - чтобы купить все книги в карзинке 
    2 - чтобы выбрать книгу 
        1 - купить выбранную книгу 
        2 - удалить выбранную книгу

Мои книги - команда 4, здесь вы можете видеть купленные вами книги

Паполнить баланс - команда 5 

Выйти из программы - команда 6 
        
"""
# База
biblioteka = [
    {"name":"Подсознание может все","autor":"Джон Кехо","price":350},
    {"name":"Психология влияние","autor":"Роберт Чалдин","price":500},
    {"name":"К черту все берись и делай","autor":"Ричард Бренсон","price":400},
    {"name":"Атомные прывычки","autor":"Кто-то","price":500},
]

karzina = []
balance = 1500
# Купленые
my_books = []


def search(base,el):
    resutl = list(filter(lambda book: book["name"].lower().replace(" ","") == el.lower().replace(" ",""),base))
    return resutl

while True:
    print("\n---------- Live Books -----------")
    print("1 - Библиотека ")
    print("2 - Поиск ")
    print("3 - Карзина ")
    print("4 - Мои книги ")
    print("5 - Паполнить баланс ")
    print("6 - Выход ")

    command = input("Выберите действие: ")

    # Вывести список книг 
    if command == str(1):
        for i in biblioteka:
            print(f"{i["name"]} | Автор {i["autor"]} | цена {i["price"]}")

    # Поиск 
    elif command == str(2):
        searched_book = input("Название : ")

        # Ищем книгу
        filtred_book = search(biblioteka,searched_book)

        # Ели книга найдена
        if filtred_book:
            print(filtred_book)
            user_choice = input("1 - в карзину | 2 - купить | с - пропустить ")

            # Добавляем в карзину найденную книгу 
            if user_choice == str(1):
                karzina.append(filtred_book[0])
                
                print(filtred_book)
                print("Добавлен в карзину")

            # Покупка
            elif user_choice == str(2):
                price = filtred_book[0]["price"] # Получам цену товара 
                if balance >= price:
                    balance -= price

                    my_books.append(filtred_book[0])

                    # Чек
                    print("\n--- Чек ---")
                    print(f"Книга : {filtred_book[0]["name"]}")
                    print(f"Цена  : {filtred_book[0]["price"]}")
                    print(f"Ваш баланс : {balance}")

                else:
                    print("У вас не достаточна деньги")
                #           крил                     латин
            elif user_choice == "с" and user_choice == "c":
                continue
        # Если кнги не найдена 
        else:
            print("Книга не найдена")

    elif command == str(3):
        
        if karzina:
            for i in karzina:
                print(f"{i["name"]} {i["autor"]} {i["price"]}")
            
            user_choice = input("1 купить все | 2 поиск(выбрать): ")
            
            if user_choice == str(1):
                price = sum(list(i["price"] for i in karzina))
                # print(price)
                
                if balance >= price:
                    balance -= price

                    # Чек
                    print("\n--- Чек ---")
                    print(f"Книги : {list(i["name"] for i in karzina)}")
                    print(f"Общай сумма  : {price}")
                    print(f"Ваш баланс : {balance}")
                    
                    for i in karzina:
                        my_books.append(i)

                    karzina.clear()

                else:
                    print("У вас не достаточна деньги")

            elif user_choice == str(2):
                search_book = input("Введите название книги: ")
                filtred_book = search(karzina,searched_book)

                print(filtred_book)
                user_choice = input("1 - купить | 2 - удалить: ")
                
                if user_choice == str(1):
                    price = filtred_book[0]["price"] 

                    if balance >= price:   
                        balance -= price

                        book = karzina.pop(karzina.index(filtred_book[0]))
                        my_books.append(book)

                        # Чек
                        print("\n--- Чек ---")
                        print(f"Книга : {filtred_book[0]["name"]}")
                        print(f"Цена  : {filtred_book[0]["price"]}")
                        print(f"Ваш баланс : {balance}")
                    
                    else:
                        print("У вас не достаточна средств")

                elif user_choice == str(2):
                    karzina.remove(karzina[karzina.index(filtred_book[0])])

    elif command == str(4):
        for i in my_books:
            print(i["name"],i["autor"])

    elif command == str(5):
        nwe_balance = int(input("Введите сумму: "))
        balance += nwe_balance

        print(f"Ваш баланс паполнен на {nwe_balance} сома")
        print(f"Ваш баланс {balance} сом")

    elif command == str(6):
        break
    
    else:
        print("Неверный команда!!!")