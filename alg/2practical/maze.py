import random
import copy
from PIL import Image, ImageDraw


def predgraghp(lst, row, col):
    """
   Функция построение лабиринта в терминале в виде псевдографики
   :param lst: список списков, иначе лабиринт
   :type lst: list
   :param row: количество рядов
   :type row: int
   :param col: количество столбцов
   :type col: int
   :return: псевдографический лабиринт
   """
    lst_2 = copy.deepcopy(lst)
    rlud = [0,0,0,0]
    for x in range(row*2+1):
        for y in range(col*2+1):
            if lst[x][y] == 0:
                if x + 1 <= row*2:
                    if lst[x + 1][y] == 0:
                        rlud[3] = 1
                if x - 1 >= 0:
                    if lst[x - 1][y] == 0:
                        rlud[2] = 1
                if y + 1 <= col*2:
                    if lst[x][y + 1] == 0:
                        rlud[0] = 1
                if y - 1 >= 0:
                    if lst[x][y - 1] == 0:
                        rlud[1] = 1
                if (rlud[0] == 1) and (rlud[1] == 1) and (rlud[2] == 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╬'
                elif (rlud[0] != 1) and (rlud[1] == 1) and (rlud[2] != 1) and (rlud[3] != 1):
                    lst_2[x][y] = '═'
                elif (rlud[0] == 1) and (rlud[1] == 1) and (rlud[2] == 1) and (rlud[3] != 1):
                    lst_2[x][y] = '╩'
                elif (rlud[0] == 1) and (rlud[1] == 1) and (rlud[2] != 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╦'
                elif (rlud[0] == 1) and (rlud[1] == 1) and (rlud[2] != 1) and (rlud[3] != 1):
                    lst_2[x][y] = '═'
                elif (rlud[0] == 1) and (rlud[1] != 1) and (rlud[2] == 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╠'
                elif (rlud[0] == 1) and (rlud[1] != 1) and (rlud[2] == 1) and (rlud[3] != 1):
                    lst_2[x][y] = '╚'
                elif (rlud[0] == 1) and (rlud[1] != 1) and (rlud[2] != 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╔'
                elif (rlud[0] == 1) and (rlud[1] != 1) and (rlud[2] != 1) and (rlud[3] != 1):
                    lst_2[x][y] = '═'
                elif (rlud[0] != 1) and (rlud[1] == 1) and (rlud[2] == 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╣'
                elif (rlud[0] != 1) and (rlud[1] == 1) and (rlud[2] == 1) and (rlud[3] != 1):
                    lst_2[x][y] = '╝'
                elif (rlud[0] != 1) and (rlud[1] == 1) and (rlud[2] != 1) and (rlud[3] == 1):
                    lst_2[x][y] = '╗'
                elif (rlud[0] != 1) and (rlud[1] != 1) and (rlud[2] == 1) and (rlud[3] == 1):
                    lst_2[x][y] = '║'
                elif (rlud[0] != 1) and (rlud[1] != 1) and (rlud[2] == 1) and (rlud[3] != 1):
                    lst_2[x][y] = '║'
                elif (rlud[0] != 1) and (rlud[1] != 1) and (rlud[2] != 1) and (rlud[3] == 1):
                    lst_2[x][y] = '║'
                rlud = [0,0,0,0]
            else: lst_2[x][y] = ' '
    return lst_2


def maze(index_er, cell_dict, row, col, lst):
    """
   Функция построение пути
   :param index_er: список точек
   :type index_er: list
   :param cell_dict: словарь списков точек
   :type cell_dict: dict
   :param lst: список списков, иначе лабиринт
   :type lst: list
   :param row: количество рядов
   :type row: int
   :param col: количество столбцов
   :type col: int
   :return: решенный лабиринт
   :rtype lab: list
   """
    while len(index_er) != 1:
        index = random.randint(0, len(index_er) - 1)
        key = index_er[index]
        rand_wall = random.randint(1, 4)
        flag, count_random, count = 0, 0, len(cell_dict)
        i = 0
        while flag == 0:
            if rand_wall == 1:
                if cell_dict[key][i][0] + 2 < row and key != lst[cell_dict[key][i][0] + 2][
                    cell_dict[key][i][1]] and key != None:
                    lst_temp = cell_dict[key]
                    lst[cell_dict[key][i][0] + 1][cell_dict[key][i][1]] = key
                    lst_temp.extend(cell_dict[lst[cell_dict[key][i][0] + 2][cell_dict[key][i][1]]])
                    cell_dict[key] = lst_temp
                    key_del = lst[cell_dict[key][i][0] + 2][cell_dict[key][i][1]]
                    del cell_dict[lst[cell_dict[key][i][0] + 2][cell_dict[key][i][1]]]
                    index_er.remove(key_del)
                    flag = 1
            elif rand_wall == 2:
                if cell_dict[key][i][0] - 2 > 0 and key != lst[cell_dict[key][i][0] - 2][
                    cell_dict[key][i][1]] and key != None:
                    lst_temp = cell_dict[key]
                    lst[cell_dict[key][i][0] - 1][cell_dict[key][i][1]] = key
                    lst_temp.extend(cell_dict[lst[cell_dict[key][i][0] - 2][cell_dict[key][i][1]]])
                    cell_dict[key] = lst_temp
                    key_del = lst[cell_dict[key][i][0] - 2][cell_dict[key][i][1]]
                    del cell_dict[lst[cell_dict[key][i][0] - 2][cell_dict[key][i][1]]]
                    index_er.remove(key_del)
                    flag = 1
            elif rand_wall == 3:
                if cell_dict[key][i][1] - 2 > 0 and key != lst[cell_dict[key][i][0]][
                    cell_dict[key][i][1] - 2] and key != None:
                    lst_temp = cell_dict[key]
                    lst[cell_dict[key][i][0]][cell_dict[key][i][1] - 1] = key
                    lst_temp.extend(cell_dict[lst[cell_dict[key][i][0]][cell_dict[key][i][1] - 2]])
                    cell_dict[key] = lst_temp
                    key_del = lst[cell_dict[key][i][0]][cell_dict[key][i][1] - 2]
                    del cell_dict[lst[cell_dict[key][i][0]][cell_dict[key][i][1] - 2]]
                    index_er.remove(key_del)
                    flag = 1
            elif rand_wall == 4:
                if cell_dict[key][i][1] + 2 < col and key != lst[cell_dict[key][i][0]][
                    cell_dict[key][i][1] + 2] and key != None:
                    lst_temp = cell_dict[key]
                    lst[cell_dict[key][i][0]][cell_dict[key][i][1] + 1] = key
                    lst_temp.extend(cell_dict[lst[cell_dict[key][i][0]][cell_dict[key][i][1] + 2]])
                    cell_dict[key] = lst_temp
                    key_del = lst[cell_dict[key][i][0]][cell_dict[key][i][1] + 2]
                    del cell_dict[lst[cell_dict[key][i][0]][cell_dict[key][i][1] + 2]]
                    index_er.remove(key_del)
                    flag = 1
            if flag == 0:
                if rand_wall < 4:
                    rand_wall += 1
                    count_random += 1
                else:
                    rand_wall = 1
            else:
                for k, v in cell_dict.items():
                    for l in range(len(v)):
                        lst[v[l][0]][v[l][1]] = k
            if count_random > 4:
                if i + 1 < len(cell_dict[key]):
                    i += 1
                    count_random = 0
                else:
                    flag = 1


def create_image(row, col, lst):
    """
   Функция построение картинки
   :param lst: список списков, иначе лабиринт
   :type lst: list
   :param row: количество рядов
   :type row: int
   :param col: количество столбцов
   :type col: int
   :return: -
   """
    img = Image.new('RGBA', (row * 2 + 1, col * 2 + 1), 'white')
    draw = ImageDraw.Draw(img)  # создание инструмента для рисования
    width = img.size[0]  # ширина
    height = img.size[1]  # высота
    i = 0
    try:
        for y in range(height):
            for x in range(width):
                if lst[x][y] == 0:
                    image_1 = (0, 0, 0)
                else:
                    image_1 = (255, 255, 255)
                draw.point((x, y), image_1)  # замена пикселей
                i += 1
    except IndexError:
        pass
    img.save("photo.png")


def wave(x, y, cur, n, m, lab):
    """
     Функция волнового алгоритма
     :param x: координата x начальной точки
     :type x: int
     :param y: координата y начальной точки
     :type y: int
     :param cur: текущее значение
     :type cur: int
     :param n: количество рядов
     :type n: int
     :param m: количество столбцов
     :type m: int
     :param lab: список списков, иначе лабиринт
     :type lab: list
     :return: список точек пути
     """
    lab[x][y] = cur
    if y + 1 < m:
        if lab[x][y + 1] == 1 or (lab[x][y + 1] != 0 and lab[x][y + 1] > cur):
            wave(x, y + 1, cur + 1, n, m, lab)
    if x + 1 < n:
        if lab[x + 1][y] == 1 or (lab[x + 1][y] != 0 and lab[x + 1][y] > cur):
            wave(x + 1, y, cur + 1, n, m, lab)
    if x - 1 >= 0:
        if lab[x - 1][y] == 1 or (lab[x - 1][y] != 0 and lab[x - 1][y] > cur):
            wave(x - 1, y, cur + 1, n, m, lab)
    if y - 1 >= 0:
        if lab[x][y - 1] == 1 or (lab[x][y - 1] != 0 and lab[x][y - 1] > cur):
            wave(x, y - 1, cur + 1, n, m, lab)
    return lab


def restore(x, y, cur, n, m, lab, way):
    """
    Функция построение пути
    :param x: координата x конечной точки
    :type x: int
    :param y: координата y конечной точки
    :type y: int
    :param cur: текущее значение
    :type cur: int
    :param n: количество рядов
    :type n: int
    :param m: количество столбцов
    :type m: int
    :param lab: список списков, иначе лабиринт
    :type lab: list
    :param way: Строка в которой буддет производиться поиск
    :type way: list
    :return: список точек пути
    """

    if x - 1 >= 0:
        if (lab[x - 1][y] != 0 and lab[x - 1][y] < cur):
            way.append((x - 1, y))
            restore(x - 1, y, cur - 1, n, m, lab, way)
    if y - 1 >= 0:
        if (lab[x][y - 1] != 0 and lab[x][y - 1] < cur):
            way.append((x, y - 1))
            restore(x, y - 1, cur - 1, n, m, lab, way)
    if y + 1 < m:
        if (lab[x][y + 1] != 0 and lab[x][y + 1] < cur):
            way.append((x, y + 1))
            restore(x, y + 1, cur - 1, n, m, lab, way)
    if x + 1 < n:
        if (lab[x + 1][y] != 0 and lab[x + 1][y] < cur):
            way.append((x + 1, y))
            restore(x + 1, y, cur - 1, n, m, lab, way)
    return way


def solve_maze(cells, row, col, lst):
    """
    Функция решения лабиринта
    :param cells: список точек
    :type cells: list
    :param lst: список списков, иначе лабиринт
    :type lst: list
    :param row: количество рядов
    :type row: int
    :param col: количество столбцов
    :type col: int
    :return: решенный лабиринт
    :rtype lab: list
    """

    x1, y1 = cells[0][0], cells[0][1]
    n = row * 2 + 1
    m = col * 2 + 1
    lab = wave(x1, y1, 1, n, m, lst)
    return lab


def restore_way(cells, lab, row, col):
    """
    Функция построение пути
    :param cells: список точек
    :type cells: list
    :param lab: список списков, иначе лабиринт
    :type lab: list
    :param row: количество рядов
    :type row: int
    :param col: количество столбцов
    :type col: int
    :return: список точек пути
    """
    last_dot = cells[-1]
    way = []
    n = row * 2 + 1
    m = col * 2 + 1
    restore(last_dot[0], last_dot[1], lab[last_dot[0]][last_dot[1]], n, m, lab, way)
    way.append(cells[-1])
    way.append(cells[0])
    return way


def create_way_image(way):
    """
    Функция создания картинки с решением
    :param way: Строка в которой буддет производиться поиск
    :type way: list
    :return: -
    """
    img = Image.open("photo.png")  # открытие файла
    draw = ImageDraw.Draw(img)  # создание инструмента для рисования
    # width = img.size[0]  # ширина
    # height = img.size[1]  # высота
    i = 0
    try:
        for i in range(len(way)):
            x = way[i][0]
            y = way[i][1]
            image_1 = (255, 0, 0)
            draw.point((x, y), image_1)
    except IndexError:
        pass
    img.save("solve.png")


def load_image():
    """
    Функция загрузки изображения
    :return:
    """
    try:
        img = Image.open("photo.png")
    except FileNotFoundError:
        print('Отустствует файл или неверный формат')
    width = img.size[0]
    height = img.size[1]
    obj = img.load()  # загрузка пикселя
    list_decryption = []
    try:
        for x in range(width):
            list_decryption.append([])
            for y in range(height):
                if obj[x, y] == (0, 0, 0, 255):
                    list_decryption[x].append(0)
                else:
                    list_decryption[x].append(1)
    except IndexError:
        pass
    img.save("photo.png")
    return list_decryption


def main():
    while True:
        print("1) Создать лабиринт")
        print("2) Загрузить лабиринт")
        print("3) Выйти")
        while not (choice := input('выбор: ')).isdigit() or int(choice) == 0 or int(choice) > 3:
            print('ошибка, введите номер команды')
        choice = int(choice)
        if choice == 1:
            while not (row := input('количество рядов: ')).isdigit() or int(row) == 0 or int(row) > 50:
                print('ошибка, введите число')
            while not (col := input('количество столбцов: ')).isdigit() or int(col) == 0 or int(col) > 50:
                print('ошибка, введите число')
            row = int(row)
            col = int(col)
            lst = []
            num = 1
            for i in range(row * 2 + 1):
                lst.append([])
                for j in range(col * 2 + 1):
                    if (i % 2 != 0) and (j % 2 != 0):
                        lst[i].append(num)
                        num += 1
                    else:
                        lst[i].append(0)
            num = 1
            cell_dict = {}
            for i in range(row):
                for j in range(col):
                    cell_dict.update({num: [(i * 2 + 1, j * 2 + 1)]})
                    num += 1
            cells = []
            index_er = []
            for i in range(col * row):
                index_er.append(i + 1)
            for i, j in cell_dict.items():
                cells.append(j[0])

            maze(index_er, cell_dict, row, col, lst)

            for i in range(row * 2 + 1):
                for j in range(col * 2 + 1):
                    if (i % 2 != 0) and (j % 2 != 0):
                        lst[i][j] = lst[1][1]
                    if lst[i][j] != 0:
                        lst[i][j] = 1

            lst_2 = predgraghp(lst, row, col)
            
            for x in range(row * 2 + 1):
                list_print_psevdo = ''.join(lst_2[x])
                print(list_print_psevdo)

            create_image(row, col, lst)

            lab = solve_maze(cells, row, col, lst)
            way = restore_way(cells, lab, row, col)
            create_way_image(way)

        elif choice == 2:
            lst = load_image()
            row = (len(lst) - 1)//2
            col = (len(lst[0]) - 1)//2
            cells = [(1, 1), (row*2-1, col*2-1)]
            lab = solve_maze(cells, row, col, lst)
            way = restore_way(cells, lab, row, col)
            create_way_image(way)
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
