/*
David Flores
2016-04-05
main.cpp
*/

#include <iostream>
using std::cout; using std::endl;
#include <utility>
using std::pair;
#include <string>
using std::string;
#include <fstream>
using std::ifstream;
#include <algorithm>
using std::copy; using std::count_if; using std::copy_if;
#include <iterator>
using std::ostream_iterator;

size_t fill_from_file(long*& ptr, string file)
{
	ifstream ifs(file);
	size_t sz;
	
	ifs >> sz;
	
	ptr = new long[sz];
	
	for (auto i = 0u; i < sz; i++)
	{
		ifs >> *(ptr + i);
	}
	
	return sz;
}

void print_array(long* ptr, size_t sz)
{
	copy(ptr, ptr + sz, ostream_iterator<long>(cout, " "));
}

size_t concatenate(long*& ptr, size_t sz, long* p2r, size_t sz2)
{
	long* new_ptr = new long[sz + sz2];
	
	copy(ptr, ptr + sz, new_ptr);
	copy(p2r, p2r + sz2, new_ptr + sz);
	
	delete [] ptr;
	
	ptr = new_ptr;
	
	return sz + sz2;
}

pair<long*,size_t> copy_evens(long ary[], size_t sz)
{
	auto even_pred = [](long v) {return v % 2 == 0;};
	
	size_t evens = count_if(ary, ary + sz, even_pred);
	
	long* ptr = new long[evens];
	
	copy_if(ary, ary + sz, ptr, even_pred);
	
	return {ptr, evens};
}

int main()
{
	long *ary;
	long ary2[] ={10,11,12,13,14};
	size_t ary2_sz = 5;
	size_t sz_file, sz_concat;
	pair<long*, size_t> p;

	print_array(ary2, 5);
	cout << endl;
    
	sz_file = fill_from_file(ary, "tables.txt");
    print_array(ary, sz_file);
    cout << endl;
    
	sz_concat = concatenate(ary, sz_file, ary2, ary2_sz);
    print_array(ary, sz_concat);
    cout << endl;
    
	p = copy_evens(ary, sz_concat);
    print_array(p.first, p.second);
    cout << endl;
    // add code to delete dynamic memory after this
    delete [] ary;
    delete [] p.first;
}
