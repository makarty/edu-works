/**
 * @file main.c
 */

#include <stdio.h>
#include <string.h>
#include "struct.h"

#define MIN_MENU_CHOICE 0
#define MAX_MENU_CHOICE 8
#define APPEND 1
#define EDIT 2
#define DELETE 3
#define PRINT_ALL_INFORMATION 4
#define CHECK_IS_UNINHABITED 5
#define EXIT 6
#define ARGUMENT_ERROR -1


/**
 * @brief Основная функция
 * @return 0 при успешном завершении программы
 */
int main(int argc, char * argv[])
{
    if(argc == 1)
    {
        puts("Ошибка! Отсутствуют аргументы командной строки");
        puts("\nНеобходимы следующие аргументы:");
        puts("name - имя файла");
        puts("size - размер записи\n");
        puts("Шаблон запуска программы: ./archipelagos name size");
        return -ARGUMENT_ERROR;
    }
    if(argc > 3 | argc < 3)
    {
        printf("Ошибка! Получено %d входных аргументов, хотя ожидалось 2", (argc - 1));
        puts("\nНеобходимы следующие аргументы:");
        puts("name - имя файла");
        puts("size - размер записи\n");
        puts("Шаблон запуска программы: ./archipelagos name size");
        return ARGUMENT_ERROR;
    }
    int size = atoi(argv[2]);
    if (size == 0)
    {
        puts("Ошибка! Некорректный ввод числа");
        return ARGUMENT_ERROR;
    } else if (size < ARCHIPELAGO_SIZE)
    {
        puts("Ошибка! Значение аргумента size меньше достимого значения");
        printf("Минимально доспустимое значение - %lu\n", ARCHIPELAGO_SIZE);
        return  ARGUMENT_ERROR;
    }
    int choice, number = 1, num_of_records = 0;
    int flag = TRUE;
    char* file_name = NULL;
    char* name = argv[1];

    file_name = create(name);

    while (flag)
    {
        PrintMenu();
        choice = get_user_int(">>> ", MIN_MENU_CHOICE, MAX_MENU_CHOICE);
        switch (choice)
        {
            case APPEND:
                add_archipelago(&number, file_name, size);
                num_of_records++;
                break;
            case EDIT:
                edit(file_name, num_of_records, size);
                break;
            case DELETE:
                delete(file_name, &num_of_records, size);
                number--;
                break;
            case PRINT_ALL_INFORMATION:
                show_archipelagos(file_name, num_of_records, size);
                break;
            case CHECK_IS_UNINHABITED:
                is_uninhabited(file_name, num_of_records, size);
                break;
            case EXIT:
                flag = FALSE;
                break;
        }
    }
    remove(file_name);

    return 0;
}
