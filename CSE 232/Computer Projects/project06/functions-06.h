#ifndef FUNCTIONS_06
#define FUNCTIONS_06


#include<string>
using std::string;
#include<vector>
using std::vector;
#include<map>
using std::map; using std::pair;

void process_file(string filename, 
                  map<string, vector<pair<long,long>>> &encode_map, 
                  map<pair<long,long>, string> &decode_map);

string encode(string to_encode, 
              map<string, vector<pair<long,long>>>& encode_map);

string decode (string to_decode,
               map<pair<long,long>, string>& decode_map);

#endif


