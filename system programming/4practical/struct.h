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
#define ARCHIPELAGO_SIZE sizeof(archipelago)
#define OPEN_ERROR -1
#define SEEK_ERROR -1
#define INDEX_ERROR -1
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
void show_archipelagos(char* file_name, int count_of_records);
void delete(char* file_name, int* number_of_records);



#endif //INC_3PRACTICAL_STRUCT_H
