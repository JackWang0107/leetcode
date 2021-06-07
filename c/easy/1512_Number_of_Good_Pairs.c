#include <stdio.h>
#include <stdlib.h>

int numIdenticalPairs(int* nums, int numsSize);

int main(void){
    int nums[] = {1,2,3,1,1,3};
    printf("%d\n", numIdenticalPairs(nums, 6));
}


int numIdenticalPairs(int* nums, int numsSize){
    int * dict = (int *) malloc(sizeof(int) * numsSize);
    int i;
    int ans = 0;

    for (i = 0; i < numsSize; i++){
        dict[i] = 0;
    }
    for (i = 0; i < numsSize; i++){
        dict[nums[i]] += 1;
    }
    for (i = 0; i < numsSize; i++){
        if (dict[i] >=2 ){
            nums += dict[i] * (dict[i] -1 ) / 2;
        }
    }
    return ans;
}