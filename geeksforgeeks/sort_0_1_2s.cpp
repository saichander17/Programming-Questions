// Write a program to sort an array of 0's,1's and 2's in ascending order.

#include <iostream>
#include <vector>
using namespace std;

void sort(vector<int> &v){
  vector<int> counts;
  counts.push_back(0);
  counts.push_back(0);
  counts.push_back(0);
  for(int i=0;i<v.size();i++){
    counts[v[i]]++;
  }
  int st = 0;
  for(int j=0;j<counts.size();j++){
    for(int i = st; i<st+counts[j];i++){
      v[i] = j;
    }
    st += counts[j];
  }
  
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
    sort(v);
    for(int i=0;i<v.size();i++){
      cout<<v[i]<<" ";
    }
    cout<<endl;
  }
  return 0;
}
