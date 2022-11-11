"""main файл"""
import argparse
import os.path
import colorama
from multiprocessing import Pool
from levensh_dist import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-str", dest="string", type=str, help="Строка")
    parser.add_argument("-substr", dest="sub_string", nargs="+", type=str, help="подстрока")
    parser.add_argument("-cs", dest="case_sensitivity", type=bool, default=False, help="Регистр")
    parser.add_argument("-met", dest="method", type=str, default="first", help="'first'поиск справа,'last'поиск слева")
    parser.add_argument("-mis", dest="mistake", type=int, default=1, help="количество ошибок")
    parser.add_argument("-k", dest="k", type=int, default=None, help="количество поисков")
    args, unknownargs = parser.parse_known_args()
    colorama.init()
    if args.string == "":
        print("Ошибка. Пустая строка")
        return
    if isinstance(args.sub_string, list):
        args.sub_string = " ".join(args.sub_string)
    if args.string.endswith(".txt"):
        if not os.path.exists(args.string):
            raise FileNotFoundError
        with open(args.string, encoding="UTF-8") as f:
            args.string = f.read()
    if not args.case_sensitivity:
        args.string = args.string.lower()
        args.sub_string = args.sub_string.lower()
    str_dict, sub_list = {}, [args.sub_string]
    print(sub_list)
    with Pool(processes=len(sub_list)) as proc:
        for substring in sub_list:
            print(substring)
            res = proc.apply(func=search_substring, args=(args.string, substring, args.mistake))
            str_dict.update(res)
    print(str_dict)
    word_dict = {}
    for key in str_dict:
        list_dict = []
        for k in str_dict:
            if str_dict[k] == str_dict[key]:
                list_dict.append(k)
            word_dict[str_dict[key]] = list_dict
    if args.method == "last":
        for key in word_dict:
            word_dict[key].reverse()
    if args.k:
        for key in word_dict:
            word_dict[key] = word_dict[key][:args.k]
    print(word_dict)
    del_list, norm_list, del_fin_list, fin_list = [], [], [], []
    for key in word_dict:
        if lev_dist(args.sub_string, str(key)) <= 1:
            norm_list.append(key)
        else:
            del_list.append(key)
    for i in norm_list:
        for j in del_list:
            if lev_dist(j, i) > 1:
                print(f'fin_list - {fin_list}')
                if j not in del_fin_list and j not in fin_list:
                    del_fin_list.append(j)
            else:
                fin_list.append(j)
    for i in del_fin_list:
        del word_dict[i]

    print(word_dict)
    with open("result.txt", "w") as f:
        for key in word_dict:
            f.write(f"{key}: {word_dict[key]}\n")
    text_color = ('\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m')
    all_values = list(word_dict.values())
    index_all = []
    for val in all_values:
        index_all.extend(val)
    index_color = 0
    print(len(index_all))
    j = 0
    if len(index_all) == 0:
        print(args.string)
    else:
        for i in index_all:
            if index_color >= len(text_color):
                index_color = 0
            index_str = len(args.string[:i])
            print(f"{j})\033[0m{args.string[:index_str]}{text_color[index_color]}{str_dict[i]}"
                  f"\033[0m{args.string[(index_str + len(str_dict[i])):]}\n")
            index_color += 1
            j += 1


if __name__ == '__main__':
    main()
