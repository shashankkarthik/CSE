/*
David Flores
2016-03-01
functions.cpp
*/

#include <iostream>
using std::cout; using std::endl;
#include <string>
using std::string;
#include <utility>
using std::pair;
#include <vector>
using std::vector; using std::back_inserter;
#include <map>
using std::map;
#include <algorithm>
using std::transform; using std::copy;
#include <sstream>
using std::ostringstream;

long collatz(long n)
{
	long result;
	
	if ((n % 2) == 1)
	{
		result = (n * 3) + 1;
	}
	else
	{
		result = n / 2;
	}
	return result;
}

string pair_to_string(const pair<long, vector<long>> &p)
{
	ostringstream oss;
	
	oss << p.first << ": {" << p.second[0];
	
	for (unsigned int i = 1u; i < p.second.size(); i++)
	{
		oss << ", " << p.second[i];
	}	
	oss << "}" << endl;
	
	return oss.str();
}

void fill_vector(map<long, vector<long>> &m, vector<long> &v, long start)
{
	long n = start;
	v.push_back(start);
	
	while (v.back() != 1)
	{
		auto itr = m.find(n);
		
		if (itr != m.end())
		{
			copy(begin(m[n])+1, end(m[n]), back_inserter(v));
			cout << "For " << start << " program copies the rest starting from " << n << endl;
		}
		else
		{
			n = collatz(n);
			v.push_back(n);
		}
	}	
	m.insert({start, v});
}
