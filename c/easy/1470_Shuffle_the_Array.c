#include <stdio.h>
#include <stdlib.h>

int* shuffle(int* nums, int numsSize, int n, int* returnSize);

int main(void){
    int nums[] = {2,5,1,3,4,7};
    int n = 3;
    int returnSize = 0;

    int * shuffled_nums = shuffle(nums, n, n, &returnSize);

    for (int i =0; i < returnSize; i++){
        printf(" %3d ", shuffled_nums[i]);
    }
    printf("\n");

    free(shuffled_nums);

    return 0;
}

// 28 ms, faster than 7.93% of C online submissions for Shuffle the Array.
// 7.1 MB, less than 52.24% of C online submissions for Shuffle the Array.
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int * shuffled_nums = (int *) malloc( sizeof(int) * n * 2);
    int i;
    int j=0;

    *returnSize = n * 2;
    for (i = 0; i < n; i++){
        shuffled_nums[j] = nums[i];
        shuffled_nums[j+1] = nums[i+n];
        j+=2;
    }
    return shuffled_nums;
}