/*!
 * \file main.c
 * \brief Родительская программа
 *
 * Данная программа является родителем, запускает дочернюю программу
 */
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define PROCESS_CREATION_ERROR -1
#define CHILD_PROCESS 0

/*!
 * @brief Основная функция
 */
int main()
{
    pid_t childPid;
    char* args[] = {"./client", "str", NULL};
    int childStatus;

    childPid = fork();
    if (PROCESS_CREATION_ERROR == childPid)
        puts("error");
    else if(CHILD_PROCESS == childPid)
    {
        execvp(args[0], args);
    }else
    {
        wait(&childStatus);
        if(WIFEXITED(childStatus))
            printf("\nPARENT: process finished with code %d.\n", WEXITSTATUS(childStatus));
    }
    return 0;
}
