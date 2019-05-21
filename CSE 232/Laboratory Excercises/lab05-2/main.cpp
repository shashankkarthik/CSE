/*
David Flores flores45@whippet
2016-02-16
main.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl; using std::cin;
#include <random>
using std::default_random_engine; using std::uniform_int_distribution;
#include <vector>
using std::vector;

int main()
{
	vector<long> l_vect;
	long seed, sum = 0;
	
	cout << "Please input a random seed: ";
	cin >> seed;
	
	default_random_engine dre(seed);
	uniform_int_distribution<long> dist(1,100);
	
	for (int i = 1; i <= 1000; i++)
	{
		long rand_num = dist(dre);
		l_vect.push_back(rand_num);
		sum += rand_num;
	}
	
	long average = sum / 1000;
	cout << "The average value of the vector of 1000 numbers is: " << average << endl;
}

