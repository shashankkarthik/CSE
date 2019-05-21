/*
David Flores flores45@whippet
2016-02-09
lab04.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl; using std::cin;
#include <string>
using std::string;
#include <cmath>
using std::pow;
#include <algorithm>
using std::sort;

long loc_to_dec(string loc)
{
	long sum = 0;
	
	for (auto chr : loc)
	{
		sum += pow(2, chr - 'a');
	}
	
	return sum;
}

string abbreviate(string loc)
{
	sort(loc.begin(), loc.end());
	
	for (unsigned int i = 0; i < loc.size();) // We know this is 'frowned' upon, but this had to be done.
	{
		if (loc[i] == loc[i+1])
		{
			loc[i] += 1;
			loc.erase(i+1, 1);
			sort(loc.begin(), loc.end());
		}
		else
		{
			i++; // This. This hurts so much. But there isn't any other way.
		}
	}
	
	return loc;
}

string dec_to_loc(long dec)
{
	string loc = "";
	
	loc.append(dec, 'a');
	
	loc = abbreviate(loc);
	
	return loc;
}

long add_loc(string loc1, string loc2)
{
	string new_loc = loc1.append(loc2);
	
	abbreviate(new_loc);
	long result = loc_to_dec(new_loc);
	
	return result;
}

int main()
{
	string str;
	long num;
	
	cout << "Please enter a location string and an integer: ";
	cin >> str >> num;
	
	cout << "The integer value of " << str << " is " << loc_to_dec(str) << endl;
	cout << "The abbreviated form of " << str << " is " << abbreviate(str) << endl;
	cout << "The location string of " << num << " is " << dec_to_loc(num) << endl;
	cout << "The sum of " << str << " and " << str << " is " << add_loc(str, str) << endl;
	
}

