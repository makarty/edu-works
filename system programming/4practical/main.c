/**
 * @file main.c
 */

#include <stdio.h>
#include "struct.h"

#define MIN_MENU_CHOICE 0
#define MAX_MENU_CHOICE 8
#define CREATE 1
#define APPEND 2
#define EDIT 3
#define DELETE 4
#define PRINT_ALL_INFORMATION 5
#define CHECK_IS_UNINHABITED 6
#define EXIT 7


/**
 * @brief Основная функция
 * @return 0 при успешном завершении программы
 */
int main()
{
    int choice, choice1, number = 1, num_of_records = 0;
    int flag = TRUE;
    char* file_name = NULL;

    while (flag)
    {
        PrintMenu();
        choice = get_user_int(">>> ", MIN_MENU_CHOICE, MAX_MENU_CHOICE);
        switch (choice) {
            case CREATE:
                file_name = create();
                break;
            case APPEND:
                add_archipelago(&number, file_name);
                num_of_records++;
                break;
            case EDIT:
                break;
            case DELETE:
                delete(file_name, &num_of_records);
                number--;
                break;
            case PRINT_ALL_INFORMATION:
                show_archipelagos(file_name, num_of_records);
                break;
            case CHECK_IS_UNINHABITED:
                is_uninhabited(file_name, num_of_records);
                break;
            case EXIT:
                flag = FALSE;
                break;
        }
    }
    remove(file_name);

    return 0;
}
