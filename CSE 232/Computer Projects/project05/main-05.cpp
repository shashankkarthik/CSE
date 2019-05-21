#include<iostream>
using std::cout;  using std::endl;
#include<random>
using std::mt19937_64; using std::uniform_int_distribution;
#include<string>
using std::string; 
#include<fstream>
using std::ifstream;
#include<vector>
using std::vector;

#include "functions-05.h"

int main () {
  ifstream in_f("test.txt");
  vector<long> shift_key;
  mt19937_64 reng;
  uniform_int_distribution<long> dist(1,100);
  
  read_key(in_f, shift_key);
  string msg, filtered_msg, s;
  while(getline(in_f, s)){
      msg = s.substr(1);
      if(s.front() == 'e'){
	filtered_msg = filter_string(msg);	
	cout << "Encoding of:"<<msg<<" is:"<<encode(filtered_msg, shift_key, reng, dist) << endl;
      }
      else if (s.front() == 'd')
	cout << "Decoding of:"<<msg<<" is:"<<decode(msg, shift_key) << endl;
    }
}
