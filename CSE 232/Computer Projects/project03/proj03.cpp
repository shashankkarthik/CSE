/*
CSE 232 - Project 3
Shashank Karthikeyan
Section 2
*/

#include <iostream>
#include <cmath>
using std::cout; using std::cin; using std::endl;


//Checks if first is greater than second, if so switches them.
void order_parameters(int &first, int &second)
{
	if (first > second)
	{
		//Temporary variable to store values of first and second such that they
		//are not lost when switching. 
		int temp_var = first;
		first = second;
		second = temp_var;	
			
	}
}

//Checks if integer is a NN given order of NN(power)
bool narc_num(int num, int power)
{
	int narc_sum = 0;
	int num_copy = num;
	int num_digit;
	
	while(num_copy > 0)
	{
		num_digit = num_copy % 10;	//Gets the rightmost digit
		narc_sum += pow(num_digit,power); //Raises it to the power and adds it to a running sum
		num_copy /= 10; //Removes the rightmost digit
	}
	
	if((narc_sum == num)) 
	{
		return true;
	}
	else
	{
		return false;
	}
}

int check_range(int first, int last, int power)
{
	int narc_count = 0;
	for(int i = first; i <= last; i++) //Iterates through each int value between first and last
	{
		bool test = narc_num(i,power);
		if(test)
		{
			cout << i << " is a narcissistic number of order: " << power << endl;
			narc_count += 1;
		}
	}
	cout << "Saw " << narc_count << " order " << power << " narc numbers in the range " << 
	first << " to " << last << endl;
	
	return 0;
}


int main()
{
	int test_cases;
	cin >> test_cases; // Gets # of test cases
	
	for(int i = 1; i <= test_cases; i++) //Runs for each test case
	{
		int first;
		int last;
		int order;
		
		cin >> first >> last;
		order_parameters(first,last);
		cin >> order;
		
		check_range(first,last,order);
		cout << endl;	
				
		
	}
}
