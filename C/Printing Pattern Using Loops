#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n,i,j,min;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
      for(i=0;i<((2*n)-1);i++)
      {
          for(j=0;j<((2*n)-1);j++)
          {
          if (i<j)
          min=i;
          else 
          min =j;
          if (min<((2*n)-i-1))
          min=min;
          else 
          min=(2*n)-i-2;
          if(min<((2*n)-j-2))
          min=min;
          else 
          min=(2*n)-j-2;
          printf("%d ",(n-min));
          }
          printf("\n");
      }
    return 0;
}
