/*************************************************************************
	> File Name: graph_linked.h
	> Author: GLB 
	> Mail: 1207445440@qq.com 
	> Created Time: 2015年07月27日 星期一 22时22分46秒
 ************************************************************************/

#ifndef _GRAPH_LINKED_H
#define _GRAPH_LINKED_H
typedef struct enode
{
    int order;
    struct node* next;
}edge_node;
typedef struct vnode
{
    char vertex;
    edgenode * first;
}vertex_node;
/*typedef struct
{
    vetex_node *graph_point;
    int n;//vertex
    int e;//edge
}graph;*/
void create_graph();
#endif
