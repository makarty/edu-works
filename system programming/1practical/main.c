#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>


int main() {
    pid_t childPid;
    char* args[] = {"./ChildProgram", "str", NULL};
    int childStatus;

    childPid = fork();
    if (-1 == childPid)
        puts("error");
    else if(0 == childPid) {
        execvp(args[0], args);
    }else{
        wait(&childStatus);
        if(WIFEXITED(childStatus))
            printf("\nPARENT: process finished with code %d.\n", WEXITSTATUS(childStatus));
    }
    return 0;
}
