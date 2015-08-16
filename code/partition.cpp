/*************************************************************************
	> File Name: partation.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年07月26日 星期日 22时23分42秒
 ************************************************************************/
#include"glb.h"
int partition(int*a,int begin,int end)
{
    int i=begin+1;
    int j=end;
    while(i<=j)
    {
        while(a[i]<a[begin])
            i++;
        while(a[j]>a[begin])
            j--;
        if(i>=j)
            break;
         else
        {   int temp;
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i++;
            j--;
        }
    }
    int temp;
    temp=a[begin];
    a[begin]=a[j];
    a[j]=temp;
    return j;
}


