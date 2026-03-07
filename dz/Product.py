from decimal import Decimal


class Product:
    def __init__(
        self,
        id: str = "",
        name: str = "",
        count: int = 0,
        state: str = "",
        distributor: str = "",
        manufacturer: str = "",
        price: Decimal = Decimal("0"),
        location: str = "",
        city: str = ""
    ) -> None:
        """Конструктор класса Product.

        Args:
            id: Идентификатор товара.
            name: Название товара.
            count: Количество товара.
            state: Состояние товара.
            distributor: Поставщик товара.
            manufacturer: Производитель товара.
            price: Стоимость товара.
            location: Местоположение товара.
            city: Город товара.
        """

        self.__id = id
        self.__name = name
        self.__count = count
        self.__state = state
        self.__distributor = distributor
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__city = city

    def get_id(self) -> str:
        """Геттер id товара.

        Returns:
            id: id товара.
        """

        return self.__id

    def get_name(self) -> str:
        """Геттер имени товара.

        Returns:
            name: имя товара.
        """

        return self.__name

    def get_count(self) -> int:
        """Геттер количества товара.

        Returns:
            quantity: Количество товара.
        """

        return self.__count

    def get_state(self) -> str:
        """Геттер состояния товара.

        Returns:
            state: Состояние товара.
        """

        return self.__state

    def get_distributor(self) -> str:
        """Геттер поставщика товара.

        Returns:
            supplier: Поставщик товара.
        """

        return self.__distributor

    def get_manufacturer(self) -> str:
        """Геттер производителя товара.

        Returns:
            supplier: Производитель товара.
        """

        return self.__manufacturer

    def get_price(self) -> Decimal:
        """Геттер стоимости товара.

        Returns:
            price: Стоимость товара.
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.

        Returns:
            location: Местоположение товара.
        """

        return self.__location

    def get_city(self) -> str:
        """Геттер категории товара.

        Returns:
            city: Город товара.
        """

        return self.__city

    def set_id(self, id: str) -> None:
        """Сеттер id товара.

        Args:
            id: id товара
        """

        try:
            id = str(id)

        except TypeError:
            print("Ошибка! ID должен быть строковым числом")

        else:
            self.__id = id
            print('✔')

    def set_name(self, name: str) -> None:
        """Сеттер имени товара.

        Args:
            name: Наименование товара.
        """

        self.__name = name
        print('✔')

    def set_count(self, count: int) -> None:
        """Сеттер количества товара.

        Args:
            count: Количество товара.
        """

        try:
            count = int(count)

            if count > 0:
                self.__count = count
                print('✔')
            else:
                print("Введено некорректное значение!")
        except ValueError:
            print("Введено некорректное значение!")

    def set_state(self, state: str) -> None:
        """Сеттер состояния товара.

        Args:
            state: Состояние товара.
        """

        state = state.lower()

        if state == "списано":
            if self.__state in ["принято к учёту", "состоит на учёте"]:
                self.__state = state
                print("Успешно списано")
            else:
                print("Товар не числится на учёте")
        else:
            self.__state = state
            print("Статус успешно изменён")

    def set_distributor(self, distributor: str) -> None:
        """Сеттер поставщика товара.

        Args:
            supplier: Поставщик товара.
        """

        self.__distributor = distributor
        print('✔')

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя товара.

        Args:
            manufacturer: Производитель товара.
        """

        self.__manufacturer = manufacturer
        print('✔')

    def set_price(self, price: Decimal) -> None:
        """Сеттер стоимости товара.

        Args:
            price: Стоимость товара.
        """

        if type(price) == Decimal:
            if price >= 0:
                self.__price = price
                print('✔')
            else:
                print("Введено некорректное значение!")
                raise ValueError
        else:
            print("Введено некорректное значение!")
            raise TypeError

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара.

        Args:
            location: Местоположение товара.
        """

        self.__location = location
        print('✔')

    def set_city(self, city: str) -> None:
        """Сеттер города товара.

        Args:
            city: Город товара.
        """

        self.__city = city
        print('✔')

    def set_from_str(self,line: str) -> None:
        """Заполнение объекта товара из строки TXT файла.

        Args:
            line: Строка с данными о товаре.
        """

        elements = line.split(';')

        self.set_id(elements[1])
        self.set_name(elements[2])
        self.set_count(int(elements[3]))
        self.set_state(elements[4])
        self.set_distributor(elements[5])
        self.set_manufacturer(elements[6])
        self.set_price(Decimal(elements[7].split()[0]))
        self.set_location(elements[8])
        self.set_city(elements[9])

    def set_from_dict(self, data: dict) -> None:
        """Заполнение объекта товара из словаря.

        Args:
            data: Словарь с данными о товаре.
        """

        self.set_id(data['id'])
        self.set_name(data['name'])
        self.set_count(int(data['count']))
        self.set_state(data['state'])
        self.set_distributor(data['distributor'])
        self.set_manufacturer(data['manufacturer'])
        self.set_price(Decimal(data['price']))
        self.set_location(data['location'])
        self.set_city(data['city'])

    def to_dict(self) -> dict:
        """Преобразование объекта товара в словарь.

        Returns:
            dict: Словарь с данными товара.
        """

        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'count': self.get_count(),
            'state': self.get_state(),
            'distributor': self.get_distributor(),
            'manufacturer': self.get_manufacturer(),
            'price': self.get_price(),
            'location': self.get_location(),
            'city': self.get_city(),
        }