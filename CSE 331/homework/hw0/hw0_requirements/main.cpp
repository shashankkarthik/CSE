#include <cstdlib>
#include <iostream>
using std::cout; using std::endl;
#include <vector>
using std::vector;
#include <ctime>
#include "LinearSearch.h"
#include <fstream>
using std::ifstream;
#include <time.h>
#include <iomanip>
#include <chrono>

vector<int> getDataVector() {
  ifstream inClientFile("input.in", std::ios::in);
	// check to see if file opening succeeded
	if ( !inClientFile.is_open() ) {
    throw("Could not open file!\n");
	}

	vector<int> data;
	//read input
	int input_t;

	//load vector
	while( inClientFile >> input_t) {
		data.push_back(input_t);
	}

  inClientFile.close();

  return data;
}

int main() {
  vector<int> data = getDataVector();

  auto t1 = std::chrono::high_resolution_clock::now();

	//Testing1
	//testing for hard-coded value!
  //int key=11268;
  //bool isFound= linearSearch(data,key);

	//Testing2
	//testing with random value
	srand(static_cast<unsigned int>(time(0)));
	int randomval=1+ rand()%1000000;

	//unless the linearSearch method is completed, main method will not work
	bool isFound=linearSearch(data,randomval);
  auto t2 = std::chrono::high_resolution_clock::now();

	if (isFound)
		cout<<"The key value --> " << randomval << " was found! " << endl;
	else
		cout<<"The key value --> " << randomval << " was not found! " << endl;

	cout << "Size of the vector : "<< data.size() << endl;
	cout << "Linear Search method  took "
      << std::chrono::duration_cast<std::chrono::nanoseconds>(t2-t1).count()
			<< " nanoseconds \n";

	return 0;



}
