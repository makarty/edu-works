#include <pthread.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <semaphore.h>
#include <unistd.h>


unsigned int iter;
sem_t records;
int readers, writers;


char* input(char* text)
{
    printf("%s", text);
    char *str = (char *)malloc(sizeof(char));
    str[0] = '\0';
    int lenght = 1;
    char cur_char = 0;
    fflush(stdin);
    while ((cur_char = getc(stdin)) != '\n')
    {
        str[lenght - 1] = cur_char;
        lenght++;
        str = (char *)realloc(str, lenght);
    }
    str[lenght - 1] = '\0';
    return str;
}


void *reader()
{
    int nRE = rand() % 100;
    int sem_value;
    sem_getvalue(&records, &sem_value);
    while (sem_value >= 0)
    {
        if (sem_value == 0)
            printf("Читатель %d в ожидании\n", nRE);
        sem_wait(&records);
        // readers--;
        printf("Читатель %d читает\n", nRE);
        sleep(1 + rand() % 2);
        printf("Читатель %d закончил чтение\n", nRE);
        // readers++;
        // sem_post(&records);
    }
}


void *writer()
{
    int nWR = rand() % 100;
    int sem_value;
    sem_getvalue(&records, &sem_value);
    for (int i = 0; i < iter; i++)
    {
        if (sem_value == 0)
            printf("Писатель %d в очереди\n", nWR);
        // sem_wait(&records);
        // writers--;
        printf("Писатель %d пишет\n", nWR);
        sleep(1 + rand() % 2);
        printf("Писатель %d создал запись\n", nWR);
        // writers++;
        sem_post(&records);
    }
}


int main()
{
    int check = 0;
    pthread_t threadRE[readers];
    pthread_t threadWR[writers];
    sem_init(&records, 0, 0);

    do{
        printf("Введите количество итераций: ");
        check = scanf("%d", &iter);
        fflush(stdin);
        if (check == 0 || iter <= 0)
            puts("Ошибка! Количество итераций должно быть больше нуля");
    } while (!check || iter <= 0);

    do{
        printf("Введите количество писателей: ");
        check = scanf("%d", &writers);
        fflush(stdin);
        if (check == 0 || writers <= 0)
            puts("Ошибка! Количество писателей должно быть больше нуля");
    } while (!check || writers <= 0);

    do{
        printf("Введите количество читателей: ");
        check = scanf("%d", &readers);
        fflush(stdin);
        if (check == 0 || readers <= 0)
            puts("Ошибка! Количество читателей должно быть больше нуля");
    } while (!check || readers <= 0);

    for(int i = 0; i < writers; i++)
    {
        pthread_create(&(threadWR[i]), NULL, (void *(*)(void *)) writer, NULL);
    }
    for(int i = 0; i < readers; i++)
    {
        pthread_create(&(threadRE[i]), NULL, (void *(*)(void *)) reader, NULL);
    }

    for(int i = 0; i < readers; i++)
    {
        pthread_join(threadRE[i],NULL);
    }
    for(int i = 0; i < writers; i++)
    {
        pthread_join(threadWR[i],NULL);
    }

    sem_destroy(&records);
    return 0;
}