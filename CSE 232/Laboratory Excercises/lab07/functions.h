#ifndef LAB_07
#define LAB_07

#include <string>
using std::string;
#include <utility>
using std::pair;
#include <vector>
using std::vector;
#include <map>
using std::map;

long collatz(long n);

string pair_to_string(const pair<long, vector<long>> &p);

void fill_vector(map<long, vector<long>> &m, vector<long> &v, long start);

#endif
