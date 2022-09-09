# Шифр Мирабо

# Шифровка
def encryption():
    pass


def decryption():
    pass


def mirabeau_cipher():
    pass


def create_an_alphabet():
    polybius_square = []
    cur_char = ord("а")
    for i in range(6):
        group = []
        for j in range(6):
            if i == 1 and j == 0:
                group.append("ё")
                continue
            if i == 5 and j > 2:
                group.append("null")
                continue
            group.append(chr(cur_char))
            cur_char += 1
        polybius_square.append(group)

    return polybius_square


def main():
    alphabet = create_an_alphabet()
    print(alphabet)


if __name__ == '__main__':
    main()
