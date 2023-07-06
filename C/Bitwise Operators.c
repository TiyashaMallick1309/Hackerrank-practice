#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    int and=0,or=0,xor=0;
   for(int a=1;a<n;a++)
   for(int b=a+1;b<=n;b++)
   {
       
       if(((a&b)>and) && ((a&b)<k))
       and=a&b;
       if(((a|b)>or) && ((a|b)<k))
       or=a|b;
       if(((a^b)>xor) && ((a^b)<k))
       xor=a^b;
   } 
   printf("%d\n%d\n%d",and,or,xor);
   return 0;
}

int main() {
    int n, k;
  int a,b;int and,or,xor;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
