# Шифр Мирабо

class MirabeauCipher:

    def __init__(self):
        self.alphabet = self.create_an_alphabet()

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

    def encryption_2x(self, text: str):
        cipher1 = self.encryption(text)
        cipher2 = []
        for i in range(len(cipher1) - 1):
            cipher2.append(float(f'{(cipher1[i] * cipher1[i + 1]):.2f}'))
        last = cipher1[-1]
        for i in cipher2:
            last += i
        cipher2.append(last)
        return cipher2



    # Дешифровка
    def decryption(self, cipher: list):
        decrypted_text = ""
        for encrypted_letter in cipher:
            if encrypted_letter == 0:
                decrypted_text += ' '
                continue
            encrypted_letter *= 10
            i = int(encrypted_letter // 10 - 1)
            j = int(encrypted_letter % 10 - 1)
            decrypted_text += self.alphabet[i][j]
        return decrypted_text

    def decryption_2x(self, cipher: list):
        last = cipher[-1]
        for i in range(len(cipher) - 1):
            last -= cipher[i]
        cipher[-1] = float(f'{last:.1f}')
        for i in range(len(cipher) - 1, 0, -1):
            cipher[i - 1] = cipher[i - 1] / cipher[i]
        return cipher

    def create_an_alphabet(self):
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

