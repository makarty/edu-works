from PIL import Image, ImageDraw

from Quadrant import Quadrant




class QuadTree:
    """
    Квадродеревья....
    """

    def __init__(self, image, max_depth, transition_threshold) -> None:
        """
        Инициализация экземпляра
        :param image: картинка или область
        """
        self.max_depth = max_depth
        self.transition_threshold = transition_threshold
        self.root = Quadrant(image, image.getbbox(), 0)
        self.width, self.height = image.size
        # Указываем начальную глубину
        self.depth = 0
        self.start(image)

    def start(self, image) -> None:
        """
        Создание начального узла
        :param image: Картинка
        :return:
        """
        # Запускаем рекурсивную функцию
        self.build(self.root, image)

    def build(self, root, image) -> None:
        """
        Рекурсивная функция построения квадродерева, можно даже сказать ГЛАВНАЯ ФУНКЦИЯ
        :param root: Текущий узел
        :param image: Картинка или область
        :return:
        """
        # Если является листом - порог перехода квадранта меньше заданного или уже слишком большая глубина
        if root.depth >= self.max_depth or root.transition <= self.transition_threshold:
            if root.depth > self.depth:
                self.depth = root.depth
            root.leaf = True
            return
        # Делим квадрант
        root.split_quadrant(image)
        for children in root.children:
            self.build(children, image)

    def create_image(self, custom_depth, show_lines=False):
        """
        Рисование картинки на определенной глубине
        :param custom_depth:
        :param show_lines:
        :return:
        """
        # Создаем пустую картинку с размерами
        image = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.width, self.height), (0, 0, 0))

        leaf_quadrants = self.get_leaf_quadrants(custom_depth)

        # Рисуем для каждого листа прямоугольник
        for quadrant in leaf_quadrants:
            if show_lines:
                draw.rectangle(quadrant.border_box, quadrant.colour, outline=(0, 0, 0))
            else:
                draw.rectangle(quadrant.border_box, quadrant.colour)

        return image

    def get_leaf_quadrants(self, depth):
        """
        Получение конечных областей (листьев)
        :param depth: глубина
        :return:
        """
        if depth > self.depth:
            raise ValueError('Вы хотите спалить комп ? Сделайте меньше глубину')

        quadrants = []

        # Запускаем
        self.recursive_search(self, self.root, depth, quadrants.append)
        return quadrants

    def recursive_search(self, tree, quadrant, max_depth, append_leaf) -> None:
        """
        Рекурсивный поиск дочернего квадранта без наследников(листа)
        :param tree: Само дерево( объекл класса QuadTree)
        :param quadrant: Квадрант дерева
        :param max_depth: максимальная глубина заданная пользователем
        :param append_leaf: список куда будем закидывать итоговые листья
        :return:
        """
        print(tree)
        # Добавляем квадрант если он - конечная область дерева( лист)
        if quadrant.leaf or quadrant.depth == max_depth:
            append_leaf(quadrant)
        # Если нет, то продолжаем искать
        elif quadrant.children is not None:
            for child in quadrant.children:
                self.recursive_search(tree, child, max_depth, append_leaf)

    def create_gif(self, file_name, duration=1000, loop=0, show_lines=False) -> None:
        """
        Создание гифки
        :param file_name: Название файла который необходимо создать
        :param duration: Длительность гифки
        :param loop: зацикленность
        :param show_lines: булево значение, показывать или не показывать очертания прямоугольников
        :return:
        """
        gif = []
        for i in range(self.depth):
            img = self.create_image(i, show_lines=show_lines)
            gif.append(img)
        gif[-1].save(
            file_name,
            save_all=True,
            append_images=gif[-1:0:-1],
            duration=duration, loop=loop)

