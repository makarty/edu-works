/*!
 * \file test.c
 *
 * Файл с тестами
 */
#include <CUnit/CUnit.h>
#include <CUnit/TestDB.h>
#include <CUnit/Basic.h>
#include <ctype.h>
#include <malloc.h>
#include <limits.h>

#define FIRST_ITERATION 0
#define SINGLE_DIGIT_NUMBER 1


struct cases
        {
    char* one;
    char* two;
    char* many;
} w_in_cases[] = {{"", "", ""},
                  {"тысяча", "тысячи", "тысяч"},
                  {"миллион", "миллиона", "миллионов"},
                  {"миллиард", "миллиарда", "миллиардов"},
                  {"триллион", "триллиона", "триллионов"}
};


struct unit
        {
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
 * @brief Функция проверки числа в строке
 * @param str Строка с числом
 * @return 1 - если строка содержит число
 * @return 0 - если ввод некорректен или неправильно записано число
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
 * @brief Тесты, проверяющие функцию isnumber
 */
void test1()
{
    CU_ASSERT_EQUAL(isnumber("-122"), 1);
    CU_ASSERT_EQUAL(isnumber("00002"), 0);
}


/*!
 * @brief Тесты, проверяющие функцию check_limit
 */
void test2()
{
    CU_ASSERT_EQUAL(check_limit("2344"), 1);
    CU_ASSERT_EQUAL(check_limit("3000000000"), 0);
    CU_ASSERT_EQUAL(check_limit("2147483648"), 0);
}


int main()
{
    CU_pSuite suit;
    CU_initialize_registry();
    suit = CU_add_suite("number_in_words", NULL, NULL);
    CU_add_test(suit, "test1", test1);
    CU_add_test(suit, "test2", test2);
    CU_basic_set_mode(CU_BRM_VERBOSE);
    CU_basic_run_tests();
    CU_cleanup_registry();
    return 0;
}