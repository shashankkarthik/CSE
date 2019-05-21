/*
David Flores
2016-03-29
main.cpp
*/

#include<iostream>
using std::cout; using std::cin; using std::endl;
#include<iomanip>
using std::boolalpha;
#include<string>
using std::string;
#include<stdexcept>
using std::runtime_error;

#include "circbuf.h"

int main()
{
	const size_t sz = 4;
	CircBuf cb(sz);

	cout << boolalpha;
	cb.add(1);
	cb.add(2);

	// cb = cb + 1;
	// cb = cb + 2;
	//cout << "Front:"<<cb.pop_front()<<endl;
	//cout << cb << endl;

	//cb.remove();
	//cout << "Front:"<<cb.pop_front() <<endl;
	//cb.remove();
	//cout << "Empty?:"<<cb.empty() << endl;
	//cout << cb << endl;

	cout << "Add 4 elements"<<endl;
	for(long i=0; i<4;i++)
	{
		cb.add(i+27);
	}
	cout << cb << endl;

	cout << "Remove 4 elements"<<endl;
	while(!cb.empty())
	{
		cout << cb.pop_front() << ", ";
		cb.remove();
	}

	cout << endl << "Fill er up"<<endl;
	for(int i=0; !cb.full(); i++)
	{
		cb.add(i*i);
	}
	cout << "Full?: "<<cb.full() <<endl;

	cout << "Drain it"<<endl;
	for(int i=0; !cb.empty(); i++)
	{
		cb.remove();  
	}
	cout << "Empty?: "<<cb.empty()<<endl;

	try
	{
		cout << cb.pop_front() << endl;
	}
	catch (runtime_error err)
	{
		cout << "Yo, cannot access an empty buffer. Real error msg follows bruh"<<endl;
		cout << err.what() << endl;
	}

	//// Extra Credit
	//cb = cb + 25;
	//cb = 30 + cb;
	//cout << cb << endl;
	//cb = cb + cb;
	//cout << cb << endl;
}
