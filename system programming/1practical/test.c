/*!
 * \file test.c
 *
 * Файл с тестами
 */
#include <CUnit/CUnit.h>
#include <CUnit/Console.h>
#include <CUnit/TestDB.h>
#include <CUnit/Basic.h>
#include <ctype.h>
#include <malloc.h>


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


/*!
 * @brief Функция записи числа просписью
 * @param str Строка с числом
 * @return Строка пропись числа
 */
char* number_in_words(char* str)
{
    int len_str = strlen(str), d, length = 1;
    char* words = (char*) malloc(sizeof(char));

    if(len_str == 1 & str[0] == '0')
    {
        length += strlen("ноль");
        words = (char*) realloc(words, length);
        strcpy(words, "ноль");
        return words;
    }
    for (int i = 0; i < strlen(str);) {
        if(len_str == 0)
            return words;
        if (str[i] == '-' & i == 0)
        {
            length += strlen("минус");
            words = (char*)realloc(words, length);
            strcat(words, "минус");
            len_str--;
            continue;
        }
        if (str[i] == '+' & i == 0)
        {
            len_str--;
            continue;
        }
        int three = len_str % 3;
        if(three == 0)
            three = 3;
        int len1 = three;
        for (int j = i; j < (i + len1); j++) {
            d = (int) str[j] - 48;

            if (three % 3 == 0 & d != 0)
            {
                if(length > 1)
                {
                    length = strlen(" ");
                    words = (char*)realloc(words, length);
                    strcat(words, " ");
                }

                length = strlen(units[d].hun);
                words = (char*)realloc(words, length);
                strcat(words, units[d].hun);
            }
            if (three % 3 == 1 & d != 0)
                if (i == 0 & len_str >= 7)
                {
                    if(length > 1)
                    {
                        length += strlen(" ");
                        words = (char*)realloc(words, length);
                        strcat(words, " ");
                    }

                    length += strlen(units[d].one[0]);
                    words = (char*)realloc(words, length);
                    strcat(words, units[d].one[0]);
                }
                else if (len_str == 1)
                {
                    if(length > 1)
                    {
                        length += strlen(" ");
                        words = (char*)realloc(words, length);
                        strcat(words, " ");
                    }

                    length += strlen(units[d].one[0]);
                    words = (char*)realloc(words, length);
                    strcat(words, units[d].one[0]);
                }
                else
                {
                    if(length > 1)
                    {
                        length += strlen(" ");
                        words = (char*)realloc(words, length);
                        strcat(words, " ");
                    }

                    length += strlen(units[d].one[1]);
                    words = (char*)realloc(words, length);
                    strcat(words, units[d].one[1]);
                }
            if (three % 3 == 2 & str[j] == '1' & str[j + 1] != '0')
            {
                d = (int) str[j + 1] - 48;
                if(d != 0)
                {
                    if(length > 1)
                    {
                        length += strlen(" ");
                        words = (char*)realloc(words, length);
                        strcat(words, " ");
                    }

                    length += strlen(units[d].two);
                    words = (char*)realloc(words, length);
                    strcat(words, units[d].two);
                    if (three <= 3)
                        return words;
                }
            } else if (three % 3 == 2 & d != 0)
            {
                if(length > 1)
                {
                    length += strlen(" ");
                    words = (char*)realloc(words, length);
                    strcat(words, " ");
                }

                length += strlen(units[d].dec);
                words = (char*)realloc(words, length);
                strcat(words, units[d].dec);
            }
            three--;
            len_str--;
            if(len_str % 3 == 0 & d == 1)
            {
                length += strlen(" ");
                words = (char*)realloc(words, length);
                strcat(words, " ");

                length += strlen(w_in_cases[len_str / 3].one);
                words = (char*)realloc(words, length);
                strcat(words, w_in_cases[len_str / 3].one);
            }
            else if(len_str % 3 == 0 & d >= 2 & d <= 4)
            {
                length += strlen(" ");
                words = (char*)realloc(words, length);
                strcat(words, " ");

                length += strlen(w_in_cases[len_str / 3].two);
                words = (char*)realloc(words, length);
                strcat(words, w_in_cases[len_str / 3].two);
            }
            else if(len_str % 3 == 0 & d >= 5)
            {
                length += strlen(" ");
                words = (char*)realloc(words, length);
                strcat(words, " ");

                length += strlen(w_in_cases[len_str / 3].many);
                words = (char*)realloc(words, length);
                strcat(words, w_in_cases[len_str / 3].many);
            }
        }
        i += len1;
    }
    char* words1 = (char*) malloc((strlen(words)/2 + 1) * sizeof(char));
    strcpy(words1, words);
    return words1;
}


/*!
 * @brief Функция проверки числа в строке
 * @param str Строка с числом
 * @return 1 если строка содержит число
 * 0 если ввод некорректен или неправильно записано число
 */
int isnumber(char* str){
    int k = 0, len = strlen(str);

    for (int i = 0; i < len; i++)
    {
        if(len == 1 & str[0] == '0')
            return 1;
        if((str[i] == '-' | str[i] == '+') & (i == 0))
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
 * @brief Тесты, проверяющие функцию isnumber
 */
void test1()
{
    CU_ASSERT_EQUAL(isnumber("-122"), 1);
    CU_ASSERT_EQUAL(isnumber("00002"), 0);
}


int main()
{
    CU_pSuite suit;
    CU_initialize_registry();
    suit = CU_add_suite("number_in_words", NULL, NULL);
    CU_add_test(suit, "test1", test1);
    CU_basic_set_mode(CU_BRM_VERBOSE);
    CU_basic_run_tests();
    CU_cleanup_registry();
    return 0;
}