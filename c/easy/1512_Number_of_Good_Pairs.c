#include <stdio.h>
#include <stdlib.h>

int numIdenticalPairs(int* nums, int numsSize);

int main(void){
    int nums[] = {4,4,2,2};
    printf("%d\n", numIdenticalPairs(nums, sizeof(nums)/sizeof(int)));
}


int numIdenticalPairs(int* nums, int numsSize){
    int * dict = (int *) malloc(sizeof(int) * 100);
    int i;
    int ans = 0;

    for (i = 0; i < numsSize; i++){
        dict[i] = 0;
    }
    for (i = 0; i < numsSize; i++){
        dict[nums[i]] += 1;
        printf("nums[%d] = %d, dict[%d] = %d\n", i, nums[i], nums[i], dict[i]);
    }
    for (i = 0; i < 100; i++){
        printf("dict[%d] = %d\n", i, dict[i]);
        if (dict[i] >=2 ){
            ans += dict[i] * (dict[i] -1 ) / 2;
        }
    }
    return ans;
}