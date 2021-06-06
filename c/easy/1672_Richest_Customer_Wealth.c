#include <stdio.h>
#include <stdlib.h>

int maximumWealth(int** accounts, int accountsSize, int* accountsColSize);

int main(void){
    int accountsSize = 2;
    int accountsColSize = 3;
    int accounts[2][3] = {{1,2,3}, {3, 2, 1}};
    int *ptr =  accounts[0] ;
    int **ptrr = &ptr;

    // 很蠢，常亮不能求地址，没法写成
    // int ** ptr = &account[0][0]
    printf("%d\n", maximumWealth(ptrr, accountsSize, &accountsColSize));

    return 0;
}


// 12 ms, faster than 11.49% of C online submissions for Richest Customer Wealth.
// 6.3 MB, less than 39.79% of C online submissions for Richest Customer Wealth.
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int max = 0;
    int account = 0;
    int colum = 0;
    int temp = 0;

    for (account = 0; account < accountsSize; account++){
        temp = 0;
        for (colum = 0; colum < *accountsColSize; colum++)
            temp += accounts[account][colum];
        if (max <= temp)
            max = temp;
    }
    return max;
}