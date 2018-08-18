// Implement an algorithm to find the nth to last element of a singly linked list.
#include<iostream>
using namespace std;
struct Node{
  int val;
  Node *next=NULL;
  Node(){}
  Node(int d){val = d;}
};

int remove_duplicates(Node* head,int n){
  Node* temp1 = head;
  Node* temp2 = head;
  for(int i=1;i<n;i++){
    if(temp2->next==NULL){
      return -1;
    }
    temp2 = temp2->next;
  }
  // cout<<temp2->val<<endl;
  // cout<<(temp2->next)->val<<endl;
  while(temp2->next!=NULL){
    temp1 = temp1->next;
    temp2 = temp2->next;
    cout<<(temp2->val)<<endl;
    if(temp2->next==NULL){
      cout<<"GOOD";
    }else{
      cout<<"BAD";
    }
  }
  cout<<"asddasd"<<endl;
  return temp1->val;
}

int main(){
  Node *list = new Node(2);
  list->next = new Node(3);
  (list->next)->next = new Node(4);
  cout<<remove_duplicates(list,2)<<endl;
}