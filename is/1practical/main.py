# Шифр Мирабо


class MirabeauCipher:

    def __init__(self, alphabet):
        self.alphabet = alphabet

    # Шифровка
    def encryption(self, text: str):
        cipher = []
        for symbol in text:
            if symbol == ' ':
                cipher.append(0)
            group_num = 1
            for group in self.alphabet:
                if symbol in group:
                    encrypted_letter = group_num + (group.index(symbol) + 1) / 10
                    cipher.append(encrypted_letter)
                group_num += 1
        return cipher

    def decryption(self, cipher: list):
        decrypted_text = ""
        for encrypted_letter in cipher:

        return decrypted_text


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
    cipher = MirabeauCipher(alphabet)
    cipher.encryption("питон нигга")


if __name__ == '__main__':
    main()
