import json
from json import JSONDecodeError

from fileInfo import FileInfo, BaseSerializer, BaseDeserializer
from Product import Product


class JSONParser(FileInfo, BaseSerializer, BaseDeserializer):
    """Класс парсера JSON файла."""

    def __init__(self, filename: str):
        """Конструктор класса JSONParser.

        Args:
            filename: Имя файла.
        """

        super().__init__(filename)
        self.set_format_of_file('json')

    def serialize_list(self, products: list[Product]) -> None:
        """Сериализация списка товаров в JSON файл.

        Args:
            products: Список объектов Product.
        """

        data = {
            product.get_id(): product.to_dict()
            for product in products
        }

        path = f"{self.get_filename()}.{self.get_format_of_file()}"

        with open(path, 'w', encoding='utf-8') as fos:
            json.dump(data, fos, ensure_ascii=False, indent=4, default=str)

    def serialize_object(self, product: Product) -> None:
        """Сериализация одного товара.

        Args:
            product: Объект товара.
        """

        products = self.deserialize_object()

        updated = False
        for i, p in enumerate(products):
            if p.get_id() == product.get_id():
                products[i] = product
                updated = True

        if not updated:
            products.append(product)

        self.serialize_list(products)

    def deserialize_object(self, ids: list[str] | None = None) -> list[Product]:
        """Десериализация товаров из JSON файла.

        Args:
            ids: Список ID товаров (опционально).

        Returns:
            products: Список объектов Product.
        """

        products = []

        path = f"{self.get_filename()}.{self.get_format_of_file()}"

        try:
            with open(path, 'r', encoding='utf-8') as fos:
                data = json.load(fos)
        except (FileNotFoundError, JSONDecodeError):
            return products

        if ids:
            for pid in ids:
                if pid in data:
                    product = Product()
                    product.set_from_dict(data[pid])
                    products.append(product)
        else:
            for payload in data.values():
                product = Product()
                product.set_from_dict(payload)
                products.append(product)

        return products