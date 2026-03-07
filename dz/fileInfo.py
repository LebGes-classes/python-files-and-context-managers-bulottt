from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    """Абстрактный класс сериализации объектов."""

    @abstractmethod
    def serialize_object(self, obj):
        """Сериализация одного объекта."""

        pass

    @abstractmethod
    def serialize_list(self, objects):
        """Сериализация списка объектов."""
        pass


class BaseDeserializer(ABC):
    """Абстрактный класс десериализации объектов."""

    @abstractmethod
    def deserialize_object(self):
        """Десериализоция одного объекта или списка."""

        pass


class FileInfo:
    """Класс хранения информации о файле."""

    def __init__(self, filename: str):
        """Конструктор класса FileInfo.

        Args:
            filename: Имя файла.
        """

        self._filename = filename
        self._format_of_file = None

    def get_filename(self) -> str:
        """Геттер имени файла.

        Returns:
            filename: Имя файла.
        """

        return self._filename

    def get_format_of_file(self) -> str:
        """Геттер формата файла.

        Returns:
            format: Формат файла.
        """

        return self._format_of_file

    def set_format_of_file(self, value: str) -> None:
        """Геттер формата файла.

        Returns:
            format: Формат файла.
        """

        self._format_of_file = value