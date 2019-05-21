/*
David Flores flores45@whippet
2016-02-16
main.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl; using std::cin; using std::noskipws;
#include <string>
using std::string;
#include <vector>
using std::vector;

#include "functions.h"

int main()
{
	string str;
	char delim;
	vector<string> result;
	
	cout << "Please input a string to split: ";
	getline(cin, str);
	cout << "Please input a separator character: ";
	cin >> noskipws;
	cin >> delim;
	
	result = split(str, delim);
	
	print_vector(cout, result);
}

