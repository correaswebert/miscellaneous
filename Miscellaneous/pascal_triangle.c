#include <stdio.h>
#define ROWS 5

void print_row(int row, int arr[])
{
    // print spaces appropriately for triangle
    for (int space=0; space < ROWS-row; space++)
        printf(" ");
    // print the numbers
    for (int num=0; num < row; num++)
    {
        if (arr[num] == 0)
            break;
        print("%d\t", arr[num]);
    }
    printf("\n");
}

int main()
{
    int a[ROWS], b[ROWS];
    
    // initialize a[]
    for (int x=0; x < ROWS; x++)
        a[x] = 0;
    a[0] = 1; a[1] = 1;
    b[0] = 1;
    
    for (int i=0; i < ROWS; i++)
    {
        a[i] = 1; b[i] = 1;
        for (int j=1; j < i; j++)
        {
            b[j] = a[j-1] + a[j];
            a[j] = b[j];
        }
        
        print_row(i+1, b);
    }
    
    return 0;
}