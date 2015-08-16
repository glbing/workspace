/*************************************************************************
	> File Name: test_gdb.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年08月13日 星期四 19时39分25秒
 ************************************************************************/
#include <stdio.h>
#include <stdlib.h>
int f(int ,int);
int main()
{
    //int *p=NULL;
    //printf("%d",*p);
    int x;
    int y;
    printf("input the x y :");
    scanf("%d",&x);
    scanf("%d",&y);
    int sum;
    sum=f(x,y);
    printf("%d\n",sum);
    return 0;
}
int f(int x,int y)
{
    return (x+y);
}
