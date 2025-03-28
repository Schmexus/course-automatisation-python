while True:
    match int(input('Выберите пункт меню: \n 1. Добавить книгу на полку \n 2. вывести всю полку \n 3. удалить книгу с полки \n 4. выход \n')):
        case 1:
            with open('books.txt', 'a') as file:
                file.write(input('Введите название книги: ')+'\n')
        case 2:
            with open('books.txt', 'r') as file:
                string = file.readlines()
                for i in range(len(string)):
                    print(str(i+1)+'. '+string[i].strip())
                print('\n')
        case 3:
            book_remove = input('Введите книгу для удаления: ')+'\n'
            with open('books.txt', 'r') as file:
                polka = file.readlines()
            removed = False
            updated_lines = []
            for book in polka:
                if book == book_remove:
                    print(f"Книга '{book.strip()}' найдена и удалена.\n")
                    removed = True
                else:
                    updated_lines.append(book)
            if not removed:
                print("Строка для удаления не найдена. Попробуйте снова\n")
                continue
            # Открываем файл для записи и записываем обновленные данные
            with open('books.txt', 'w') as file:
                file.writelines(updated_lines)
        case 4:
            break
        case _:
            print('Введен некорректный пункт меню, попробуйте снова')
            continue