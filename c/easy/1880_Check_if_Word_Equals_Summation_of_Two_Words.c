#include <stdio.h>
#include <stdlib.h>
#include <iso646.h>

// 0 ms, faster than 100.00% of C online submissions for Check if Word Equals Summation of Two Words.
// 5.5 MB, less than 65.91% of C online submissions for Check if Word Equals Summation of Two Words.
_Bool isSumEqual(char * firstWord, char * secondWord, char * targetWord){
    long nums[3] = {0};
    char * strings[3] = {firstWord, secondWord, targetWord};
    int j = 0;
    int k = 0;
    for (int i = 0; i < 3; i++){
        k = 0;
        while (*(strings[j]+k) != '\0'){
            nums[i] = nums[i] *10 + *(strings[j]+k)  - 'a';
            k++;
        }
        j++;
    }
    return nums[0] + nums[1] == nums[2];
}


int main(void){
    char s1[10], s2[10], s3[10];
    scanf("%s", s1);
    scanf("%s", s2);
    scanf("%s", s3);
    printf("%d\n", isSumEqual(s1,s2, s3));

    return 0;
}