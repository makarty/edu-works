#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>


struct cases{
    char* one;
    char* two;
    char* many;
} w_in_cases[] = {{"", "", ""},
                  {"тысяча", "тысячи", "тысяч"},
                  {"миллион", "миллиона", "миллионов"},
                  {"миллиард", "миллиарда", "миллиардов"}
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


char* input(char* text){
    printf("%s", text);
    char *str = (char *)malloc(sizeof(char));
    str[0] = '\0';
    int lenght = 1;
    char cur_char = 0;
    fflush(stdin);
    while ((cur_char = getc(stdin)) != '\n'){
        str[lenght - 1] = cur_char;
        lenght++;
        str = (char *)realloc(str, lenght);
    }
    str[lenght - 1] = '\0';
    return str;
}


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


void number_in_words(char* str){
    int len_str = strlen(str), d;

    if(len_str == 1 & str[0] == '0')
    {
        printf("ноль");
        return;
    }
    for (int i = 0; i < strlen(str);) {
        if(len_str == 0)
            return;
        if (str[i] == '-' & i == 0)
        {
            printf("минус ");
            len_str--;
            continue;
        }
        if (str[i] == '+' & i == 0)
        {
            len_str--;
            continue;
        }
        int len = len_str % 3;
        if(len == 0)
            len = 3;
        int len1 = len;
        for (int j = i; j < (i + len1); j++) {
            d = (int) str[j] - 48;

            if (len % 3 == 0)
                printf("%s ", units[d].hun);
            if (len % 3 == 1) // Доработать падежи
                printf("%s ", units[d].one[0]);
            if (len % 3 == 2 & str[j] == '1' & str[j + 1] != '0') {
                d = (int) str[j + 1] - 48;
                printf("%s ", units[d].two);
                if (len <= 3)
                    return;
            } else if (len % 3 == 2)
                printf("%s ", units[d].dec);
            len--;
            len_str--;
            if(len_str % 3 == 0 & d == 1)
                printf("%s ", w_in_cases[len_str / 3].one);
            else if(len_str % 3 == 0 & d >= 2 & d <= 4)
                printf("%s ", w_in_cases[len_str / 3].two);
            else if(len_str % 3 == 0 & d >= 5)
                printf("%s ", w_in_cases[len_str / 3].many);
        }
        i += len1;
    }
}


int main(){
    char* str;
    str = input("Введите строку: ");
    if(isnumber(str) == 1)
        number_in_words(str);
    else
        puts("Некорректный ввод");

    free(str);
    return 0;
}
