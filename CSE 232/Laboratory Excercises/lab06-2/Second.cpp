#include<iostream>
using std::cout; using std::endl;
#include<vector>
using std::vector;

long f1(vector<long>& v){
  long result=0;
  unsigned int i=0u;
  for (i=0; i< v.size(); i++)
    result += v[i];
  cout << "Went through "<<i<<" elements"<<endl;
  return result;
}

int main (){
  vector<long> v={1,2,3,4,5};
  cout << f1(v) << endl;
}
