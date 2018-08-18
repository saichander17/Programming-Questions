// Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
#include <iostream>
#include <vector>

using namespace std;

int getMaxSum(vector<int> &A){
  if(A.size()==0){
    return 0;
  }
  int curSum = A[0], maxSum = curSum;
  for(int i=1; i<A.size(); i++){
    cout<<i<<endl;
    if(curSum<=0){
      curSum = A[i];
    }else{
      curSum += A[i];
    }
    if(curSum > maxSum){
      maxSum = curSum;
    }
  }
  return maxSum;
}

int main() {
  int T;
  cin>>T;
  for(int i=0;i<T;i++){
    int n;
    cin>>n;
    vector<int> A;
    for(int j=0;j<n;j++){
      int pp;
      cin>>pp;
      A.push_back(pp);
    }
    cout<<getMaxSum(A)<<endl;
  }
  return 0;
}