/*************************************************************************
	> File Name: warshall.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年08月26日 星期三 15时23分11秒
 ************************************************************************/

#include<iostream>
using namespace std;
int a[5][4][4];
int main()
{
    for(int k=0;k<5;k++)
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                //if(k==0)
                  //  a[k][i][j]=(4*i+j*3+j)%2;
                //else
                    a[k][i][j]=0;
            }
    a[0][0][1]=1;
    a[0][1][3]=1;
    a[0][3][0]=1;
    a[0][3][2]=1;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cout<<a[0][i][j]<<" ";
        cout<<endl;
    }
    //R0=a;...Rk.....Rn
    for(int k=1;k<5;k++)
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                if(a[k-1][i][j])
                    a[k][i][j]=a[k-1][i][j];
                else
                {
                    if(a[k-1][i][k-1]&&a[k-1][k-1][j])
                        a[k][i][j]=1;
                }
            }

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cout<<a[4][i][j]<<" ";
        cout<<endl;
    }
    return 0; 
}
