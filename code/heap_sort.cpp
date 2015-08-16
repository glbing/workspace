/*************************************************************************
	> File Name: heap_sort.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年08月08日 星期六 20时06分22秒
 ************************************************************************/

#include<iostream>
using namespace std;
extern "C"
void create_heap(int *,int n);
void check_heap(int *,int v,int n);
int main()
{
    int a[8]={0,9,6,8,2,5,7,10};
    int n=7;
    create_heap(a,n);
    while(n>1)
    {
        int temp=a[1];
        a[1]=a[n];
        a[n]=temp;
        check_heap(a,1,--n);
    }
    for(int i=1;i<8;i++)
        cout<<a[i]<<endl;
   // int temp=a[1];
    //a[1]=a[n];
    //a[n]=temp;
    return 0;
}

void create_heap(int *a,int n)
{
    //a[]
    for(int i=n/2;i>=1;i--)
    {
        int v=i;
        bool flag=false;
       // check_heap(a,v,n);
        while(2*v<=n&&!flag)
        {
            if(2*v<n)//i has two child
            {
                // one is 2*i,another is 2*i+1
                int temp;
                if(a[2*v]>a[2*v+1])
                    temp=2*v;
                else
                    temp=2*v+1;
                if(a[v]<a[temp])
                {
                    int t=a[v];
                    a[v]=a[temp];
                    a[temp]=t;
                    v=temp;
                }
                else
                    flag=true;
            }
            else
            {
                if(a[2*v]>a[v])
                {
                     int  t=a[v];
                    a[v]=a[2*v];
                    a[2*v]=t;
                    v=2*v;
                }
                else
                    flag=true;
            }
        }
    }   
}

void check_heap(int *a,int v,int n)
{
    while(2*v<=n)
    {
        if(2*v<n)//i has two child
        {
            // one is 2*i,another is 2*i+1
            int temp;
            if(a[2*v]>a[2*v+1])
                temp=2*v;
            else
               temp=2*v+1;
            if(a[v]<a[temp])
            {
                int t=a[v];
                a[v]=a[temp];
                a[temp]=t;
                v=temp;
            }
            else
                break;
        }
        else
        {
            if(a[2*v]>a[v])
            {
                int  t=a[v];
                a[v]=a[2*v];
                a[2*v]=t;
                v=2*v;
            }
            else
                break;
        }
    }
}
