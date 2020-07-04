#include <stdio.h>

void sumAvg(int num1, int num2);
int main(void)
{
    int num1;
    int num2;
    printf("Enter first number\n");
    scanf("%d", &num1);
    printf("Enter second number\n");
    scanf("%d",&num2);
    while (num1 < 0 || num2 < 0 || num1 > num2)
    {
        printf("Input should be positive numbers\n");
        scanf("%d %d", &num1, &num2);
    }

    sumAvg(num1, num2);
}

void sumAvg(int num1, int num2)
{
    int result = 0;
    int sum = 0;
    for (int i = 1; i < num2; i++)
    {
        result += num1 + i;
    }
    sum = result + num1;
    
    printf("\n%d", sum);
    printf("\nAverage is %d", sum / num2);
}



