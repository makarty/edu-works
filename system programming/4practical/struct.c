/**
 * @file struct.c
 */
#include "struct.h"

mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH;

/**
 * @brief Функция ввода числа
 * @param question Сообщение пользователю
 * @param min минимально возможное число для выбора
 * @param max максимально возможное число для выбора
 * @return число которое ввёл пользователь
 */
int get_user_int(char* question, int min, int max)
{
    int user_choose = 0;
    int success = 0;
    char buff[32];
    do
    {
        fputs(question, stdout);
        fgets(buff, 32, stdin);
        fflush(stdin);
        success = sscanf(buff, "%d", &user_choose);
        if (user_choose > max || user_choose < min || success != INPUT_ERROR)
            puts("Ошибка! Число не входит в диапазон допустимых значений");
    } while (user_choose > max || user_choose < min || success != INPUT_ERROR);
    return user_choose;
}


/**
 * @brief Функция ввода строки
 * @return строку которую ввёл пользователь
 */
char* input()
{
    char *str = (char *)malloc(sizeof(char));
    if (str == NULL) exit (MEMORY_ERROR);
    int lenght = 1;
    char cur_char = 0;
    fflush(stdin);
    while ((cur_char = getc(stdin)) != '\n')
    {
        str[lenght - 1] = cur_char;
        lenght++;
        str = (char *)realloc(str, lenght);
        if (str == NULL)
        {
            perror("realloc");
            exit(MEMORY_ERROR);
        }
    }
    str[lenght - 1] = '\0';
    return str;
}


void PrintMenu()
{
    puts("1) Создать файл");
    puts("2) Добавить архипелаг");
    puts("3) Редактировать архипелаг");
    puts("4) Удалить архипелаг");
    puts("5) Вывести информацию обо всех архипелагах");
    puts("6) Проверка архипелага на необитаемость");
    puts("7) Выход");
}


char* create()
{
    char* file_name = NULL;
    int flag = TRUE;
    printf("Введите имя файла: ");
    while(flag)
    {
        file_name = input();
        int database = open(file_name, O_CREAT | O_EXCL, mode);
        if(database == ERROR)
        {
            puts("Ошибка");
        } else
        {
            printf("Файл |%s| создан.\n", file_name);
            close(database);
            flag = FALSE;
        }
    }
    return file_name;
}


void add_archipelago(int* number, char* file_name)
{
    if (file_name == NULL)
    {
        puts("Ошибка! Файла не существует");
        return;
    }
    int num_of_islands, num_of_inh_islands;

    num_of_islands = get_user_int("Введите количество островов: ", 0, INT_MAX);
    num_of_inh_islands = get_user_int("Введите количество обитаемых островов: ", 0, num_of_islands);

    int file = open(file_name, O_WRONLY | O_APPEND);
    archipelago archplg = {*number, num_of_islands, num_of_inh_islands};
    *number = *number + 1;
    unsigned int add_code = write(file, &archplg, ARCHIPELAGO_SIZE);
    if(add_code == ERROR)
    {
        perror("ERROR");
    }
    close(file);
}


void show_archipelagos(char* file_name, int count_of_records)
{
    if (file_name == NULL)
    {
        puts("Ошибка! Файла не существует");
        return;
    }
    int file = open(file_name, O_RDONLY);
    archipelago archplg;
    unsigned int pointer = 0;

    for(int i = 0; i < count_of_records; i++)
    {
        unsigned int read_code = read(file, &archplg, ARCHIPELAGO_SIZE);
        if(read_code == ERROR)
        {
            perror("ERROR");
        }
        printf("%d. Количество островов - %d.\n   Количество обитаемых островов - %d.\n",
               archplg.number,
               archplg.num_of_islands,
               archplg.num_of_inhabited_islands);
        pointer = pointer + ARCHIPELAGO_SIZE;
        lseek(file, pointer, SEEK_SET);
    }
    close(file);
}


void delete(char* file_name, int* number_of_records)
{
    if (file_name == NULL)
    {
        puts("Ошибка! Файла не существует");
        return;
    }
    int number_to_delete;
    unsigned int pointer = 0;
    int flag = TRUE;
    archipelago tmp_archplg;

    while (flag)
    {
        number_to_delete = get_user_int("Выберите номер удаляемого архипелага: ", 1, INT_MAX);
        int file = open(file_name, O_RDONLY);
        for(int i = 0; i < *number_of_records; i++)
        {
            unsigned int read_code = read(file, &tmp_archplg, ARCHIPELAGO_SIZE);
            if(read_code == ERROR)
                perror("ERROR");
            if(tmp_archplg.number == number_to_delete)
                flag = FALSE;
        }
        if(flag == TRUE)
            puts("Данного номера нет в списке");
        close(file);
    }


    int old_file = open(file_name, O_RDONLY);
    int new_file = open(TMP_FILENAME, O_CREAT | O_EXCL | O_APPEND | O_WRONLY, mode);
    for (int i = 0; i < *number_of_records; i++)
    {
        unsigned int read_code = read(old_file, &tmp_archplg, ARCHIPELAGO_SIZE);
        if(read_code == ERROR)
            perror("ERROR");
        if(tmp_archplg.number != number_to_delete)
        {
            if (tmp_archplg.number > number_to_delete)
                tmp_archplg.number--;
            unsigned int write_code = write(new_file, &tmp_archplg, ARCHIPELAGO_SIZE);
            if(write_code == ERROR)
                perror("ERROR");
        }
        pointer = pointer + ARCHIPELAGO_SIZE;
        lseek(old_file, pointer, SEEK_SET);
    }
    close(old_file);
    close(new_file);
    remove(file_name);
    rename(TMP_FILENAME, file_name);
    *number_of_records = *number_of_records - 1;
}


void is_uninhabited(char* file_name, int number_of_records)
{
    if (file_name == NULL)
    {
        puts("Ошибка! Файла не существует");
        return;
    }
    unsigned int number = 1, pointer = 0;
    archipelago archplg;
    int file = open(file_name, O_RDONLY);

    number = get_user_int("Введите номер архипелага: ", 1, INT_MAX);
    pointer = pointer + (number - 1) * ARCHIPELAGO_SIZE;
    lseek(file, pointer, SEEK_SET);
    if (number > number_of_records)
    {
        puts("Данного номера нет в списке");
        return;
    }

    unsigned int read_code = read(file, &archplg, ARCHIPELAGO_SIZE);
    if(read_code == ERROR)
        perror("ERROR");

    close(file);
    if (archplg.num_of_inhabited_islands == 0)
        puts("Архипелаг необитаемый");
    else if (archplg.num_of_inhabited_islands != 0)
        puts("Архипелаг обитаемый");
}
