/**
 * @file main.c
 */

#include <stdio.h>
#include <limits.h>
#include "struct.h"

#define MIN_MENU_CHOICE 0
#define MAX_MENU_CHOICE 8
#define MAX_FIELD_CHOICE 1
#define MIN_FIELD_CHOICE 3
#define INPUT_ERROR 1
#define APPEND 1
#define EDIT 2
#define DELETE 3
#define PRINT_ALL_INFORMATION 4
#define PRINT_INFORMATION 5
#define CHECK_IS_UNINHABITED 6
#define PRINT_INHABITED_ARCHIPELAGOS 7
#define EXIT 8


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
            puts("Error");
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


/**
 * @brief Основная функция
 * @return 0 при успешном завершении программы
 */
int main()
{
    int choice, choice1;
    linked_list* link_list = create_linked_list();

    while (TRUE)
    {
        printf("\n1) Добавить архипелаг");
        printf("\n2) Редактировать архипелаг");
        printf("\n3) Удалить архипелаг");
        printf("\n4) Вывести информацию обо всех архипелагах");
        printf("\n5) Вывести информацию об одном архипелаге");
        printf("\n6) Проверка архипелага на необитаемость");
        printf("\n7) Вывести все обитаемые архипелаги");
        printf("\n8) Выход");

        choice = get_user_int("\nВыберите действие: ", MIN_MENU_CHOICE, MAX_MENU_CHOICE);

        if (choice == APPEND)
        {
            archipelago* archplg = (archipelago*)malloc(sizeof(archipelago));
            if (archplg == NULL) exit (MEMORY_ERROR);

            printf("\nВведите название архипелага: ");
            archplg->name = input();

            archplg->num_of_islands = get_user_int(
                    "Введите количество островов: ", MIN_MENU_CHOICE, INT_MAX);

            archplg->num_of_inhabited_islands = get_user_int(
                    "Введите количество обитаемых островов: ", MIN_MENU_CHOICE, archplg->num_of_islands);

            add(link_list, archplg);
        }
        if (choice == EDIT)
        {
            int field;
            choose_archipelago(link_list);
            choice1 = get_user_int("\nВыберите архипелаг: ", MIN_MENU_CHOICE, link_list->size);

            puts("1) Название");
            puts("2) Количество островов");
            puts("3) Количество обитаемых островов");
            field = get_user_int("Какое поле нужно изменить: ", MIN_FIELD_CHOICE, MAX_FIELD_CHOICE);
            if (field == 1)
            {
                printf("Введите название архипелага: ");
                get_element(link_list, choice1 - 1)->name = input();
            }else if (field == 2)
                get_element(link_list, choice1 - 1)->num_of_islands = get_user_int(
                        "Введите количество островов: ", 0, INT_MAX);
            else if (field == 3)
                get_element(link_list, choice1 - 1)->num_of_inhabited_islands = get_user_int(
                        "Введите количество обитаемых островов: ", 0,
                        get_element(link_list, choice1 - 1)->num_of_islands);

        }
        if (choice == DELETE)
        {
            choose_archipelago(link_list);
            choice1 = get_user_int("\nВыберите архипелаг: ", MIN_MENU_CHOICE, link_list->size);
            remove_element(link_list, choice1 - 1);
        }
        if (choice == PRINT_ALL_INFORMATION)
            print_linked_list(link_list);
        if (choice == PRINT_INFORMATION)
        {
            choose_archipelago(link_list);
            choice1 = get_user_int("\nВыберите архипелаг: ", MIN_MENU_CHOICE, link_list->size);
            print_information(*get_element(link_list, choice1 - 1));

        }
        if (choice == CHECK_IS_UNINHABITED)
        {
            choose_archipelago(link_list);
            choice1 = get_user_int("\nВыберите архипелаг: ", MIN_MENU_CHOICE, link_list->size);
            if (is_uninhabited(*get_element(link_list, choice1 - 1)))
                printf("\n---------------------\nАрхипелаг необитаемый\n---------------------");
            else
                printf("\n-------------------\nАрхипелаг обитаемый\n-------------------");
        }
        if (choice == PRINT_INHABITED_ARCHIPELAGOS)
            print_inhabited_archipelagos(link_list);
        if (choice == EXIT)
            break;
    }

    list_remove(link_list);

    return 0;
}
