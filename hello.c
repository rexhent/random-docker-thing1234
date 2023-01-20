
#include<stdio.h>

int i = 0;

int main(void) {

    while (i < 10000000)
    {
        i += 1;
        printf("%d\n", &i);

    }
    
    return 0;
}