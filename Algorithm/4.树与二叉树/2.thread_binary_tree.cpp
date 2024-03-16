#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Node {
    int key;
    int ltag, rtag; // 1: thread, 0 : edge
    struct Node *lchild, *rchild;
} Node;

Node *getNewNode(int val) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->key = val;
    p->ltag = p->rtag = 0;
    p->lchild = p->rchild = NULL;
    return p;
}

Node *insert(Node *root, int val) {
    if (root == NULL)
        return getNewNode(val);
    if (rand() % 2)
        root->lchild = insert(root->lchild, val);
    else
        root->rchild = insert(root->rchild, val);
    return root;
}

void clear(Node *root) {
    if (root == NULL)
        return;
    if (root->ltag == 0) clear(root->lchild);
    if (root->rtag == 0) clear(root->rchild);
    free(root);
    return;
}

void pre_order(Node *root) {
    if (root == NULL) return ;
    printf("%d ", root->key);
    if (root->ltag == 0) pre_order(root->lchild);
    if (root->rtag == 0) pre_order(root->rchild);
    return ;
}

void in_order(Node *root) {
    if (root == NULL) return ;
    if (root->ltag == 0) in_order(root->lchild);
    printf("%d ", root->key);
    if (root->rtag == 0) in_order(root->rchild);
    return ;
}

void post_order(Node *root) {
    if (root == NULL) return ;
    if (root->ltag == 0) post_order(root->lchild);
    if (root->rtag == 0) post_order(root->rchild);
    printf("%d ", root->key);
    return ;
}

Node *pre_node = NULL, *inorder_node = NULL;
void __build_inorder_thread(Node *root) {
    if (root == NULL) return ;
    if (root->ltag == 0) __build_inorder_thread(root->lchild);
    if (inorder_node == NULL) inorder_node = root;
    if (root->lchild == NULL) {
        root->lchild = pre_node;
        root->ltag = 1;
    }
    if (pre_node && pre_node->rchild == NULL) {
        pre_node->rchild = root;
        pre_node->rtag = 1;
    }
    pre_node = root;
    if (root->rtag == 0) __build_inorder_thread(root->rchild);
    return ;
}

void build_inorder_thread(Node *root) {
    __build_inorder_thread(root);
    pre_node->rchild = NULL;
    pre_node->rtag = 1;
    return ;
}

Node *getNext(Node *root) {
    if (root->rtag == 1) return root->rchild;
    root = root->rchild;
    while (root->ltag == 0 && root->lchild) {
        root = root->lchild;
    }
    return root;
}
 
int main() {
    srand(time(0));
    Node *root = NULL;
    #define MAX_OP 10
    for (int i = 0; i < MAX_OP; ++i) {
        root = insert(root, rand() % 100);
    }
    pre_node = NULL; 
    build_inorder_thread(root);
    pre_order(root); printf("\n");
    in_order(root); printf("\n");
    post_order(root); printf("\n");
    // like linklist
    Node *node = inorder_node;
    while (node) {
        printf("%d ", node->key);
        node = getNext(node);
    }
    clear(root);
    return 0;
}
