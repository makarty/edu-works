/**
 * @file main.c
 */

#include <stdio.h>
#include "struct.h"

#define MIN_MENU_CHOICE 0
#define MAX_MENU_CHOICE 8
#define INIT_ERROR 1
#define CREATE 1
#define APPEND 2
#define EDIT 3
#define DELETE 4
#define PRINT_ALL_INFORMATION 5
#define PRINT_INFORMATION 6
#define CHECK_IS_UNINHABITED 7
#define EXIT 8


/**
 * @brief Основная функция
 * @return 0 при успешном завершении программы
 */
int main()
{
    int choice, choice1, num_of_records = 0, number = 1;
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
            case PRINT_ALL_INFORMATION:
                show_archipelagos(file_name, num_of_records);
                break;
            case EXIT:
                flag = FALSE;
                break;
        }
    }

    return 0;
}
