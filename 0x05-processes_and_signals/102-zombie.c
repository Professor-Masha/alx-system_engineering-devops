#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t zombie_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        zombie_pid = fork();
        if (zombie_pid > 0)
        {
            printf("Zombie process created, PID: %d\n", zombie_pid);
        }
        else if (zombie_pid == 0)
        {
            exit(0); // Child exits immediately to become a zombie
        }
        else
        {
            perror("fork");
            exit(1);
        }
    }
    
    infinite_while(); // Keep parent alive
    return (0);
}

