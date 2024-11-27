import wikipediaapi

def main():
    user_agent = "MyWikiApp/1.0 (https://example.com; myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )  # Используем русскую Википедию

    while True:
        # 1. Запрашиваем у пользователя первоначальный запрос
        search_query = input("Введите запрос для поиска в Википедии (или 'выход' для завершения): ")
        if search_query.lower() == 'выход':
            break

        page = wiki_wiki.page(search_query)

        if not page.exists():
            print("Статья не найдена. Попробуйте другой запрос.")
            continue

        while True:
            print(f"\nСтатья: {page.title}\n")
            print(page.text[:1000])  # Печатаем первые 1000 символов статьи
            print("\nВыберите действие:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ")

            if choice == '1':
                # параграфы
                print("\nПараграфы статьи:")
                for section in page.sections:
                    print(f"\n{section.title}\n{section.text[:500]}")  # Печатаем первые 500 символов каждого параграфа
                input("\nНажмите Enter, чтобы продолжить...")
                break

            elif choice == '2':
                # связанные страницы
                print("\nСвязанные страницы:")
                for link in page.links.keys():
                    print(link)
                related_page_title = input("\nВведите название связанной страницы для перехода (или 'назад' для возврата): ")
                if related_page_title.lower() == 'назад':
                    break
                related_page = wiki_wiki.page(related_page_title)
                if related_page.exists():
                    page = related_page
                else:
                    print("Связанная страница не найдена. Попробуйте другой запрос.")
                    break

            elif choice == '3':
                print("Выход из программы.")
                return

            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
