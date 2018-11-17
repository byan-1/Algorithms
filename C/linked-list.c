#include <stdio.h>
#include <stdlib.h>
//node->data == (*node).data
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* insertHead(Node* head, int new_data) 
{ 
    Node* new_node = (Node*)malloc(sizeof(Node)); 
    new_node->data  = new_data; 
    new_node->next = head; 
    head = new_node;
    return head;
}

Node* insertTail(Node* head, int new_data) 
{ 
    Node* new_node = (Node*) malloc(sizeof(Node)); 
    Node* cur = head;
    new_node->data = new_data; 
    new_node->next = NULL; 
    if (head == NULL) {
        head = new_node;
        return head;
    }
    while (cur->next != NULL) {
        cur = cur->next;
    }
    cur->next = new_node;
    return head;
} 

void printList(Node* head) 
{
    Node* cur = head;
    if (head == NULL) {
        printf("list is empty\n");
        return;
    }
    
    while (cur != NULL) {
        if (cur->next != NULL) {
            printf("%d, ", cur->data);
        }
        if (cur->next == NULL) {
            printf("%d.\n", cur->data);
        }
        cur = cur->next;
    }
}

reverseList(Node* head) {
    
}

int main(void){
    Node* head;
    head = NULL;
    head = insertHead(head, 2);
    head = insertHead(head, 3);
    head = insertHead(head, 4);
    head = insertTail(head, 5);
    printList(head);
    return 0;
}