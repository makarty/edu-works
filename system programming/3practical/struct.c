/**
 * @file struct.c
 */
#include "struct.h"

#define NOT_INHABITED_ISLAND 0
#define LIST_EMPTY 0
#define ONE_ELEMENT_IN_LIST 1
#define FIRST 1


/**
 * @brief Функция проверки на необитаемость архипелага
 * @param archplg Архипелаг
 * @return 1 если архипелаг необитаемый
 * 0 если архипелаг обитаемый
 */
int is_uninhabited(archipelago archplg)
{
    if (archplg.num_of_inhabited_islands == NOT_INHABITED_ISLAND)
        return TRUE;
    return FALSE;
}


/**
 * @brief Функция вывода архипелагов, состоящих из обитаемых островов
 * @param list Список архипелагов
 */
void print_inhabited_archipelagos(linked_list* list)
{
    if (is_empty(list))
    {
        puts("Список пуст");
        return;
    }
    struct node* tmp = list->tail;

    while (tmp->prev != NULL)
        tmp = tmp->prev;

    while (tmp != NULL)
    {
        if (tmp->element->num_of_islands == tmp->element->num_of_inhabited_islands)
            print_information(*tmp->element);
        tmp = tmp->next;
    }
}


/**
 * @brief Функция вывода краткой информации
 * @details Выводит номер и название всех элементов списка архипелагов
 * @param list список архипелагов
 */
void choose_archipelago(linked_list * list)
{
    int i = 1;
    struct node* tmp = list->tail;

    while (tmp->prev != NULL)
    {
        tmp = tmp->prev;
    }

    while (tmp != NULL)
    {
        printf("\n№ %d: %s\n", i, tmp->element->name);
        i++;
        tmp = tmp->next;
    }
}


/**
 * @brief Функция вывода полной информации об элементе
 * @details Выводит полную информацию об архипелаге
 * @param archplg Архипелаг
 */
void print_information(archipelago archplg)
{
    printf("\n-----------------------------");
    printf("\nНазвание архипелага: %s", archplg.name);
    printf("\nКоличество островов: %d", archplg.num_of_islands);
    printf("\nКоличество обитаемых островов: %d", archplg.num_of_inhabited_islands);
    printf("\n-----------------------------");
}


// Операции с двусвязным списком
/**
 * @brief Функция создания двусвязного списка
 * @return созданный список
 */
linked_list* create_linked_list()
{
    linked_list* list = (linked_list*) malloc(sizeof(linked_list));
    if (list == NULL) exit (MEMORY_ERROR);
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
    return list;
}


/**
 * @brief Функция создания узла двусвязного списка
 * @details Является вспомогательной функцией для функции add
 * @param data Данные, которые будет хранить узел
 * @return созданный узел
 */
struct node* create_node(archipelago* data)
{
    struct node* tmp = (struct node*)malloc(sizeof(struct node));
    if (tmp == NULL) exit (MEMORY_ERROR);
    tmp->element = data;
    tmp->next = NULL;
    tmp->prev = NULL;
    return tmp;
}


/**
 * @brief Функция проверки списка на пустоту
 * @param list Двусвязный список, который нужно проверить
 * @return 1 если список пуст
 * 0 если список не пуст
 */
int is_empty(linked_list* list)
{
    if (list->size == LIST_EMPTY)
        return TRUE;
    return FALSE;
}


/**
 * @brief Функция вставки элемента в конец списка
 * @param list Список в который необходимо вставить элемент
 * @param data Данный, которые необходимо вставить
 */
void add(linked_list* list, archipelago* data)
{
    struct node* tmp = create_node(data);
    if (is_empty(list))
        list->head = tmp;
    else
    {
        if (list->size == ONE_ELEMENT_IN_LIST)
            list->head->next = tmp;
        list->tail->next = tmp;
    }

    tmp->prev = list->tail;
    list->tail = tmp;

    list->size++;
}



/**
 * @brief Функция удаления элемента из начала списка
 * @details Является вспомогательной функцией для функции remove_element
 * @param list Двусвязный список из которого удаляют элемент
 */
void remove_first(linked_list* list)
{
    if (list->head->next == NULL)
        list->tail = NULL;
    else
        list->head->next->prev = NULL;
    list->head = list->head->next;
}


/**
 * @brief Функция удаления элемента из конца списка
 * @details Является вспомогательной функцией для функции remove_element
 * @param list Двусвязный список из которого удаляют элемент
 */
void remove_last(linked_list* list)
{
    if (list->head->next == NULL)
        list->head = list->head->next;
    else
        list->tail->prev->next = NULL;
    list->tail = list->tail->prev;
}


/**
 * @brief Функция удаления элемента по индексу
 * @param list Двусвязный список из которого удаляют элемент
 * @param index Индекс элемента
 */
void remove_element(linked_list* list, int index)
{
    if (is_empty(list))
    {
        puts("Список пуст");
        return;
    }
    int current_index = 0;
    struct node* tmp = list->head;

    if (list->size == ONE_ELEMENT_IN_LIST)
    {
        free(tmp->element->name);
        free(tmp->element);
        free(tmp);
        list->head = NULL;
        list->tail = NULL;
        list->size--;
        return;
    }

    while (current_index != index)
    {
        tmp = tmp->next;
        current_index++;
    }

    if (index == FIRST)
        remove_first(list);
    else
        tmp->prev->next = tmp->next;

    if (index == list->size - 1)
        remove_last(list);
    else
        tmp->next->prev = tmp->prev;
    list->size--;
}


/**
 * @brief Функция получения элемента по индексу
 * @param list Список из которого получают элемент
 * @param index Индекс элемента
 * @return Элемент списка
 */
archipelago* get_element(linked_list* list, int index)
{
    if (is_empty(list))
    {
        puts("Список пуст");
        return NULL;
    }
    int count = 0;

    if (index >= list->size)
        index = list->size - 1;
    else if (index < FIRST)
        index = 0;
    struct node* current_element = list->head;

    while (count != index)
    {
        current_element = current_element->next;
        count++;
    }
    return current_element->element;
}


/**
 * @brief Функция вывода всех элементов списка
 * @param list Двусвязный список
 */
void print_linked_list(linked_list* list)
{
    if (is_empty(list))
    {
        puts("Список пуст");
        return;
    }

    struct node* tmp = list->tail;

    while (tmp->prev != NULL)
    {
        tmp = tmp->prev;
    }

    while (tmp != NULL)
    {
        print_information(*tmp->element);
        tmp = tmp->next;
    }
}


/**
 * @brief Функция освобождения памяти
 * @param list Двусвязный список
 */
void list_remove(linked_list* list)
{
    if (!is_empty(list))
    {
        struct node* tmp = list->tail;
        struct node* tmp_prev;

        while (tmp->prev != NULL)
        {
            tmp = tmp->prev;
        }

        while (tmp != NULL)
        {
            free(tmp->element->name);
            free(tmp->element);
            tmp_prev = tmp;
            tmp = tmp->next;
            free(tmp_prev);
        }
    }

    free(list);
}
