#include <iostream>
#include <ctime>
#include <cmath>
#include <vector>
#include <algorithm>
#include <fstream>
#include <random>
#include <chrono>
#include "KthSmallest.h"
using namespace std;

int main()
{
	//ifstream inClientFile("f100",ios::in);
	ifstream inClientFile("f1000",ios::in);
	//ifstream inClientFile("f10000",ios::in);
	//ifstream inClientFile("f100000",ios::in);
	//ifstream inClientFile("small_input.in",ios::in);

	// check to see if file opening succeeded
	if ( !inClientFile.is_open() ) {
		cout<<"Could not open file\n";
		return 0;
	}

	// read input
	vector<int> nums;
	int input_t;
	while (inClientFile >> input_t) {
		nums.push_back(input_t);
	}
	inClientFile.close();

	vector<int> nums2 = nums;

	// Testing with Insertion sort
	auto t1 = std::chrono::high_resolution_clock::now();
	srand(static_cast<unsigned int>(time(0)));

    // FOLLOWING IS FOR TESTING
    // Generate random k values
	//int min=1,max=10;

	random_device rd;     // only used once to initialize (seed) engine
	mt19937 rng(rd());    // random-number engine used (Mersenne-Twister in this case)

    // ********TESTING ++++++++uncomment it for testing against random k
    // generating random kth value given a certain range
    // uniform_int_distribution<int> uni(min,2000); // guaranteed unbiased
	// auto kthvalue = uni(rng);

    //	********TESTING insertion sort for kth element
    //	hard coded kth value using Insertion Sort

    int kthvalue= 4;
    // nums will be sorted after
	KthSmallestUsingSorting(nums, kthvalue);
	auto t2 = std::chrono::high_resolution_clock::now();
	cout << "Size of the vector : "<< nums.size() << endl;

    cout << "Insertion Sort Search method  took "
			<< std::chrono::duration_cast<std::chrono::nanoseconds>(t2-t1).count()
			<< " nanoseconds \n" << endl;

    //***FOR TESTING*******
    // time unit can be changed to millisecond when data size >100
	// cout << "Insertion Sort Search method  took "
			// << std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count()
			// << " milliseconds \n";    inClientFile.close();

    // **************TESTING kthSmallest for kth element
    // hard coded kth value using kthSmallest method.

	// using nums2 so the vector is not sorted
	auto t3 = std::chrono::high_resolution_clock::now();
	srand(static_cast<unsigned int>(time(0)));
	KthSmallestUsingExtractMin(nums2, kthvalue);
	auto t4 = std::chrono::high_resolution_clock::now();

	cout << "Size of the vector : "<< nums2.size() << endl;
	cout << std::chrono::duration_cast<std::chrono::nanoseconds>(t4-t3).count()
			<< " nanoseconds \n";    inClientFile.close();
	return 0;


}
