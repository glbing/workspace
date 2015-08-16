/*************************************************************************
	> File Name: qsort_main.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年07月27日 星期一 20时52分09秒
 ************************************************************************/

#include"usual_header.h"
void qsort(int *,int,int);
int main()
{
    int a[10]={12,3,4,5,677,82,34,56,1,2};
    qsort(a,0,9);
   // partition(a,0,9);
    for(int i=0;i<10;i++)
        printf("%d\n",a[i]);
    return 0;
}
void qsort(int *a,int begin,int end)
{
    if(begin>=end)
        return;
    else
    {
        int s=partition(a,begin,end);
        qsort(a,begin,s-1);
        qsort(a,s+1,end);
    }
}
