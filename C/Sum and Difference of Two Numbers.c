#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int c,d;
	float a,b;
    scanf("%d%d%f%f",&c,&d,&a,&b);
    printf("%d %d\n%.1f %.1f",(c+d),(c-d),(a+b),(a-b));
    
    return 0;
}
