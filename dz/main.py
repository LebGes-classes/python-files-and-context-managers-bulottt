from menu import Menu


def main() -> None:
    """Запуск программы."""

    menu = Menu(json_filename="products", txt_filename="products")

    running = True

    while running:
        menu.show_info()
        choice = input("Ваш выбор: ").strip()
        running = menu.choice(choice)


if __name__ == "__main__":
    main()
