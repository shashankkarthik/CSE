#ifndef FUNC_H
#define FUNC_H

#include <string>
using std::string;
#include <vector>
using std::vector;
#include <ostream>
using std::ostream;

vector<string> split (const string &s, char separator = ' ');

void print_vector (ostream &out, const vector<string> &v);

# endif
