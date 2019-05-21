/*
David Flores flores45@whippet
2016-02-16
functions.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl;
#include <string>
using std::string;
#include <vector>
using std::vector;
#include <sstream>
using std::istringstream; using std::ostringstream;
#include <ostream>
using std::ostream;

vector<string> split (const string &s, char separator = ' ')
{
	vector<string> s_vect;
	string word, line;
	istringstream iss(s);
	ostringstream oss;
	
	while (getline(iss, line, separator))
	{				
		s_vect.push_back(line);
	}
	
	return s_vect;
}

void print_vector (ostream &out, const vector<string> &v)
{
	for (auto str: v)
	{
		out << str << endl;
	}
}
