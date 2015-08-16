/*************************************************************************
	> File Name: selection_main.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年07月27日 星期一 20时16分01秒
 ************************************************************************/

#include"glb.h"
int main()
{
    int n;
    printf("input the nubmer of sequence\n");
    scanf("%d",&n);
    int *a=(int*)malloc(sizeof(int)*n);
    printf("input the sequence\n");
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    //int a[];
    int k;
    printf("input the k\n");
    scanf("%d",&k);
    int s;
    int begin=0;
    int end=n-1;
    do{
        s=partition(a,begin,end);
        if(s>k)
            end=s-1;   
        if(s<k)
            begin=s+1;  
    }while(s!=k);
    printf("%d\n",a[s]);
    return 0;
}
