/*************************************************************************
	> File Name: horspool.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年08月25日 星期二 15时19分04秒
 ************************************************************************/

#include<iostream>
#include<string.h>
using namespace std;
struct table
{
    char data;
    int offset;
};
table b[26];
char text[]="hdgddhjijiojoejmdldjqiqseefwodideiijdnejnej";
void shfittable(const char*,table*);
int main()
{
   /* const char *a="acdwfrg";
   *(a+1)='q';
    a=a+1;
    cout<<*a;
    char b[]="dwdjiji";
    a=b;*/
    const char* a="qsedef";
    int m=strlen(a);
    for(int i=0;i<26;i++)
    {
        b[i].data=97+i;
        b[i].offset=strlen(a);
    }
    //char b[10]="dww";
    //cout<<strlen(b)<<endl;
    shfittable(a,b);
    int n=strlen(text);
    /*for(int i=0;i<26;i++)
        cout<<b[i].offset<<" ";
    */
    int i=m-1;
    while(i<n)
    {
        int j=0;
        while(j<m)
        {
            if(a[m-1-j]!=text[i-j])
            {
                char temp=text[i];
                i=i+b[temp-97].offset;
                break;
            }
            else
                j++;
        }
        if(j==m)
        {
            break;
        }
    }
    if(i<n)
        cout<<i-m<<endl;
    else
        cout<<"no match pattern"<<endl;
    return 0;

}

void shfittable(const char *a,table*b)
{
    int m=strlen(a);
    cout<<m<<endl;
    for(int i=0;i<m-1;i++)
    {
        for(int j=0;j<26;j++)
        {
            if(a[i]==b[j].data)
            {
                b[j].offset=m-1-i;
                //cout<<b[j].offset<<endl;;
            }
        }
    }

}
