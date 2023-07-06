#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;int i,len,zero=0,one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0;
    s=malloc(1024*sizeof(char));
    scanf("%[^\n]",s);
     len=strlen(s);
    s=realloc(s,len+1);
   
     for(i=0;i<len;i++)
     {
         switch(s[i])
         {
             case '0': {zero++; break;}
             case '1': {one++;break;}
             case '2': {two++;break;}
             case '3': {three++;break;}
             case '4': {four++;break;}
             case '5': {five++;break;}
             case '6': {six++;break;}
             case '7': {seven++;break;}
             case '8': {eight++;break;}
             case '9': {nine++;break;}
         }
     } 
     printf("%d %d %d %d %d %d %d %d %d %d",zero,one,two,three,four,five,six,seven,eight,nine);
    return 0;
}
