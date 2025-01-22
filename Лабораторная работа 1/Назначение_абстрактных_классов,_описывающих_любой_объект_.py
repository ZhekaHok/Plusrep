import doctest
from abc import ABC, abstractmethod


class Shape(ABC):
    def init(self, color: str):
        """
        Создание и подготовка к работе объекта "Фигура"

        :param color: Цвет фигуры

        Примеры:
        >>> shape = Shape("red")  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """
        Вычисление площади фигуры.

        :return: Площадь фигуры
        """
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вычисление периметра фигуры.

        :return: Периметр фигуры
        """
        ...


class Circle(Shape):
    def init(self, radius: float, color: str):
        """
        Создание и подготовка к работе объекта "Круг"

        :param radius: Радиус круга
        :param color: Цвет круга

        Примеры:
        >>> circle = Circle(5, "blue")  # инициализация экземпляра класса
        """
        super().init(color)
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисление площади круга.

        :return: Площадь круга

        Примеры:
        >>> circle = Circle(5, "blue")
        >>> circle.area()
        78.53981633974483
        """
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """
        Вычисление периметра круга.

        :return: Периметр круга

        Примеры:
        >>> circle = Circle(5, "blue")
        >>> circle.perimeter()
        31.41592653589793
        """
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def init(self, width: float, height: float, color: str):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        :param color: Цвет прямоугольника

        Примеры:
        >>> rectangle = Rectangle(4, 6, "green")  # инициализация экземпляра класса
        """
        super().init(color)
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Вычисление площади прямоугольника.

        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(4, 6, "green")
        >>> rectangle.area()
        24.0
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Вычисление периметра прямоугольника.

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(4, 6, "green")
        >>> rectangle.perimeter()
        20.0
        """
        return 2 * (self.width + self.height)

