// Given an array of size n-1 and given that there are numbers from 1 to n with one missing, the missing number is to be found.

#include <iostream>
#include <vector>

using namespace std;

int getMissingNumber(vector<int> &A){
  if(A.size()==0){
    return 0;
  }
  int n = A.size()+1;
  // What if n*(n+1) can overflow?
  int idealSum = (n*(n+1))/2;
  int curSum = 0;
  for (int i = 0; i < n-1; ++i){
    curSum += A[i];
  }
  return idealSum - curSum;
}

int main() {
  int T;
  cin>>T;
  for(int i=0;i<T;i++){
    int n;
    cin>>n;
    vector<int> A;
    for(int j=0;j<n-1;j++){
      int pp;
      cin>>pp;
      A.push_back(pp);
    }
    cout<<getMissingNumber(A)<<endl;
  }
  return 0;
}