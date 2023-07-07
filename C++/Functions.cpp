#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b,int c,int d)
{
    int ans;
    if(a>b && a>c && a>d)
    printf("%d",a);
    else if(b>a && b>c && b>d)
    printf("%d",b);
    else if(c>a && c>b && c>d)
    printf("%d",c);
    else
    printf("%d",d);
    return ans;
}
int main() {
    int a, b, c, d;
    scanf("%d\n%d\n%d\n%d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
}
