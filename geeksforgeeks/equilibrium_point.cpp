// Given an array A your task is to tell at which position the equilibrium first occurs in the array. 
// Equilibrium position in an array is a position such that the sum of elements below it is equal to 
// the sum of elements after it.
#include <iostream>
#include <vector>
using namespace std;

int getEquilibriumPoint(vector<int> v){
  int sum = 0;
  if(v.size()==1){
    return 1;
  }
  for(int i=0;i<v.size();i++){
    sum+=v[i];
  }
  int curSum = 0;
  for (int i = 0; i < v.size(); ++i){
    sum -= v[i];
    if(curSum==sum){
      return i+1;
    }
    curSum += v[i];
  }
  return -1;
}
int main() {
  int T;
  cin>>T;
  for(int t=0;t<T;t++){
    int N;
    cin>>N;
    vector<int> v;
    for(int i=0;i<N;i++){
      int tt;
      cin>>tt;
      v.push_back(tt);
    }
    cout<<getEquilibriumPoint(v)<<endl;
  }
  return 0;
}
