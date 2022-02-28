/*!
 * \file ChildProgram.c
 * \brief Дочерняя программа
 *
 * Данная программа выводит число прописью
 */
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

#define THERE_IS_NO_REMAINDER 0
#define HUNDRED 0
#define TEN 2
#define UNIT 1
#define MILLION 7
#define FIRST_ITERATION 0
#define SINGLE_DIGIT_NUMBER 1
#define CORRECT_NUMBER 1


/*!
 * @brief Массив структур
 * @details Содержит прописи чисел от тысячи
 */
struct cases{
    char* one;
    char* two;
    char* many;
} w_in_cases[] = {{"", "", ""},
                  {"тысяча", "тысячи", "тысяч"},
                  {"миллион", "миллиона", "миллионов"},
                  {"миллиард", "миллиарда", "миллиардов"},
                  {"триллион", "триллиона", "триллионов"}
};


/*!
 * @brief Массив структур
 * @details Содержит прописи чисел до тысячи
 */
struct unit{
    char* one[2];
    char* two;
    char* dec;
    char* hun;
} units[] = {{{"", ""}, "десять", "", ""},
             {{"один", "одна"}, "одиннадцать", "десять", "сто"},
             {{"два", "две"}, "двенадцать", "двадцать", "двести"},
             {{"три", "три"}, "тринадцать", "тридцать", "триста"},
             {{"четыре", "четыре"}, "четырнадцать", "сорок", "четыреста"},
             {{"пять", "пять"}, "пятнадцать", "пятьдесят", "пятьсот"},
             {{"шесть", "шесть"}, "шестнадцать", "шестьдесят", "шестьсот"},
             {{"семь", "семь"}, "семнадцать", "семьдесят", "семьсот"},
             {{"восемь", "восемь"}, "восемнадцать", "восемьдесят", "восемьсот"},
             {{"девять", "девять"}, "девятнадцать", "девяносто", "девятьсот"}
};


int degree[] = {1, 10, 100, 1000, 10000,
                100000, 1000000, 10000000, 100000000, 1000000000};


/*!
 * @brief Функция ввода строки из потока ввода
 *
 * @details Считывает строку, введённую пользователем
 * @param text - Сообщение пользователю
 * @return Строку
 */
char* input(char* text)
{
    printf("%s", text);
    char *str = (char *)malloc(sizeof(char));
    str[0] = '\0';
    int lenght = 1;
    char cur_char = 0;
    fflush(stdin);
    while ((cur_char = getc(stdin)) != '\n')
    {
        str[lenght - 1] = cur_char;
        lenght++;
        str = (char *)realloc(str, lenght);
    }
    str[lenght - 1] = '\0';
    return str;
}

/*!
 * @brief Функция проверки строки
 * @details Проверяет, является ли введённая пользователем строка числом
 * @param str - Проверяемая строка
 * @return 1 - если строка является числом
 * @return 0 - если ввод некорректен или строка не является числом
 */
int isnumber(char* str)
{
    int k = 0, len = strlen(str);

    for (int i = 0; i < len; i++)
    {
        if(len == SINGLE_DIGIT_NUMBER & str[0] == '0')
            return 1;
        if((str[i] == '-' | str[i] == '+') & (i == FIRST_ITERATION))
            continue;
        if(str[i] == '0' & k <= 0)
            k--;
        if(str[i] != '0' & k >= 0)
            k++;
        if(!isdigit(str[i]) | (k < 0))
            return 0;
    }
    return 1;
}


/*!
 * @brief Функция проверки числа на максимально/минимально возможное для int
 * @param str Строка, содержащая число
 * @return 1 - если число входит в диапазон
 * @return 0 - если не входит в диапазон
 */
int check_limit(char* str)
{
    int figure, sign = 1, len = strlen(str);
    long long int number = 0;
    for(int i = 0; i < strlen(str); i++)
    {
        if(str[i] == '-' & i == FIRST_ITERATION)
        {
            sign = -1;
            len--;
            continue;
        }
        if(str[i] == '+' & i == FIRST_ITERATION)
        {
            len--;
            continue;
        }
        if(len > 10)
            return 0;
        figure = (int)str[i] - 48;
        if(len == 10 & figure > 2)
            return 0;
        number += figure * degree[len - 1];
        len--;
    }
    number *= sign;
    if(number > INT_MAX | number < INT_MIN)
        return 0;
    return 1;
}


/*!
 * @brief Функция вывода числа строкой
 * @param str - Строка, содержащая число
 */
void number_in_words(char* str)
{
    int len_str = strlen(str), figure;

    if(len_str == SINGLE_DIGIT_NUMBER & str[0] == '0')
    {
        printf("%s ", "ноль");
        return;
    }
    for (int i = 0; i < strlen(str);)
    {
        if(len_str == THERE_IS_NO_REMAINDER)
            return;
        if (str[i] == '-' & i == FIRST_ITERATION)
        {
            printf("минус ");
            len_str--;
            i++;
            continue;
        }
        if (str[i] == '+' & i == FIRST_ITERATION)
        {
            printf("плюс ");
            len_str--;
            i++;
            continue;
        }
        int three = len_str % 3;
        if(three == THERE_IS_NO_REMAINDER)
            three = 3;
        int len1 = three;
        for (int j = i; j < (i + len1); j++)
        {
            figure = (int) str[j] - 48;

            if (three % 3 == HUNDRED & figure != 0)
                printf("%s ", units[figure].hun);
            if (three % 3 == UNIT & figure != 0)
            {
                if (i == FIRST_ITERATION & len_str >= MILLION)
                    printf("%s ", units[figure].one[0]);
                else if (len_str == UNIT)
                    printf("%s ", units[figure].one[0]);
                else
                    printf("%s ", units[figure].one[1]);
            }
            if (three % 3 == TEN & str[j] == '1' & str[j + 1] != '0')
            {
                figure = (int) str[j + 1] - 48;
                if(figure != 0)
                {
                    printf("%s ", units[figure].two);
                    if (three <= 3)
                        return;
                }
            } else if (three % 3 == TEN & figure != 0)
                printf("%s ", units[figure].dec);
            three--;
            len_str--;
            if(len_str % 3 == THERE_IS_NO_REMAINDER & figure == 1)
                printf("%s ", w_in_cases[len_str / 3].one);
            else if(len_str % 3 == THERE_IS_NO_REMAINDER & figure >= 2 & figure <= 4)
                printf("%s ", w_in_cases[len_str / 3].two);
            else if(len_str % 3 == THERE_IS_NO_REMAINDER & figure >= 5)
                printf("%s ", w_in_cases[len_str / 3].many);
        }
        i += len1;
    }
}

/*!
 * @brief Основная функция
 */
int main(){
    char* str;
    int check;
    str = input("Введите строку: ");
    check = check_limit(str);
    if(check == 0)
    {
        printf("Число не входит в диапазон от минимального до максимального значения int");
    } else if(isnumber(str) == CORRECT_NUMBER)
    {
        printf("Результат: ");
        number_in_words(str);
    } else
        puts("Некорректный ввод");

    free(str);
    return 0;
}
