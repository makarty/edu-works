/**
 * @file struct.h
 */
#ifndef INC_3PRACTICAL_STRUCT_H
#define INC_3PRACTICAL_STRUCT_H
#define TRUE 1
#define FALSE 0

#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char* name;
    int num_of_islands;
    int num_of_inhabited_islands;
} archipelago;

struct node{
    struct node* next;
    struct node* prev;
    archipelago* element;
};

typedef struct{
    struct node* head;
    struct node* tail;
    int size;
} linked_list;

// Запросы
int is_uninhabited(archipelago archplg);

void choose_archipelago(linked_list * list);
void print_information(archipelago archplg);

// Операции с двусвязным списком
linked_list* create_linked_list();
int is_empty(linked_list* list);
void add(linked_list* list, archipelago* data);
void remove_element(linked_list* list, int index);
archipelago* get_element(linked_list* list, int index);
void print_linked_list(linked_list* list);
void list_remove(linked_list* list);

#endif //INC_3PRACTICAL_STRUCT_H
