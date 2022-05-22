/**
 * @file struct.h
 */
#ifndef INC_3PRACTICAL_STRUCT_H
#define INC_3PRACTICAL_STRUCT_H
#define TRUE 1
#define FALSE 0
#define INPUT_ERROR 1
#define MEMORY_ERROR 1
#define ERROR 1
#define NUMBER_OF_INHABITED_ISLANDS 2
#define NUMBER_OF_ISLANDS 1
#define ARCHIPELAGO_SIZE sizeof(archipelago)
#define TMP_FILENAME "tmp"

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <limits.h>

typedef struct{
    int number;
    int num_of_islands;
    int num_of_inhabited_islands;
} archipelago;


int get_user_int(char* question, int min, int max);
char* input();


// Запросы
void is_uninhabited(char* file_name, int number_of_records);
void PrintMenu();

//Работа с файлами
char* create();
void add_archipelago(int* number, char* file_name);
void show_archipelagos(char* file_name, int number_of_records);
void delete(char* file_name, int* number_of_records);
void edit(char* file_name, int number_of_records);



#endif //INC_3PRACTICAL_STRUCT_H
