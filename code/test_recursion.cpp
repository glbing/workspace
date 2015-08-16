/*************************************************************************
	> File Name: test.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年07月26日 星期日 19时41分02秒
 ************************************************************************/

#include<iostream>
using namespace std;
void  f(int);
int main()
{
    f(4);
    return 0;
}

void f(int n)
{
    cout<<n<<"in"<<endl;
    if(n==1)
    {
        cout<<n<<"out"<<endl;
        return ;
    }
    else
    {
     f(n-1);
    }
    cout<<n<<"out"<<endl;
}
