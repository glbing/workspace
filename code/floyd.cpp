/*************************************************************************
	> File Name: floyd.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年09月03日 星期四 11时09分57秒
 ************************************************************************/

#include<iostream>
using namespace std;
#define MAX 1024
int a[5][4][4];
int main()
{
    a[0][0][2]=3;
    a[0][1][0]=2;
    a[0][2][1]=7;
    a[0][2][3]=1;
    a[0][3][0]=6;
    a[0][0][1]=a[0][0][3]=a[0][1][2]=a[0][1][3]=a[0][2][0]=a[0][3][1]=a[0][3][2]=MAX;

   /* for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cout<<a[0][i][j]<<' ';
        cout<<endl;
    }
    */
    for(int k=1;k<5;k++)
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                a[k][i][j]=(a[k-1][i][j]<(a[k-1][i][k-1]+a[k-1][k-1][j])?a[k-1][i][j]:(a[k-1][i][k-1]+a[k-1][k-1][j]));
            }

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cout<<a[4][i][j]<<' ';
        cout<<endl;
    }
        
    return 0;
}
