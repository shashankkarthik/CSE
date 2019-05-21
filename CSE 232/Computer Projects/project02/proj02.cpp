/* Project 2
 * Shashank Karthikeyan
 * Section 2
*/

#include <iostream>
#include <cmath>
#include <iomanip>
using std::cout; using std::endl; using std::cin; using std::setw; using std::setprecision;


//Calculates the value of n!
double factorial (long n)
{
	double mult = 1;
	double total = 1;
	while(mult <= n)
	{
		total *= mult;
		mult += 1;
	}
	return total;	
}

//Calculates sum [from k=0 to k= (n-1)/2] of 1/(2k+1)
double term (long n)
{
	double k = 0;
	double sum = 0;
	while (k <= floor((n-1)/2))
	{
		sum += 1.0/(2*k+1);
		k += 1;
	}
	return sum;	
}



int main()
{
	long test,iter;
	double x;
	double gamma = 0.577215664901532; //Gamma Constant
	long test_count=1; 
	long n=1;
	double sum_inf = 0.0;
	
	cin >> test; // Gets number of test cases from input file
	cin >> x >> iter; //Gets first x and interation numbers
	
	while(test_count <= test) //Runs while there are still test cases left
	{			
		n = 1;
		sum_inf = 0;
		while(n<=iter) //Finds sum for each value of n in range of n values.
		{	
			double factorial_term = pow(-1.0,n-1.0)*pow(log(x),n)/(factorial(n)*pow(2.0,n-1.0));
			double sum_terms = factorial_term * term(n);
			sum_inf += sum_terms;		
			n += 1;	
		}
		
		double total = gamma + log(log(x)) + sqrt(x) * sum_inf; //Calculates final value of Li(x) for current test case.
		cout << "x:" << setw(15)<< std::fixed << setprecision(0)<< x;
		cout << ", iters: " << setw(2) << iter << setw(4);
		cout << ", Li(x)=" << setw(15) << setprecision(3)<<total << endl;
		test_count += 1;
		cin >> x >> iter; //Prompts for the next x and iteration numbers
	}
}





