from decimal import Decimal

from Product import Product
from parser import JSONParser
from txt import TxtParser


class Menu:
    """Класс пользовательского меню."""

    def __init__(self, json_filename: str = "products", txt_filename: str = "products") -> None:
        """Конструктор класса Menu.

        Args:
            json_filename: Имя JSON файла.
            txt_filename: Имя TXT файла.
        """

        self.json = JSONParser(json_filename)
        self.txt = TxtParser(txt_filename)
        self.current = self.new_empty_product()

    def new_empty_product(self) -> Product:
        """Создание пустой карточки товара.

        Returns:
            product: Пустой объект Product.
        """

        return Product(
            id="0",
            name="",
            count=1,
            state="в обработке",
            distributor="",
            manufacturer="",
            price=Decimal("0"),
            location="",
            city="",
        )

    def input_decimal(self, input_price: str) -> Decimal:
        """Ввод стоимости товара.

        Args:
            input_price: Переменная для ввода цены.

        Returns:
            value: Корректное значение цены.
        """

        check = True
        value = Decimal("0")

        while check:
            raw = input(input_price).replace(",", ".").strip()

            try:
                value = Decimal(raw)
                check = False
            except Exception:
                print("Введите число, например 10.50")

        return value

    def print_current(self) -> None:
        """Вывод текущей карточки товара."""

        product = self.current

        print("\nТекущая карточка:")
        print("ID:", product.get_id())
        print("Название:", product.get_name())
        print("Количество:", product.get_count())
        print("Статус:", product.get_state())
        print("Поставщик:", product.get_distributor())
        print("Производитель:", product.get_manufacturer())
        print("Цена:", product.get_price())
        print("Местоположение:", product.get_location())
        print("Город:", product.get_city())
        print()

    def print_product_short(self, product: Product) -> None:
        """Краткий вывод информации о товаре.

        Args:
            product: Объект товара.
        """

        print(
            "ID:", product.get_id(),
            "|", product.get_name(),
            "| кол-во:", product.get_count(),
            "| статус:", product.get_state(),
            "| цена:", product.get_price(),
            "|", product.get_location(),
            "/", product.get_city()
        )

    def show_info(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            "\nВыберите действие:\n"
            "1) Задать ID товара\n"
            "2) Указать название товара\n"
            "3) Указать количество товара\n"
            "4) Указать поставщика\n"
            "5) Указать производителя\n"
            "6) Указать цену\n"
            "7) Указать местоположение\n"
            "8) Указать город\n"
            "9) Принять товар к учёту\n"
            "10) Поставить товар на учёт\n"
            "11) Списать товар\n"
            "12) Показать текущую карточку\n"
            "13) Сохранить текущую карточку в JSON (добавить/обновить)\n"
            "14) Показать все товары из JSON\n"
            "15) Найти товар в JSON по ID\n"
            "16) Удалить товар из JSON по ID\n"
            "17) Импортировать товары из TXT → сохранить в JSON\n"
            "18) Создать новую пустую карточку (сброс текущей)\n"
            "19) Выход\n"
        )

    def save_current_to_json(self) -> None:
        """Сохранение текущей карточки товара в JSON файл."""

        self.json.serialize_object(self.current)
        print("Сохранено в JSON")

    def show_all_from_json(self) -> None:
        """Вывод всех товаров из JSON файла."""

        products = self.json.deserialize_object()

        if not products:
            print("Каталог пуст (или JSON ещё не создан).")
        else:
            print("Товаров в каталоге:", len(products))

            for product in products:
                self.print_product_short(product)

    def find_by_id(self) -> None:
        """Поиск товара по id."""

        pid = input("Введите ID: ").strip()
        products = self.json.deserialize_object(ids=[pid])

        if not products:
            print("Не найдено")
        else:
            print("\nНайденный товар:")

            self.print_product_short(products[0])

    def delete_by_id(self) -> None:
        """Удаление товара из JSON файла по ID."""

        pid = input("Введите ID для удаления: ").strip()
        products = self.json.deserialize_object()

        new_products = []
        deleted = False

        for product in products:
            if product.get_id() == pid:
                deleted = True
            else:
                new_products.append(product)

        if not deleted:
            print("Товар с таким ID не найден!")
        else:
            self.json.serialize_list(new_products)
            print("Удалено из JSON")

    def import_txt_to_json(self) -> None:
        """Импорт товаров из TXT файла и сохранение их в JSON."""

        from_txt = self.txt.deserialize_object()

        if not from_txt:
            print("TXT пуст или не найден.")
        else:
            current = self.json.deserialize_object()

            by_id = {}
            for product in current:
                by_id[product.get_id()] = product

            for product in from_txt:
                by_id[product.get_id()] = product

            merged = []

            for key in by_id:
                merged.append(by_id[key])

            self.json.serialize_list(merged)
            print("Импортировано из TXT:", len(from_txt), "и сохранено в JSON")

    def choice(self, choice: str) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: Выбор пользователя.
        """

        try:
            c = int(choice)
        except ValueError:
            print("Введите число!")
            return True

        p = self.current

        if c == 1:
            p.set_id(input("Введите ID товара: ").strip())

        elif c == 2:
            p.set_name(input("Введите название товара: ").strip())

        elif c == 3:
            p.set_count(input("Введите количество товара: ").strip())

        elif c == 4:
            p.set_distributor(input("Введите поставщика: ").strip())

        elif c == 5:
            p.set_manufacturer(input("Введите производителя: ").strip())

        elif c == 6:
            price = self.input_decimal("Введите цену: ")
            p.set_price(price)

        elif c == 7:
            p.set_location(input("Введите местоположение: ").strip())

        elif c == 8:
            p.set_city(input("Введите город: ").strip())

        elif c == 9:
            p.set_state("принято к учёту")

        elif c == 10:
            p.set_state("состоит на учёте")

        elif c == 11:
            p.set_state("списано")

        elif c == 12:
            self.print_current()

        elif c == 13:
            self.save_current_to_json()

        elif c == 14:
            self.show_all_from_json()

        elif c == 15:
            self.find_by_id()

        elif c == 16:
            self.delete_by_id()

        elif c == 17:
            self.import_txt_to_json()

        elif c == 18:
            self.current = self.new_empty_product()
            print("Текущая карточка сброшена")

        elif c == 19:
            print("Выход...")
            return False

        else:
            print("Нет такого пункта меню")

        return True
