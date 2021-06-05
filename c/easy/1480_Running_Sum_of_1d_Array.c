#include <stdio.h>
#include <stdlib.h>

// 12 ms, faster than 7.13% of C online submissions for Running Sum of 1d Array.
// 12 ms, faster than 7.13% of C online submissions for Running Sum of 1d Array.
int* runningSum(int* nums, int numsSize, int* returnSize){
    int cumsum = 0;
    int *result = (int *) malloc(numsSize * sizeof(int));
    * returnSize = numsSize;
    for (int i = 0; i < numsSize; i++){
        cumsum += nums[i];
        result[i] = cumsum;
    }
    return result;
}


int main(void){
    int nums[] = {3,1,2,10,1};
    int size;
    int i;
    int * results;

    results = runningSum(nums, sizeof(nums)/sizeof(int), &size);
    for (i = 0; i<sizeof(nums)/sizeof(int); i++){
        printf("  [%4d]  ",results[i] );
    }
    printf("\n");

    return 0;
}