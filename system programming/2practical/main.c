#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <unistd.h>
#include <time.h>

#define EMPTY_BUFFER 0

sem_t records, buffers;
int readers, writers, N, choice, sec;
time_t start, end;
double timer;


char* files[] = {"file1.txt", "file2.txt"};


/**
 * @brief Функция чтения из файла
 * @details Считывает информацию из файла
 */
char* reading_from_file(FILE *file)
{
    char *str = (char *)malloc(sizeof(char));
    str[0] = '\0';
    int lenght = 1;
    char cur_char = 0;
    fflush(stdin);
    while ((cur_char = fgetc(file)) != EOF)
    {
        str[lenght - 1] = cur_char;
        lenght++;
        str = (char *)realloc(str, lenght);
    }
    str[lenght - 1] = '\0';
    return str;
}


/**
 * @brief Функция, описывающая поведение потока-читателя
 * @details Блокирует семафор records и разблокирует семафор buffer
 */
void *reader()
{
    FILE *fp;
    int nRE = rand() % 10;
    int rec_value, buff_value, i = 0;
    char* record_from_file;
    sem_getvalue(&records, &rec_value);
    sem_getvalue(&buffers, &buff_value);
    while (rec_value >= 0 & buff_value <= N)
    {
        if (buff_value == N)
            printf("Читатель %d в ожидании\n", nRE);
        sem_wait(&records);
        if (choice == 1)
        {
            fp = fopen(files[i], "r");
            if (fp == NULL)
            {
                printf("Error");
                fclose(fp);
                continue;
            }
            record_from_file = reading_from_file(fp);
            fclose(fp);
        }

        printf("Читатель %d читает\n", nRE);
        sleep(1 + rand() % 2);
        printf("Читатель %d прочитал следующее: %s\n", nRE, record_from_file);
        sem_post(&buffers);
        printf("Читатель %d закончил чтение\n", nRE);
        i++;
        if (i > 1)
            i = 0;
        time(&end);
        if (difftime(end, start) > sec)
            break;
    }
}

/**
 * @brief Функция, описывающая поведение потока-писателя
 * @details Блокирует семафор buffer и разблокирует семафор records
 */
void *writer()
{
    FILE *fp;
    int nWR = rand() % 10;
    int rec_value, buff_value, i = 0;
    sem_getvalue(&records, &rec_value);
    sem_getvalue(&buffers, &buff_value);
    while (rec_value < N & buff_value >= EMPTY_BUFFER)
    {
        if (buff_value == EMPTY_BUFFER)
            printf("Писатель %d в очереди\n", nWR);
        sem_wait(&buffers);
        if (choice == 1)
        {
            fp = fopen(files[i], "w");
            if (fp == NULL)
            {
                printf("Error");
                fclose(fp);
                continue;
            }
            fprintf(fp, "%d", (rand() % 100));
            fclose(fp);
        }
        printf("Писатель %d пишет\n", nWR);
        sleep(1 + rand() % 2);
        sem_post(&records);
        printf("Писатель %d создал запись\n", nWR);
        i++;
        if (i > 1)
            i = 0;
        time(&end);
        if (difftime(end, start) > sec)
            break;
    }
}

/**
 * @brief Основная функция
 */
int main()
{
    int check = 0;
    sem_init(&records, 0, 0);
    puts("1) Честное чтение, честная запись");
    puts("2) Нечестное чтение, нечестное запись");

    do{
        printf("Выберите действие: ");
        check = scanf("%d", &choice);
        fflush(stdin);
        if (check == 0 || choice <= 0 || choice > 2)
            puts("Ошибка! Несуществующий вариант ответа");
    } while (!check || choice <= 0 ||choice > 2);

    if (choice == 1)
    {
        N = 2;

        do{
            printf("Сколько секунд должна работать программа: ");
            check = scanf("%d", &sec);
            fflush(stdin);
            if (check == 0 || sec <= 0)
                puts("Ошибка! Значение не может быть отрицательным");
        } while (!check || sec <= 0);

    } else
    {
        do{
            printf("Введите количество буферов: ");
            check = scanf("%d", &N);
            fflush(stdin);
            if (check == 0 || N <= 0)
                puts("Ошибка! Количество буферов должно быть больше нуля");
        } while (!check || N <= 0);
    }

    sem_init(&buffers, 0, N);

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

    pthread_t threadRE[readers], threadWR[writers];
    time(&start);

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