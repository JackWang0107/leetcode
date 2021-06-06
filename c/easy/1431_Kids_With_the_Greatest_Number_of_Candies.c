#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize);

int main(void){
    int candies[] = {2, 3, 5, 1, 3};
    int candiesSize = 5;
    int extraCandies = 3;
    int returnSize = 0;

    bool * ans = kidsWithCandies(candies, candiesSize, extraCandies, &returnSize);
    for (int i = 0; i < returnSize; i++){
        printf("%d\t", ans[i]);
    }
    printf("\n");

    return 0;
}

// 8 ms, faster than 7.11% of C online submissions for Kids With the Greatest Number of Candies.
// 6.6 MB, less than 22.51% of C online submissions for Kids With the Greatest Number of Candies.
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    int i = 0;
    int max = 0;
    bool * ans = (bool * ) malloc( sizeof(bool) * candiesSize);
    *returnSize = candiesSize;

    for (i = 0; i<candiesSize; i++){
        max = max < candies[i] ? candies[i] : max;
        candies[i] += extraCandies;
    }
    for (i = 0; i < candiesSize; i++){
        if ((candies[i] -= max) < 0)
            ans[i] = false;
        else
            ans[i] = true;
    }
    return ans;
}