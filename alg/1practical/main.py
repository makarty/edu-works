from sys import argv

from PIL import Image

from QuadTree import QuadTree


def main() -> int:
    """
    Основная функция программы
    :return:  Код завершения
    :rtype: int
    """
    #image_path = "tiger.jpg"
    # image_path = "forest.jpg"
    image_path = "selected_picture.jpg"
    # Загружаем картинку
    image = Image.open(image_path)
    try:
        max_depth = int(argv[1])
        transition_threshold = int(argv[2])
        print(argv[1], argv[2])
    except:
        raise ValueError("Пользователь белбес, введите числа")
    if (2 < max_depth < 10) and (3 < transition_threshold < 45):
        pass
    else:
        raise ValueError("Вы хотите спалить комп ? ")
    print("Масимальная глубина - ", max_depth)
    print("Порог перехода - ", transition_threshold)
    # Создаем дерево
    quadtree = QuadTree(image, max_depth, transition_threshold)

    # Создаем картинку
    depth = 7
    image = quadtree.create_image(depth, show_lines=True)
    image.save("pict_output.jpg")
    # Создаем гифку

    # quadtree.create_gif("tiger_gif.gif", show_lines=True)
    quadtree.create_gif("gif_output.gif", show_lines=False)
    print("Done")
    return 0


if __name__ == '__main__':
    main()
