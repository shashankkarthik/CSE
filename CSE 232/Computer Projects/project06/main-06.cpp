#include<iostream>
using std::cout; using std::endl;
#include<string>
using std::string;
#include<vector>
using std::vector;
#include<map>
using std::map; using std::pair;
#include<algorithm>
using std::copy;
#include<iterator>
using std::ostream_iterator;
#include<sstream>
using std::ostringstream;

#include "split.h"
#include "functions-06.h"


int main(){
  map<string, vector<pair<long,long> > > encode_map;
  map<pair<long,long> , string> decode_map;
  string good_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'";
  string encoded_string, decoded_string;
  vector<string> words;
  vector<string> encoded_vector;
  vector<string> decoded_vector;

  // TEST split
  split("This is a TEST.", words, good_chars);
  // words should have: {"this", "is", "a", "test"}, no period in test
  copy(words.begin(), words.end(), ostream_iterator<string>(cout, ","));
  cout << endl;

  words.clear();
  split ("Boards.......................... $ 8.03-1/2, mostly shanty boards.",
	 words, good_chars);
  // words should have {"boards", "mostly", "shanty", "boards"}
  copy(words.begin(), words.end(), ostream_iterator<string>(cout, ","));
  cout << endl;
  
  process_file("gburg.txt", encode_map, decode_map);

  // TEST encoding
  words={"fourscore", "seven", "fathers"};
  for(auto w : words){	
    encoded_vector.push_back( encode(w,encode_map) );
  }
  // encoded should have {"0:0",  "0:2",  "0:6"}
  ostringstream oss;
  copy(encoded_vector.begin(),
       encoded_vector.end(),
       ostream_iterator<string>(oss, " ")
       );
  encoded_string = oss.str();
  cout << "Encoded:"<<encoded_string<<endl;

  // TEST decoding
  for(auto w : encoded_vector)
    decoded_vector.push_back(decode(w,decode_map));

  // decoded_vector should have {"fourscore", "seven", "fathers"}
  oss.clear();
  copy(decoded_vector.begin(),
       decoded_vector.end(),
       ostream_iterator<string>(oss, " ")
       );
  decoded_string = oss.str();  
  cout << "Decoded: "<<decoded_string<<endl;
}
