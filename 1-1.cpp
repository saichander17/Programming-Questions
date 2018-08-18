// Implement an algorithm to determine if a string has all unique characters. What if you 
// can not use additional data structures?
#include<iostream>
using namespace std;
bool check_if_all_chars_are_uniq(string s){
  // Using char ascii codes.
  // Define an array with size as the number of possible distinct characters.
  int memory[256] = {0};
  for(int i=0;i<s.length();i++){
    if(memory[s[i]-0]!=0){
      return false;
    }
    memory[s[i]-0]++;
  }
  return true;
}
int main(){
  string s = "asd";
  cout<<check_if_all_chars_are_uniq(s)<<endl;
  cout<<check_if_all_chars_are_uniq("asdasd")<<endl;
  cout<<check_if_all_chars_are_uniq("aaaaa")<<endl;
  cout<<check_if_all_chars_are_uniq("123jpo")<<endl;
}