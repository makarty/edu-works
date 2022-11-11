import MathFunctions


class Quadrant:
    """
    Класс содержит в себе информацию о квадратнах
    """

    def __init__(self, image, border_box, depth) -> None:
        """
        Инициализация экземпляра
        :param image: картинка или область
        :param border_box: Координаты углов области
        :param depth: текущая глубина
        """
        self.border_box = border_box
        self.depth = depth
        self.children = None
        self.leaf = False
        # Вырезаем нужную область для дальнейшего использования и получаем гистограмму
        image = image.crop(border_box)
        # Строим гистограмму для получения границы перехода
        hist = image.histogram()
        # Получаем чернобелый порог перехода
        self.transition = MathFunctions.get_transition(hist)
        self.colour = MathFunctions.average_colour(image)

    def split_quadrant(self, image) -> None:
        """
        Функция деления квадранта на 4 дочерних
        :param image: Картинка или область
        :return:
        """
        left, top, width, height = self.border_box

        # Получаем середину каждой области для дальнейшего использования
        middle_x = left + (width - left) / 2
        middle_y = top + (height - top) / 2

        # Делим квадрант на 4 области
        upper_left = Quadrant(image, (left, top, middle_x, middle_y), self.depth + 1)
        upper_right = Quadrant(image, (middle_x, top, width, middle_y), self.depth + 1)
        bottom_left = Quadrant(image, (left, middle_y, middle_x, height), self.depth + 1)
        bottom_right = Quadrant(image, (middle_x, middle_y, width, height), self.depth + 1)

        # Записываем эти квадранты в потомки
        self.children = [upper_left, upper_right, bottom_left, bottom_right]
