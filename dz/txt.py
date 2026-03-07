from fileInfo import FileInfo, BaseDeserializer
from Product import Product


class TxtParser(FileInfo, BaseDeserializer):
    """Класс парсера TXT файла."""

    def __init__(self, filename: str):
        """Конструктор класса TxtParser.

        Args:
            filename: Имя файла.
        """

        super().__init__(filename)
        self.set_format_of_file('txt')

    def deserialize_object(self) -> list[Product]:
        """Десериализация объектов из TXT файла.

        Returns:
            products: Список объектов Product.
        """

        products = []

        path = f"{self.get_filename()}.{self.get_format_of_file()}"

        with open(path, 'r', encoding='utf-8') as fos:
            lines = fos.readlines()[1:]

        for line in lines:
            product = Product()
            product.set_from_str(line.strip())
            products.append(product)

        return products
