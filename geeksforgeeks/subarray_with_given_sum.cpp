// Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
#include <iostream>
#include <vector>
using namespace std;

vector<int> getSequenceMatchingSum(vector<int> &v, int S){
  if(v.size()==0){
    vector<int> res;
    res.push_back(-1);
    return res;
  }
  int curSum = 0;
  vector<int> res;
  res.push_back(0);
  res.push_back(0);

  for(int i=0;i<v.size();i++){
    curSum += v[i];
    while(curSum > S){
      if(res[0] < i){
        curSum = curSum - v[res[0]];
        res[0] = res[0]+1;
      }
    }
    if(curSum == S){
      res[1] = i+1;
      res[0]++;
      return res;
    }
  }
  vector<int> ttt;
  ttt.push_back(-1);
  // res.push_back(-1);
  return ttt;
}

int main() {
  int T;
  cin>>T;
  for(int t=0;t<T;t++){
    int N,S;
    cin>>N>>S;
    vector<int> v;
    for(int i=0;i<N;i++){
      int tt;
      cin>>tt;
      v.push_back(tt);
    }
    vector<int> res = getSequenceMatchingSum(v, S);
    for(int i=0;i<res.size();i++){
      cout<<res[i]<<" ";
    }
    cout<<endl;
  }
  return 0;
}
