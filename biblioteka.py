# База данных книг
book_db = [
    {"title": "Подсознание может все", "author": "Джон Кехо", "price": 350},
    {"title": "Психология влияние", "author": "Роберт Чалдин", "price": 500},
    {"title": "К черту все берись и делай", "author": "Ричард Бренсон", "price": 400},
    {"title": "Атомные прывычки", "author": "Кто-то", "price": 500},
]

cart = []
balance = 1500
my_books = []


def is_matching_book(book, normalized_el):
    return book["title"].lower().replace(" ", "") == normalized_el


def search_in_bd_book(el, db_book):
    normalized_el = el.lower().replace(" ", "")
    return list(filter(lambda book: is_matching_book(book, normalized_el), db_book))


def search_in_cart(cart):
    search_title = input("Введите название книги: ")
    normalized_title = search_title.lower().replace(" ", "")
    result = [
        book for book in cart
        if book["title"].lower().replace(" ", "") == normalized_title
    ]
    if result:
        print("Найдено:", result)
        return result[0]
    else:
        print("Книга не найдена")
        return None


def show_library():
    print("\nСписок книг:")
    for book in book_db:
        print(f"{book['title']} | Автор: {book['author']} | Цена: {book['price']}")


def search_book():
    global cart, balance
    book_title = input("Введите название книги: ")
    find_books = search_in_bd_book(book_title, book_db)

    if find_books:
        print("Найдено:", find_books)
        user_choice = input("1 - В корзину | 2 - Купить | c - Пропустить: ")

        if user_choice == "1":
            cart.append(find_books[0])
            print(f"Книга '{find_books[0]['title']}' добавлена в корзину.")

        elif user_choice == "2":
            price = find_books[0]["price"]
            if balance >= price:
                balance -= price
                my_books.append(find_books[0])
                print("\n--- Чек ---")
                print(f"Книга: {find_books[0]['title']}")
                print(f"Цена: {price}")
                print(f"Ваш баланс: {balance}")
            else:
                print("У вас недостаточно денег.")
    else:
        print("Книга не найдена.")


def show_cart():
    global balance
    if cart:
        print("\nСодержимое корзины:")
        for book in cart:
            print(f"{book['title']} | Автор: {book['author']} | Цена: {book['price']}")

        user_choice = input("1 - Купить все | 2 - Поиск (выбрать): ")

        if user_choice == "1":
            total_price = sum(item["price"] for item in cart)
            if balance >= total_price:
                balance -= total_price
                print("\n--- Чек ---")
                print(f"Книги: {[item['title'] for item in cart]}")
                print(f"Общая сумма: {total_price}")
                print(f"Ваш баланс: {balance}")
                my_books.extend(cart)
                cart.clear()
            else:
                print("У вас недостаточно денег.")
        elif user_choice == "2":
            selected_book = search_in_cart(cart)
            if selected_book:
                user_action = input("1 - Купить | 2 - Удалить: ")
                if user_action == "1":
                    if balance >= selected_book["price"]:
                        balance -= selected_book["price"]
                        my_books.append(selected_book)
                        cart.remove(selected_book)
                        print("\n--- Чек ---")
                        print(f"Книга: {selected_book['title']}")
                        print(f"Цена: {selected_book['price']}")
                        print(f"Ваш баланс: {balance}")
                    else:
                        print("У вас недостаточно денег.")
                elif user_action == "2":
                    cart.remove(selected_book)
                    print(f"Книга '{selected_book['title']}' удалена из корзины.")
    else:
        print("Корзина пуста.")


def show_my_books():
    print("\nВаши книги:")
    if my_books:
        for book in my_books:
            print(f"{book['title']} | Автор: {book['author']}")
    else:
        print("У вас пока нет купленных книг.")


def top_up_balance():
    global balance
    amount = int(input("Введите сумму пополнения: "))
    balance += amount
    print(f"Баланс пополнен на {amount} сома.")
    print(f"Ваш текущий баланс: {balance}")


def main():
    actions = {
        "1": show_library,
        "2": search_book,
        "3": show_cart,
        "4": show_my_books,
        "5": top_up_balance,
        "6": exit,
    }

    while True:
        print("\n---------- Live Books -----------")
        print("1 - Библиотека")
        print("2 - Поиск")
        print("3 - Корзина")
        print("4 - Мои книги")
        print("5 - Пополнить баланс")
        print("6 - Выход")

        command = input("Выберите действие: ")
        action = actions.get(command)

        if action:
            action()
        else:
            print("Неверная команда!")


if __name__ == "__main__":
    main()
