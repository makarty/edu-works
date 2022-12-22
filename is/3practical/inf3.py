# -*- coding: utf-8 -*-
from itertools import cycle


def possible_key_len(msg: str, n_gramma: int = 3) -> list:
    for_NOD = {}
    for start in range(len(msg) - n_gramma - 1):
        for msg_start in range(start + n_gramma, len(msg) - n_gramma + 1):
            if msg[start:start + n_gramma] == msg[msg_start:msg_start + n_gramma]:
                if msg[start:start + n_gramma] not in for_NOD:
                    for_NOD[msg[start:start + n_gramma]] = []

                for_NOD[msg[start:start + n_gramma]].append(msg_start - start)

    keys = {}
    all_div, keys_list = [], []
    for k, v in for_NOD.items():
        divs = []
        for value in v:
            divs.extend([i for i in range(2, value + 1) if value % i == 0])

        keys[k] = divs
        all_div.extend(divs)
    probably_len = {}
    for i in all_div:
        if i not in probably_len and i <= 10:
            probably_len[i] = all_div.count(i)
    for k, v in probably_len.items():
        if v == max(probably_len.values()):
            keys_list.append(k)
    return keys_list


def separate(u: int, string: str) -> list:
    list_group, const_1, const_2 = [], 0, 0
    for i in range(u):
        list_group.append([])
        for j in range(len(string)):
            if (const_1 * u + const_2) < len(string):
                list_group[i].append(string[const_1 * u + const_2])
                const_1 += 1
        const_1 = 0
        const_2 += 1
    dict_group = {}
    for i in range(u):
        dict_group[i] = list_group[i]
    return dict_group


def frequency_analysis(msg: str, key_len: list) -> list:
    if isinstance(key_len, list):
        key_len = max(key_len)
    groups = separate(key_len, msg)

    frequencies = []
    for i in range(key_len):
        freq_group = {}
        for value in groups[i]:
            if value not in freq_group:
                freq_group[value] = groups[i].count(value)
        frequencies.append(freq_group)
    print(frequencies)
    return frequencies


def keyword(freq: list, key_len: int, alphabet: list) -> list:
    shifts = []
    for i in range(key_len):
        shifts.append(None)

    for col in range(1, key_len):
        mics = []
        for shift in range(len(alphabet)):
            tmp_freq = {}
            for k, v in freq[col].items():
                ind = alphabet.index(k)
                tmp_freq[alphabet[(ind + shift) % len(alphabet)]] = v
            mic = 0
            for k, v in freq[0].items():
                mic += (freq[0][k] * tmp_freq.get(k, 0))
            mic /= (sum(freq[0].values()) * sum(tmp_freq.values()))
            mics.append(mic)
            if 0.0529 <= mic <= 0.07:
                shifts[col] = shift
                break
        if shifts[col] == None:
            shifts[col] = (mics.index(max(mics)))
    return shifts


def key_get_shifts(alphabet: str, shifts: list) -> list:
    probable_keys = []
    for i in range(len(alphabet)):
        key = alphabet[i]
        for j in range(1, len(shifts)):
            key += alphabet[i - shifts[j]]
        probable_keys.append(key)
    return probable_keys


def decode(code_text: str, keytext: str, alp: str) -> str:
    return_str = ""
    j = 0
    for i in code_text:
        if j >= len(keytext):
            j = 0
        return_str += alp[alp.index(i) - alp.index(keytext[j]) % len(alp)]
        j += 1
    return return_str

def text_with_pun(string: str, string_no_pun: str, alphabet: str) -> str:
    text = ""
    j = 0
    for i in range(len(string)):
        if string[i] in alphabet:
            text += (string_no_pun[j])
            j += 1
        else:
            text += (string[i])
    return text


def applic():
    f = open("file.txt", mode='r', encoding='utf-8')
    string = f.read().lower()
    f.close()
    a = ord('а')
    string_alph = ''.join([chr(i) for i in range(a, a + 32)])
    words = "".join(filter(str.isalpha, string))
    words = words.lower()

    pkl = possible_key_len(words)
    if isinstance(pkl, list):
        pkl = max(pkl)
    f = frequency_analysis(words, pkl)
    shifts = keyword(f, pkl, string_alph)
    pk = key_get_shifts(string_alph, shifts)
    return pk


def enc(pk_l: str) -> str:
    f = open("file.txt", mode='r', encoding='utf-8')
    string = f.read().lower()
    f.close()
    words = "".join(filter(str.isalpha, string))
    a = ord('а')
    string_alph = ''.join([chr(i) for i in range(a, a + 32)])
    words = words.lower()

    decode_cipher = decode(words, pk_l, string_alph)

    return text_with_pun(string.lower(), decode_cipher, string_alph).upper()
