/*
David Flores
2016-04-19
main.cpp
*/

#include<iostream>
using std::cout; using std::endl; using std::ostream;
#include<string>
using std::string;

#include "singlelink.h"

int main ()
{
	SingleLink<string>sl;
	sl.append_back("beds");
	sl.append_back("tables");
	cout << sl << endl;
  
	sl.append_back("chairs");
	cout << sl << endl;
	
	cout << sl.del("beds") << endl;
	cout << sl.del("next") << endl;
	
	Node<string> result_1 = sl[1];
	try
	{
		Node<string> result_2 = sl[-1];
	}
	catch (out_of_range err)
	{
		cout << "Error, message follows: ";
		cout << err.what() << endl;
	}
}
