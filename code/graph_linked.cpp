/*************************************************************************
	> File Name: graph_linked.cpp
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年07月27日 星期一 22时34分51秒
 ************************************************************************/

#include"graph_linked.h"
#include<stdio.h>
#include<stdlib.h>
void create_graph()
{
    printf("input the vertex number of graph:\n");
    int n;
    scanf("%d\n",&n);
    vetex_node *g1=(vertex_node*)malloc(sizeof(vertex_node)*n);
    printf("input the vertex of graph\n");
    for(int i=0;i<n;i++)
        scanf("%c\n",&g1[i].vertex);
    printf("input the vertex of graph\n");
    
}
