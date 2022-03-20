#include <pthread.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <semaphore.h>


unsigned int iter;
sem_t semaphore;
unsigned int readers = 2;


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


void *reader(int numberRE)
{
    bool read = false;
    int r, sem_value;
    sem_getvalue(&semaphore, &sem_value);
    while (true)
    {
        if(!read)
        {
            if (sem_value == 0)
                printf("Читатель %d в очереди\n", numberRE);
            sem_wait(&semaphore);
            readers--;
            printf("Читатель %d читает", numberRE);
            read = true;
            printf("Читатель %d закончил чтение", numberRE);
            sem_post(&semaphore);
            break;
        }
    }
}


void *writer();


int main()
{
    pthread_t threadRE[2];
    pthread_t threadWR[2];
    sem_init(&semaphore, 0, 2);

    printf("Введите количество итераций: ");
    scanf("%d",&iter);
    printf("Iter                         ОЧЕРЕДЬ/ВЫПОЛНЕНИЕ\n");
    int i;
    for(i = 0;i < 2;i++)
    {
        pthread_create(&(threadWR[i]),NULL,writer,(void*)&i);
    }
    for(i = 0;i < 2;i++)
    {
        pthread_create(&(threadRE[i]),NULL,reader,(void*)&i);
    }


    for(i = 0;i < 2;i++)
    {
        pthread_join(threadRE[i],NULL);
    }
    for(i = 0;i < 2;i++)
    {
        pthread_join(threadWR[i],NULL);
    }

    sem_destroy(&semaphore);
    return 0;
}