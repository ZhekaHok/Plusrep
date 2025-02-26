class ElectronicDevice:
    """
    Базовый класс для всех электронных устройств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация электронного устройства.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param year: Год выпуска устройства.
        """
        self.__brand = brand  # Инкапсуляция: бренд устройства не должен изменяться напрямую
        self.__model = model  # Инкапсуляция: модель устройства не должна изменяться напрямую
        self.__year = year    # Инкапсуляция: год выпуска устройства не должен изменяться напрямую

    def power_on(self) -> str:
        """
        Метод, который включает устройство.
        Должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть переопределен в дочерних классах.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление электронного устройства.
        """
        return f"{self.__class__.__name__}(brand={self.__brand}, model={self.__model}, year={self.__year})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление электронного устройства.
        """
        return f"ElectronicDevice(brand={self.__brand!r}, model={self.__model!r}, year={self.__year!r})"
class Smartphone(ElectronicDevice):
    """
    Класс для смартфонов, наследуется от ElectronicDevice.
    """

    def __init__(self, brand: str, model: str, year: int, os: str) -> None:
        """
        Инициализация смартфона.

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param year: Год выпуска смартфона.
        :param os: Операционная система смартфона.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.__os = os  # Инкапсуляция: операционная система не должна изменяться напрямую

    def power_on(self) -> str:
        """
        Включает смартфон и возвращает сообщение.
        """
        return f"{self.__model} включен(а)!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление смартфона, включая операционную систему.
        """
        return f"{super().__str__()}, os={self.__os}"

    def install_app(self, app_name: str) -> str:
        """
        Устанавливает приложение на смартфон.

        :param app_name: Название приложения для установки.
        :return: Сообщение о том, что приложение установлено.
        """
        return f"Приложение {app_name} установлено на {self.__model}!"
class Laptop(ElectronicDevice):
    """
    Класс для ноутбуков, наследуется от ElectronicDevice.
    """

    def __init__(self, brand: str, model: str, year: int, ram: int) -> None:
        """
        Инициализация ноутбука.

        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param year: Год выпуска ноутбука.
        :param ram: Объем оперативной памяти в ГБ.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.__ram = ram  # Инкапсуляция: объем оперативной памяти не должен изменяться напрямую

    def power_on(self) -> str:
        """
        Включает ноутбук и возвращает сообщение.
        """
        return f"{self.__model} включен(а)!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление ноутбука, включая объем оперативной памяти.
        """
        return f"{super().__str__()}, ram={self.__ram}GB"

    def upgrade_ram(self, additional_ram: int) -> str:
        """
        Обновляет объем оперативной памяти ноутбука.

        :param additional_ram: Дополнительный объем оперативной памяти в ГБ.
        :return: Сообщение о том, что оперативная память обновлена.
        """