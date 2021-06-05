#include <stdio.h>
#include <stdlib.h>
#include<string.h>

char * defangIPaddr(char *);

int main(void){
    char ip_addr[] = "1.1.1.1";
    printf("%s\n", defangIPaddr(ip_addr));
    return 0;
}

// 0 ms, faster than 100.00% of C online submissions for Defanging an IP Address.
// 5.5 MB, less than 72.20% of C online submissions for Defanging an IP Address.
char * defangIPaddr(char * address){
    char * ip = (char *) malloc(sizeof(char) * (strlen(address)+7));
    int i=0;
    int j=0;
    while (address[i] != '\0'){
        if (address[i] == '.'){
            ip[j] = '['; 
            ip[++j] = '.'; 
            ip[++j] = ']'; 
        }
        else{
            ip[j] = address[i];
        }
            j++;
        i++;
    }
    ip[j] = '\0';
    return ip;
}