/*!
 * \file ChildProgram.c
 * \brief Дочерняя программа
 *
 * Данная программа выводит число прописью
 */
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define SOCKET_ERROR 1
#define INET_PTON_ERROR 1
#define CONNECT_ERROR 1
#define PORT 34293


/*!
 * @brief Функция ввода строки из потока ввода
 *
 * @details Считывает строку, введённую пользователем
 * @param text - Сообщение пользователю
 * @return Строку
 */
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



/*!
 * @brief Основная функция
 */
int main(int argc, char* argv[]){
    char* str;
    int socket_init;
    struct sockaddr_in serv_addr;

    if (argc == 1)
    {
        char *server_ip = input("Введите ip адрес сервера: ");
    }
    str = input("Введите строку: ");

    if((socket_init = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        puts("\nОшибка: сокет не создан");
        return SOCKET_ERROR;
    }

    memset(&serv_addr, '0', sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr) <= 0)
    {
        puts("\nОшибка: inet_pton");
        return INET_PTON_ERROR;
    }
    puts("нет проблем в inet_pton");

    if(connect(socket_init, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        puts("\nОшибка подключения к серверу");
        return CONNECT_ERROR;
    }
    puts("нет проблем с коннектом");

    size_t lens = strlen(str) + 1;
    printf("\n%s\n", str);
    write(socket_init, &lens, sizeof(size_t));
    write(socket_init, str, lens);
    puts("нет проблем с записью");
    //free(str);// Возможны ошибки
    return 0;
}

/*
int main(int argc, char *argv[]) {
    int sockfd = 0, n = 0;
    char recvBuff[1024];
    struct sockaddr_in serv_addr;

    if(argc != 2) {
        printf("\n Usage: %s <ip of server> \n",argv[0]);
        return 1;
    }

    memset(recvBuff, '0',sizeof(recvBuff));
    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Error : Could not create socket \n");
        return 1;
    }

    memset(&serv_addr, '0', sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000);

    if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr)<=0)
    {
        printf("\n inet_pton error occured\n");
        return 1;
    }

    if( connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
       printf("\n Error : Connect Failed \n");
       return 1;
    }

    while ( (n = read(sockfd, recvBuff, sizeof(recvBuff)-1)) > 0)
    {
        recvBuff[n] = 0;
        if(fputs(recvBuff, stdout) == EOF)
        {
            printf("\n Error : Fputs error\n");
        }
    }

    if(n < 0)
    {
        printf("\n Read error \n");
    }
    return 0;
}
*/
