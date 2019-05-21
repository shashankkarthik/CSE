/*
David Flores
2016-03-01
main.cpp
*/

#include <iostream>
using std::cout; using std::endl; using std::cin;
#include <string>
using std::string;
#include <utility>
using std::pair;
#include <vector>
using std::vector;
#include <map>
using std::map;
#include <algorithm>
using std::transform;
#include <iterator>
using std::ostream_iterator;

#include "functions.h"

int main()
{
	long low, high;
	map<long, vector<long>> collatz_map;
			
	cout << "Low range: ";
	cin >> low;
	cout << "High range: ";
	cin >> high;
	
	for (int i = low; i <= high; i++)
	{
		vector<long> collatz_vec;
		fill_vector(collatz_map, collatz_vec, i);
	}
	transform(collatz_map.begin(), collatz_map.end(), ostream_iterator<string>(cout), pair_to_string);
}

